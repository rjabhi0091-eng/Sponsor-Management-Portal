import httpx

BASE_URL = "http://127.0.0.1:8000"

def test_contact_endpoint():
    payload = {
        "name": "Test User",
        "email": "test@example.com",
        "message": "This is a test message"
    }
    response = httpx.post(f"{BASE_URL}/contact/message", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "status" in data

def test_chat_endpoint():
    payload = {"message": "help"}
    response = httpx.post(f"{BASE_URL}/chat/assistant", json=payload)
    assert response.status_code == 200
    assert "reply" in response.json()

def test_admin_auth_failure():
    # Attempting to fetch clients without token should fail
    response = httpx.get(f"{BASE_URL}/clients/")
    assert response.status_code in (401, 403)

def test_marketing_endpoint():
    payload = {
        "title": "Test Campaign",
        "platform": "Instagram",
        "status": "planning",
        "metrics": "{}"
    }
    response = httpx.post(f"{BASE_URL}/marketing/campaigns", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Campaign"

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
