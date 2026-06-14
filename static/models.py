import hashlib

from sqlalchemy import Column, Integer, String, Text, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Sponsor(Base):
    __tablename__ = "sponsors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False, unique=True)
    email = Column(String(200), nullable=False)
    phone = Column(String(50), nullable=True)
    status = Column(String(50), nullable=False, default="prospect")
    notes = Column(Text, nullable=True)
    password_hash = Column(String(256), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    clients = relationship("Client", back_populates="sponsor", cascade="all, delete-orphan")

    def set_password(self, password: str):
        self.password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()

    def verify_password(self, password: str) -> bool:
        return self.password_hash == hashlib.sha256(password.encode("utf-8")).hexdigest()


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False, unique=True)
    email = Column(String(200), nullable=False)
    phone = Column(String(50), nullable=True)
    company = Column(String(200), nullable=True)
    sponsor_id = Column(Integer, ForeignKey("sponsors.id"), nullable=True)
    status = Column(String(50), nullable=False, default="active")
    notes = Column(Text, nullable=True)
    password_hash = Column(String(256), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    sponsor = relationship("Sponsor", back_populates="clients")

    def set_password(self, password: str):
        self.password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()

    def verify_password(self, password: str) -> bool:
        return self.password_hash == hashlib.sha256(password.encode("utf-8")).hexdigest()

    @property
    def sponsor_name(self):
        return self.sponsor.name if self.sponsor else None


class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(128), nullable=False, unique=True)
    email = Column(String(200), nullable=False, unique=True)
    password_hash = Column(String(256), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def set_password(self, password: str):
        self.password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()

    def verify_password(self, password: str) -> bool:
        return self.password_hash == hashlib.sha256(password.encode("utf-8")).hexdigest()
