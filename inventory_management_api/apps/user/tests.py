import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_user_login_returns_jwt(api_client, create_test_user):
    # 1. Act (Ejecutar la acción)
    response = api_client.post('/api/login/', {
        "username": "validuser",
        "password": "correct_password123"
    }, format='json')

    # 3. Assert (Verificar resultados)
    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data

@pytest.mark.django_db
class TestLoginEdgeCases:

    def test_login_wrong_password(self, api_client, create_test_user):
        """1. Credenciales incorrectas: Password erróneo"""
        response = api_client.post('/api/login/', {
            "username": "validuser",
            "password": "wrong_password"
        })
        assert response.status_code == 401  # O 400, dependiendo de tu SimpleJWT config
        assert 'access' not in response.data

    def test_login_non_existent_user(self, api_client):
        """2. Usuario que no existe en la base de datos"""
        response = api_client.post('/api/login/', {
            "username": "ghost_user",
            "password": "some_password"
        })
        assert response.status_code == 401

    def test_login_missing_fields(self, api_client):
        """3. Campos faltantes en el JSON (Payload incompleto)"""
        # Enviamos solo el username sin el password
        response = api_client.post('/api/login/', {"username": "admin"})
        assert response.status_code == 400
        assert 'password' in response.data # DRF suele indicar qué campo falta

    def test_login_inactive_user(self, api_client, create_test_user):
        """4. Usuario desactivado (is_active = False)"""
        create_test_user.is_active = False
        create_test_user.save()
        
        response = api_client.post('/api/login/', {
            "username": "validuser",
            "password": "correct_password123"
        })
        # Un usuario desactivado no debe poder obtener tokens
        assert response.status_code == 401