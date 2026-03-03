from inventory.models import Product
from inventory.serializers import ProductSerializer
from rest_framework import viewsets
from django_filters import rest_framework as filters
from inventory.filters import ProductFilter

class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet to list, retrieve, create, update, partial_update and destroy products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter

    def perform_create(self, serializer):
        # Aquí le decimos: "Al guardar, inyecta el usuario actual en created_by"
        serializer.save(created_by=self.request.user)