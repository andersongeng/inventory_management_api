from inventory.models import Category
from inventory.serializers import CategorySerializer
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(description="Get a list of all categories."),
    create=extend_schema(description="Create a new category. Name must be unique."),
    retrieve=extend_schema(description="Get the detail of an specific category."),
)

class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet to list, retrieve, create, update, partial_update and destroy categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer