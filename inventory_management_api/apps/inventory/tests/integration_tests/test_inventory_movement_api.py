import pytest
from inventory.models import Product, InventoryMovement

@pytest.mark.django_db
def test_inbound_movement_updates_stock(auth_client, create_test_user):
    """Test to check product stock update by movement"""
    # Arrange: Product with stock 0
    product = Product.objects.create(
        name="Drill", sku="DRI01", price=100, created_by=create_test_user
    )
    url = '/api/inventory_movements/'
    payload = {
        "product": product.id,
        "type": "IN",
        "quantity": 50,
        "comment": "Initial buy"
    }

    # Act: Send POST request
    response = auth_client.post(url, payload)

    # Assert: Verify API response
    assert response.status_code == 201

    # Assert: Verify stock updated on db
    product.refresh_from_db()
    assert product.stock == 50  # 0 + 50
    assert response.data['user'] == create_test_user.id