import pytest
from inventory.models import Category

pytestmark = pytest.mark.django_db

def test_category_creation():
    category = Category.objects.create(name="Construction")
    assert category.name == "Construction"
    assert str(category) == "Construction"

def test_category_verbose_name_plural():
    # Verifica que el Meta esté bien configurado (Categories)
    assert str(Category._meta.verbose_name_plural) == "Categories"