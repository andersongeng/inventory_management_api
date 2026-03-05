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

def test_outbound_movement_updates_stock(auth_client, create_test_user):
    """Test to check if an OUTBOUND discount product stock"""
    # Arrange: Product with initial stock of 20
    product = Product.objects.create(
        name="Sierra", sku="SIE01", price=50, stock=20, created_by=create_test_user
    )

    # Arrange: Data to make an OUTBOUND
    url = '/api/inventory_movements/'
    payload = {
        "product": product.id,
        "type": "OUT",
        "quantity": 5,
        "comment": "Sell to customer"
    }

    # Act: Send POST request
    response = auth_client.post(url, payload)

    # Assert: Verify API response
    assert response.status_code == 201
    product.refresh_from_db()
    assert product.stock == 15  # 20 - 5

def test_movement_requires_positive_quantity(auth_client, create_test_user):
    """Test do not allow outbounds of 0 or less"""
    product = Product.objects.create(name="Screw", sku="SCR", price=1, created_by=create_test_user)
    url = '/api/inventory_movements/'
    payload = {
        "product": product.id,
        "type": "IN",
        "quantity": 0  # Invalid quantity
    }

    # Act: Send POST request
    response = auth_client.post(url, payload)
    
    # Assert: Positive integer field or serializer should raise 400
    assert response.status_code == 400

def test_outbound_insufficient_stock(auth_client, create_test_user):
    """Test do not allow an outbound greater than available stock"""

    # Arrange:
    product = Product.objects.create(
        name="iPhone", sku="IPH", price=1000, stock=5, created_by=create_test_user
    )

    # Arrange: Data to make an OUTBOUND
    payload = {
        "product": product.id,
        "type": "OUT",
        "quantity": 10  # Try make an OUTBOUND greater than stock available
    }
    
    # Act: Send a POST request
    response = auth_client.post('/api/inventory_movements/', payload)
    
    # Assert: Verify API response
    assert response.status_code == 400
    assert "stock" in str(response.data).lower()