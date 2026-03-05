from inventory.models import InventoryMovement
from inventory.serializers import InventoryMovementSerializer
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(
        summary="List inventory movements",
        description="Retrieve a full history of stock movements, including ins, outs, and adjustments."
    ),
    create=extend_schema(
        summary="Record a movement",
        description=(
            "Create a new inventory movement. Note: The system automatically "
            "assigns the movement to the currently authenticated user."
        )
    ),
    retrieve=extend_schema(
        summary="Get movement details",
        description="Retrieve the details of a specific stock transaction by its ID."
    ),
    # Usually, movements are immutable for audit trails, 
    # but since you have a ModelViewSet, let's document them:
    update=extend_schema(summary="Update movement record"),
    partial_update=extend_schema(summary="Partially update movement record"),
    destroy=extend_schema(summary="Delete movement record"),
)

class InventoryMovementViewSet(viewsets.ModelViewSet):
    """
    ViewSet to list, retrieve, create, update, partial_update and destroy inventory movements
    """
    queryset = InventoryMovement.objects.all()
    serializer_class = InventoryMovementSerializer

    def perform_create(self, serializer):
        # Asign the actual user that made the movement to the user field
        serializer.save(user=self.request.user)