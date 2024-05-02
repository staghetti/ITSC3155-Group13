import pytest
from fastapi.testclient import TestClient
from ..main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def create_customer(client):
    customer_data = {
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "phone_number": "708-567-8362",
        "address": "New Home Street"
    }
    response = client.post("/customers/", json=customer_data)
    assert response.status_code == 200, "Failed to create customer"
    return response.json()['id']


def test_create_order(client, create_customer):
    customer_id = create_customer
    order_data = {
        "customer_name": "Jane Doe",
        "description": "Test order",
        "customer_id": customer_id,
        "is_guest": False,
        "order_type": "Takeout",
        "promo_code": ""
    }

    response = client.post("/orders/", json=order_data)
    assert response.status_code == 200, "Failed to create order"
    assert response.json()['customer_name'] == order_data['customer_name'], "Customer name mismatch"
    assert response.json()['order_type'] == order_data['order_type'], "Order type mismatch"
