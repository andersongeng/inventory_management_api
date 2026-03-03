from django.urls import path, include
from inventory.views import ProductViewSet, CategoryViewSet, InventoryMovementViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"inventory_movements", InventoryMovementViewSet, basename="inventory_movement")

urlpatterns = [
    path('', include(router.urls)),
]