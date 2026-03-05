import pytest
from inventory.models import Product, Category

@pytest.mark.django_db
def test_list_products(auth_client, create_test_user):
    # Arrange
    Product.objects.create(name="P1", sku="SKU1", price=10, created_by=create_test_user)
    Product.objects.create(name="P2", sku="SKU2", price=20, created_by=create_test_user)
    
    # Act
    response = auth_client.get('/api/products/')
    
    # Assert
    assert response.status_code == 200
    assert len(response.data) >= 2 # Verificamos que al menos hay 2

@pytest.mark.django_db
def test_create_product_api(auth_client, create_test_user):
    # Arrange: Frontend data
    url = '/api/products/'
    payload = {
        "name": "Sierra Circular",
        "sku": "SIE001",
        "price": "45.50",
    }

    # Act: Send POST request
    response = auth_client.post(url, payload, format='json')

    # Assert: Verify API response
    if response.status_code != 201:
        print(f"\nErrores del Serializer: {response.data}")

    assert response.status_code == 201
    assert response.data['name'] == "Sierra Circular"
    assert response.data['created_by'] == create_test_user.id

    # Verify if the new product exists on the database
    assert Product.objects.filter(sku="SIE001").exists()

@pytest.mark.django_db
def test_create_duplicate_sku(auth_client):
    # Arrange: Create first object
    Product.objects.create(name="Original", sku="UNIQ123", price=10, stock=5)
    
    # Arrange: Data to create a second one with the same sku
    payload = {"name": "Copia", "sku": "UNIQ123", "price": 5}

    # Act: Send POST request
    response = auth_client.post('/api/products/', payload)
    
    # Assert: Verify API response
    assert response.status_code == 400
    assert "sku" in response.data

@pytest.mark.django_db
def test_sku_validation_alphanumeric(auth_client):
    # Arrange: Data to create a new product
    payload = {"name": "Producto Malo", "sku": "SKU-@#", "price": 10}

    # Act: Send POST request
    response = auth_client.post('/api/products/', payload)
    
    # Assert: Verify API response
    assert response.status_code == 400
    assert "sku" in response.data
    assert "letras y números" in str(response.data['sku'])

@pytest.mark.django_db
def test_negative_price(auth_client):
    # Arrange: Data to create a new product
    payload = {"name": "Test", "sku": "TEST", "price": -10}

    # Act: Send POST request
    response = auth_client.post('/api/products/', payload)

    # Assert: Verify API response
    assert response.status_code == 400

@pytest.mark.django_db
def test_update_product_ignores_stock(auth_client, create_test_user):
    # Arrange: Data to create a product with stock
    product = Product.objects.create(
        name="Taladro", sku="TAL01", price=50, stock=10, created_by=create_test_user
    )

    # Arrange: Define the url to get the created product
    url = f'/api/products/{product.id}/'
    
    # Arrange: Data to update fields of the product
    payload = {"name": "Taladro Pro", "stock": 999}

    # Act: Send PATCH request
    response = auth_client.patch(url, payload)
    
    # Assert: Verify API response
    assert response.status_code == 200
    assert response.data['name'] == "Taladro Pro"
    # Stock should ignore the new stock value
    assert response.data['stock'] == 10

@pytest.mark.django_db
def test_delete_product(auth_client, create_test_user):
    # Arrange
    product = Product.objects.create(name="Borrar", sku="DEL", price=5, created_by=create_test_user)
    url = f'/api/products/{product.id}/'
    
    # Act
    response = auth_client.delete(url)
    
    # Assert
    assert response.status_code == 204
    assert not Product.objects.filter(id=product.id).exists()

@pytest.mark.django_db
def test_create_product_with_category(auth_client, create_test_user):
    # Arrange: Create Category
    category = Category.objects.create(name="Tools")
    
    # Arrange: Data to create a product
    url = '/api/products/'
    payload = {
        "name": "Destornillador",
        "sku": "DEST01",
        "price": "5.99",
        "category": category.id  # Send only ID
    }
    
    # Act: Send POST request
    response = auth_client.post(url, payload)
    
    # Assert: Verify API response
    assert response.status_code == 201
    assert response.data['category'] == category.id
    
    # Verify DB
    product = Product.objects.get(sku="DEST01")
    assert product.category.name == "Tools"

@pytest.mark.django_db
def test_create_product_invalid_category(auth_client):
    url = '/api/products/'
    payload = {
        "name": "Ghost product",
        "sku": "GHOST",
        "price": "10.00",
        "category": 9999  # ID do not exist
    }
    
    response = auth_client.post(url, payload)
    
    assert response.status_code == 400
    assert "category" in response.data