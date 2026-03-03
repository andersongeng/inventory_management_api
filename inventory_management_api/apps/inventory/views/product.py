from inventory.models import Product
from django.shortcuts import get_object_or_404
from inventory.serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet to list, retrieve, create, update, partial_update and destroy products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # Aquí le decimos: "Al guardar, inyecta el usuario actual en created_by"
        serializer.save(created_by=self.request.user)