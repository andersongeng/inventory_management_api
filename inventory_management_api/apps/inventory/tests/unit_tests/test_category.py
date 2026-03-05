import pytest
from inventory.models import Category

pytestmark = pytest.mark.django_db

def test_category_creation():
    # Arrange and act 
    category = Category.objects.create(name="Construction")

    # Assert: Verify product on DB
    assert category.name == "Construction"
    assert str(category) == "Construction"

def test_category_verbose_name_plural():
    # Assert: Meta verbose name plural
    assert str(Category._meta.verbose_name_plural) == "Categories"