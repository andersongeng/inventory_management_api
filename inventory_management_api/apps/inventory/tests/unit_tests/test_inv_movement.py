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
    # Assert: Verifying representation
    # representation should be something like: "IN - Screw (100)"
    assert str(movement) == f"IN - {product.name} (100)"

def test_movement_choices_validation(create_test_user):
    # Arrange: Create product
    product = Product.objects.create(name="Tornillo", sku="TOR", price=1, created_by=create_test_user)
    
    # Arrange: Create product movement verifying the choices
    movement = InventoryMovement(
        product=product,
        user=create_test_user,
        type=InventoryMovement.MovementType.OUTBOUND,
        quantity=5
    )

    # Assert: check the correct choice
    assert movement.type == "OUT"