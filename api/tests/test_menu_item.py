from fastapi.testclient import TestClient
from ..main import app
import pytest


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def create_category(client):
    category_data = {"name": "New Food category"}
    response = client.post("/categories/", json=category_data)
    assert response.status_code == 200, f"Category creation failed: {response.json()}"
    return response.json()['id']


def test_create_menu_item(client, create_category):
    category_id = create_category
    menu_item_data = {
        "name": "New Test Menu Item",
        "description": "New Tasty menu item",
        "price": 20.00,
        "category_id": category_id,
    }
    response = client.post("/menuitems/", json=menu_item_data)
    assert response.status_code == 200, f"Menu item creation failed: {response.json()}"
    data = response.json()
    assert data['name'] == "New Test Menu Item"
    assert data['description'] == "New Tasty menu item"
    assert data['price'] == 20.00
    assert data['category_id'] == category_id
