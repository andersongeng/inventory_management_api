import pytest
from inventory.models import Product, InventoryMovement

pytestmark = pytest.mark.django_db

def test_movement_str_representation(create_test_user):
    # Arrange: Create product
    product = Product.objects.create(name="Screw", sku="SCR", price=1, created_by=create_test_user)

    # Arrange: Create movement of the product
    movement = InventoryMovement.objects.create(
        product=product,
        user=create_test_user,
        type="IN",
        quantity=100
    )
    # representation should be something like: "IN - Screw (100)"
    assert str(movement) == f"IN - {product.name} (100)"