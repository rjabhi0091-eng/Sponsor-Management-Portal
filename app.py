from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import or_, text
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles


import portal.models as models
import portal.schemas as schemas
from portal.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

with engine.connect() as connection:
    def existing_columns(table_name: str):
        result = connection.execute(text(f"PRAGMA table_info({table_name})"))
        return [row[1] for row in result.fetchall()]

    if "sponsor_id" not in existing_columns("clients"):
        connection.execute(text("ALTER TABLE clients ADD COLUMN sponsor_id INTEGER"))
    if "password_hash" not in existing_columns("sponsors"):
        connection.execute(text("ALTER TABLE sponsors ADD COLUMN password_hash TEXT DEFAULT ''"))
    if "password_hash" not in existing_columns("clients"):
        connection.execute(text("ALTER TABLE clients ADD COLUMN password_hash TEXT DEFAULT ''"))

app = FastAPI(
    title="Sponsor and Client Management Portal",
    description="Backend API and UI for managing sponsors and clients in a single portal.",
    version="0.1.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=FileResponse, tags=["ui"])
def root():
    return FileResponse("static/index.html")


@app.post("/sponsors/", response_model=schemas.Sponsor, tags=["sponsors"])
def create_sponsor(sponsor: schemas.SponsorCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Sponsor).filter(models.Sponsor.name == sponsor.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Sponsor with this name already exists")
    sponsor_data = sponsor.dict(exclude={"password"})
    db_sponsor = models.Sponsor(**sponsor_data)
    db_sponsor.set_password(sponsor.password)
    db.add(db_sponsor)
    db.commit()
    db.refresh(db_sponsor)
    return db_sponsor


@app.get("/sponsors/", response_model=list[schemas.Sponsor], tags=["sponsors"])
def list_sponsors(skip: int = 0, limit: int = 100, search: str | None = None, status: str | None = None, db: Session = Depends(get_db)):
    query = db.query(models.Sponsor)
    if search:
        filter_value = f"%{search}%"
        query = query.filter(
            or_(
                models.Sponsor.name.ilike(filter_value),
                models.Sponsor.email.ilike(filter_value),
                models.Sponsor.phone.ilike(filter_value),
                models.Sponsor.status.ilike(filter_value),
                models.Sponsor.notes.ilike(filter_value),
            )
        )
    if status:
        query = query.filter(models.Sponsor.status == status)
    return query.offset(skip).limit(limit).all()


@app.get("/sponsors/{sponsor_id}", response_model=schemas.Sponsor, tags=["sponsors"])
def get_sponsor(sponsor_id: int, db: Session = Depends(get_db)):
    sponsor = db.query(models.Sponsor).filter(models.Sponsor.id == sponsor_id).first()
    if not sponsor:
        raise HTTPException(status_code=404, detail="Sponsor not found")
    return sponsor


@app.put("/sponsors/{sponsor_id}", response_model=schemas.Sponsor, tags=["sponsors"])
def update_sponsor(sponsor_id: int, sponsor_update: schemas.SponsorUpdate, db: Session = Depends(get_db)):
    sponsor = db.query(models.Sponsor).filter(models.Sponsor.id == sponsor_id).first()
    if not sponsor:
        raise HTTPException(status_code=404, detail="Sponsor not found")
    update_data = sponsor_update.dict(exclude_unset=True)
    if "password" in update_data:
        sponsor.set_password(update_data.pop("password"))
    for field, value in update_data.items():
        setattr(sponsor, field, value)
    db.commit()
    db.refresh(sponsor)
    return sponsor


@app.delete("/sponsors/{sponsor_id}", status_code=204, tags=["sponsors"])
def delete_sponsor(sponsor_id: int, db: Session = Depends(get_db)):
    sponsor = db.query(models.Sponsor).filter(models.Sponsor.id == sponsor_id).first()
    if not sponsor:
        raise HTTPException(status_code=404, detail="Sponsor not found")
    db.delete(sponsor)
    db.commit()
    return None


@app.post("/clients/", response_model=schemas.Client, tags=["clients"])
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Client).filter(models.Client.name == client.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Client with this name already exists")
    if client.sponsor_id:
        sponsor = db.query(models.Sponsor).filter(models.Sponsor.id == client.sponsor_id).first()
        if not sponsor:
            raise HTTPException(status_code=400, detail="Assigned sponsor does not exist")
    client_data = client.dict(exclude={"password"})
    db_client = models.Client(**client_data)
    db_client.set_password(client.password)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


@app.get("/sponsors/{sponsor_id}/clients", response_model=list[schemas.Client], tags=["sponsors"])
def list_sponsor_clients(sponsor_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sponsor = db.query(models.Sponsor).filter(models.Sponsor.id == sponsor_id).first()
    if not sponsor:
        raise HTTPException(status_code=404, detail="Sponsor not found")
    return db.query(models.Client).filter(models.Client.sponsor_id == sponsor_id).offset(skip).limit(limit).all()


@app.get("/clients/", response_model=list[schemas.Client], tags=["clients"])
def list_clients(skip: int = 0, limit: int = 100, search: str | None = None, status: str | None = None, db: Session = Depends(get_db)):
    query = db.query(models.Client)
    if search:
        filter_value = f"%{search}%"
        query = query.filter(
            or_(
                models.Client.name.ilike(filter_value),
                models.Client.email.ilike(filter_value),
                models.Client.company.ilike(filter_value),
                models.Client.phone.ilike(filter_value),
                models.Client.status.ilike(filter_value),
                models.Client.notes.ilike(filter_value),
            )
        )
    if status:
        query = query.filter(models.Client.status == status)
    return query.offset(skip).limit(limit).all()


@app.get("/clients/{client_id}", response_model=schemas.Client, tags=["clients"])
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client


@app.get("/summary", response_model=schemas.Summary, tags=["dashboard"])
def get_summary(db: Session = Depends(get_db)):
    total_sponsors = db.query(models.Sponsor).count()
    total_clients = db.query(models.Client).count()
    active_clients = db.query(models.Client).filter(models.Client.status == "active").count()
    prospect_sponsors = db.query(models.Sponsor).filter(models.Sponsor.status == "prospect").count()
    return schemas.Summary(
        total_sponsors=total_sponsors,
        total_clients=total_clients,
        active_clients=active_clients,
        prospect_sponsors=prospect_sponsors,
    )


@app.post("/auth/sponsor-login", response_model=schemas.LoginResponse, tags=["auth"])
def sponsor_login(payload: schemas.UserLogin, db: Session = Depends(get_db)):
    sponsor = db.query(models.Sponsor).filter(models.Sponsor.email == payload.email).first()
    if not sponsor or not sponsor.verify_password(payload.password):
        raise HTTPException(status_code=401, detail="Invalid sponsor credentials")
    return schemas.LoginResponse(role="sponsor", name=sponsor.name, message="Sponsor login successful")


@app.post("/auth/client-login", response_model=schemas.LoginResponse, tags=["auth"])
def client_login(payload: schemas.UserLogin, db: Session = Depends(get_db)):
    client = db.query(models.Client).filter(models.Client.email == payload.email).first()
    if not client or not client.verify_password(payload.password):
        raise HTTPException(status_code=401, detail="Invalid client credentials")
    return schemas.LoginResponse(role="client", name=client.name, message="Client login successful")


@app.put("/clients/{client_id}", response_model=schemas.Client, tags=["clients"])
def update_client(client_id: int, client_update: schemas.ClientUpdate, db: Session = Depends(get_db)):
    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    update_data = client_update.dict(exclude_unset=True)
    if "sponsor_id" in update_data:
        sponsor_id = update_data["sponsor_id"]
        if sponsor_id:
            sponsor = db.query(models.Sponsor).filter(models.Sponsor.id == sponsor_id).first()
            if not sponsor:
                raise HTTPException(status_code=400, detail="Assigned sponsor does not exist")
    if "password" in update_data:
        client.set_password(update_data.pop("password"))
    for field, value in update_data.items():
        setattr(client, field, value)
    db.commit()
    db.refresh(client)
    return client


@app.delete("/clients/{client_id}", status_code=204, tags=["clients"])
def delete_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    db.delete(client)
    db.commit()
    return None
