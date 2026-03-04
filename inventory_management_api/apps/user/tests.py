import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

@pytest.mark.django_db
def test_user_login_returns_jwt(api_client):
    # 1. Arrange (Preparar el escenario)
    username = "testuser"
    password = "securepassword123"
    User.objects.create_user(username=username, password=password)

    # 2. Act (Ejecutar la acción)
    response = api_client.post('/api/login/', {
        "username": username,
        "password": password
    }, format='json')

    # 3. Assert (Verificar resultados)
    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data