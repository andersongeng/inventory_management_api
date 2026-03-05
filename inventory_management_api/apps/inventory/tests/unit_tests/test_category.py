import pytest
from inventory.models import Category

@pytest.mark.django_db
def test_category_creation():
    category = Category.objects.create(name="Construction")
    assert category.name == "Construction"
    assert str(category) == "Construction"