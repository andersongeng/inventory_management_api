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