from inventory.models import InventoryMovement
from inventory.serializers import InventoryMovementSerializer
from rest_framework import viewsets

class InventoryMovementViewSet(viewsets.ModelViewSet):
    """
    ViewSet to list, retrieve, create, update, partial_update and destroy inventory movements
    """
    queryset = InventoryMovement.objects.all()
    serializer_class = InventoryMovementSerializer

    def perform_create(self, serializer):
        # Aquí asignamos al usuario logueado al campo que definiste en tu modelo
        # Si en tu modelo el campo se llama 'user', usa user=self.request.user
        serializer.save(user=self.request.user)