from fastapi.testclient import TestClient
from ..main import app
import pytest


@pytest.fixture
def client():
    return TestClient(app)


def test_create_order(client):
    order_data = {
        "customer_name": "Customer Name Test",
        "description": "Test order",
        "customer_id": 1,
        "is_guest": False,
        "order_type": "Takeout",
        "promo_code": "B4UEAT"
    }

    response = client.post("/orders/", json=order_data)
    assert response.status_code == 200
    assert response.json()['customer_name'] == "Customer Name Test"
    assert response.json()['customer_id'] == 1
    assert response.json()['is_guest'] is False
    assert response.json()['order_type'] == "Takeout"
