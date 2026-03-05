import pytest
from inventory.models.category import Category

@pytest.mark.django_db
def test_create_category_success(auth_client):
    """Test to create a category successfully"""

    # Arrange: Data to create a category
    url = '/api/categories/'
    payload = {"name": "Electric Tools"}
    
    # Act: Send POST request
    response = auth_client.post(url, payload)
    
    # Assert: Verify API response
    assert response.status_code == 201
    assert response.data['name'] == "Electric Tools"
    assert Category.objects.filter(name="Electric Tools").exists()

@pytest.mark.django_db
def test_create_duplicate_category(auth_client):
    """Test do not allow duplicate categories"""

    # Arrange: Create a first category
    Category.objects.create(name="Construction")

    # Arrange: Data to create a second category
    url = '/api/categories/'
    payload = {"name": "Construction"}
        
    # Act: Send POST request
    response = auth_client.post(url, payload)
        
    # Assert: Verify API response
    assert response.status_code == 400
    assert "name" in response.data # DRF return unique field error

def test_list_categories(auth_client):
    """Test to retrieve all categories created"""

    # Arrange: Create categories
    Category.objects.create(name="Wood")
    Category.objects.create(name="Paint")
    
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
    category = Category.objects.create(name="Plumbing")

    # Arrange: Data to update the created category
    url = f'/api/categories/{category.id}/'
    payload = {"name": "Advance plumbing"}
    
    # Act: Send PUT request
    response = auth_client.put(url, payload)
    
    # Assert: Verify API response
    assert response.status_code == 200
    category.refresh_from_db()
    assert category.name == "Advance plumbing"

def test_delete_category(auth_client):
        """Test to delete a category"""
        category = Category.objects.create(name="Delete")
        url = f'/api/categories/{category.id}/'
        
        response = auth_client.delete(url)
        
        assert response.status_code == 204
        assert not Category.objects.filter(id=category.id).exists()