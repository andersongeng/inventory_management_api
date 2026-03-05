import pytest
from inventory.models.category import Category

@pytest.mark.django_db
def test_create_category_success(auth_client):
    """Test to create a category successfully"""

    # Arrange: Data to create a category
    url = '/api/categories/'
    payload = {"name": "Herramientas Eléctricas"}
    
    # Act: Send POST request
    response = auth_client.post(url, payload)
    
    # Assert: Verify API response
    assert response.status_code == 201
    assert response.data['name'] == "Herramientas Eléctricas"
    assert Category.objects.filter(name="Herramientas Eléctricas").exists()

@pytest.mark.django_db
def test_create_duplicate_category(auth_client):
    """Test do not allow duplicate categories"""

    # Arrange: Create a first category
    Category.objects.create(name="Construcción")

    # Arrange: Data to create a second category
    url = '/api/categories/'
    payload = {"name": "Construcción"}
        
    # Act: Send POST request
    response = auth_client.post(url, payload)
        
    # Assert: Verify API response
    assert response.status_code == 400
    assert "name" in response.data # DRF devuelve error de campo único

def test_list_categories(auth_client):
    """Test to retrieve all categories created"""

    # Arrange: Create categories
    Category.objects.create(name="Madera")
    Category.objects.create(name="Pintura")
    
    # Act: Send GET request
    response = auth_client.get('/api/categories/')
    
    # Assert: Verify API response
    assert response.status_code == 200

    # Use 'results' in case of pagination
    results = response.data.get('results', response.data)
    assert len(results) >= 2

def test_update_category(auth_client):
    """Test to update a category"""

    # Arrange:
    category = Category.objects.create(name="Plomeria")

    # Arrange: Data to update the created category
    url = f'/api/categories/{category.id}/'
    payload = {"name": "Plomería Avanzada"}
    
    # Act: Send PUT request
    response = auth_client.put(url, payload)
    
    # Assert: Verify API response
    assert response.status_code == 200
    category.refresh_from_db()
    assert category.name == "Plomería Avanzada"