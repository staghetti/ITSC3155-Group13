import pytest
from fastapi.testclient import TestClient
from ..main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_create_customer(client):
    customer_data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone_number": "000-000-0000",
        "address": "New Address"
    }
    response = client.post("/customers/", json=customer_data)
    assert response.status_code == 200, "Failed to create customer"
    data = response.json()
    assert data['name'] == "John Doe"
    assert data['email'] == "john.doe@example.com"
    assert data['phone_number'] == "000-000-0000"
    assert data['address'] == "New Address"
