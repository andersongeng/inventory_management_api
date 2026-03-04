import pytest
from inventory.models import Product

@pytest.mark.django_db
def test_create_product_api(auth_client, create_test_user):
    # 1. Arrange: Frontend data
    url = '/api/products/'
    payload = {
        "name": "Sierra Circular",
        "sku": "SIE001",
        "price": "45.50",
    }

    # 2. Act: Send POST request
    response = auth_client.post(url, payload, format='json')

    # 3. Assert: Verify API response
    if response.status_code != 201:
        print(f"\nErrores del Serializer: {response.data}")

    assert response.status_code == 201
    assert response.data['name'] == "Sierra Circular"
    assert response.data['created_by'] == create_test_user.id

    # 4. Verify if the new product exists on the database
    assert Product.objects.filter(sku="SIE001").exists()

@pytest.mark.django_db
def test_create_duplicate_sku(auth_client):
    # Create first object
    Product.objects.create(name="Original", sku="UNIQ123", price=10, stock=5)
    
    # Try create a second one with the same sku
    payload = {"name": "Copia", "sku": "UNIQ123", "price": 5}
    response = auth_client.post('/api/products/', payload)
    
    assert response.status_code == 400
    assert "sku" in response.data

@pytest.mark.django_db
def test_negative_price(auth_client):
    payload = {"name": "Test", "sku": "TEST", "price": -10}

    response = auth_client.post('/api/products/', payload)

    assert response.status_code == 400