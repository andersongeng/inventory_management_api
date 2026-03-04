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
        "stock": 20
    }

    # 2. Act: Send POST request
    response = auth_client.post(url, payload, format='json')

    # 3. Assert: Verify API response
    if response.status_code != 201:
        print(f"\nErrores del Serializer: {response.data}")

    assert response.status_code == 201
    assert response.data['name'] == "Sierra Circular"
    # Verify created_by attribute were asigned to the product
    assert response.data['created_by'] == create_test_user.id

    # 4. Verify if the new product exists on the database
    assert Product.objects.filter(sku="SIE001").exists()