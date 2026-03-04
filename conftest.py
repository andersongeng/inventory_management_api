import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def api_client():
    """Proporciona un cliente de DRF para hacer peticiones a la API"""
    return APIClient()