import pytest
from inventory.models import Product
from decimal import Decimal

pytestmark = pytest.mark.django_db

def test_create_product(create_test_user):
    # 1. Create new product
    new_product = Product.objects.create(
        name = "Drill",
        sku = "DRI01",
        price = 1, # Recieve an Integer and parse it to Decimal
        stock = 10,
        created_by = create_test_user
    )
    print(new_product.created_by_id)

    # 2. Asserts
    assert new_product.name == "Drill"
    assert new_product.created_by == create_test_user
    assert new_product.price == Decimal("1.00")