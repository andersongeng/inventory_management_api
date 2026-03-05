import pytest
from inventory.models import Product
from decimal import Decimal

pytestmark = pytest.mark.django_db

def test_create_product(create_test_user):
    # Arrange
    new_product = Product.objects.create(
        name = "Drill",
        sku = "DRI01",
        price = 1, # Recieve an Integer and parse it to Decimal
        stock = 10,
        created_by = create_test_user
    )

    # Asserts: Verify product on DB
    assert new_product.name == "Drill"
    assert new_product.created_by == create_test_user
    assert new_product.price == Decimal("1.00")