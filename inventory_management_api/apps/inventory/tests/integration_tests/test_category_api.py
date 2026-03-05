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