import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def api_client():
    """Provide a DRF client to make requests"""
    return APIClient()

@pytest.fixture
def create_test_user(db):
    """Fixture to create a base user quickly"""
    return User.objects.create_user(username="validuser", password="correct_password123")

@pytest.fixture
def auth_client(create_test_user):
    """Create an API Client and authenticate automatically with test_user"""
    client = APIClient()
    client.force_authenticate(user=create_test_user)
    return client