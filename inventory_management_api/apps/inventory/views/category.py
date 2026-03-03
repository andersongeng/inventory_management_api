from inventory.models import Category
from inventory.serializers import CategorySerializer
from rest_framework import viewsets

class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet to list, retrieve, create, update, partial_update and destroy categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer