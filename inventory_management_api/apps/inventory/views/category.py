from inventory.models import Category
from inventory.serializers import CategorySerializer
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(
        summary="List all categories",
        description="Retrieve a paginated list of all active categories in the system."
    ),
    create=extend_schema(
        summary="Create a new category",
        description="Register a new product category. The 'name' field must be unique."
    ),
    retrieve=extend_schema(
        summary="Get category details",
        description="Retrieve detailed information about a specific category by its ID."
    ),
    update=extend_schema(
        summary="Update a category",
        description="Full update of a category record."
    ),
    destroy=extend_schema(
        summary="Delete a category",
        description="Permanently remove a category from the database. Use with caution."
    ),
)

class CategoryViewSet(viewsets.ModelViewSet):
    """
    Inventory Category Management.
    
    This resource allows you to group products into logical families, 
    making it easier to filter stock and generate specialized reports.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer