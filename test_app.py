import pytest
from fastapi.testclient import TestClient
import sys
import os

# Add statics directory to path so we can import app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'statics'))
from app import app

client = TestClient(app)

def test_contact_endpoint():
    payload = {
        "name": "Test User",
        "email": "test@example.com",
        "message": "This is a test message"
    }
    response = client.post("/contact/message", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "status" in data

def test_chat_endpoint():
    payload = {"message": "help"}
    response = client.post("/chat/assistant", json=payload)
    assert response.status_code == 200
    assert "reply" in response.json()

def test_admin_auth_failure():
    # Attempting to fetch clients without token should fail
    response = client.get("/clients/")
    assert response.status_code in (401, 403)


def test_admin_login_with_default_password():
    response = client.post(
        "/auth/admin-login",
        json={"email": "admin", "password": "Admin@2026!"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["role"] == "admin"


def test_marketing_endpoint():
    payload = {
        "title": "Test Campaign",
        "platform": "Instagram",
        "status": "planning",
        "metrics": "{}"
    }
    response = client.post("/marketing/campaigns", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Campaign"


def test_public_page_routes():
    for route in ["/about", "/media", "/registration", "/contact", "/work"]:
        response = client.get(route)
        assert response.status_code == 200

if __name__ == "__main__":
    try:
        test_contact_endpoint()
        print("Contact endpoint test passed.")
        test_chat_endpoint()
        print("Chat endpoint test passed.")
        test_admin_auth_failure()
        print("Admin auth test passed.")
        test_marketing_endpoint()
        print("Marketing endpoint test passed.")
        print("ALL TESTS PASSED SUCCESSFULLY.")
    except AssertionError as e:
        print(f"Test failed: {e}")
