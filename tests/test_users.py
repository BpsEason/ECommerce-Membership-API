import pytest
from fastapi.testclient import TestClient
from ..main import app
from ..database import SessionLocal, engine
from ..models.user import User
from ..models.address import Address

@pytest.fixture
def client():
    """創建測試客戶端"""
    return TestClient(app)

@pytest.fixture
def db():
    """創建測試資料庫會話"""
    User.metadata.create_all(bind=engine)
    Address.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    db.close()

def test_register_user(client, db):
    """測試使用者註冊"""
    response = client.post("/auth/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "Test1234",
        "full_name": "Test User",
        "phone_number": "1234567890"
    })
    assert response.status_code == 201
    assert response.json()["username"] == "testuser"