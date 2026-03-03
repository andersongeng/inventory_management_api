from inventory.models import InventoryMovement
from inventory.serializers import InventoryMovementSerializer
from rest_framework import viewsets

class InventoryMovementViewSet(viewsets.ModelViewSet):
    """
    ViewSet to list, retrieve, create, update, partial_update and destroy inventory movements
    """
    queryset = InventoryMovement.objects.all()
    serializer_class = InventoryMovementSerializer