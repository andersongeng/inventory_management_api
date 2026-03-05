from inventory.models import Product
from inventory.serializers import ProductSerializer
from rest_framework import viewsets
from django_filters import rest_framework as filters
from inventory.filters import ProductFilter
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(
        summary="List all products",
        description=(
            "Retrieve a list of products. You can use query parameters to filter "
            "results by name, category, SKU, stock "
        )
    ),
    create=extend_schema(
        summary="Register a new product",
        description=(
            "Add a new product to the inventory. The 'created_by' field is "
            "automatically set to the currently authenticated user."
        )
    ),
    retrieve=extend_schema(
        summary="Get product details",
        description="Retrieve comprehensive information about a single product using its ID."
    ),
    update=extend_schema(
        summary="Update product",
        description="Update all fields of an existing product record."
    ),
    partial_update=extend_schema(
        summary="Patch product",
        description="Update specific fields (like price or stock) without sending the full object."
    ),
    destroy=extend_schema(
        summary="Remove product",
        description="Delete a product from the system. This action cannot be undone."
    ),
)

class ProductViewSet(viewsets.ModelViewSet):
    """
    Core Product Management.
    
    This resource handles the central catalog of your inventory. It supports 
    advanced filtering and automatically tracks which user created each entry.
    """
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter

    def perform_create(self, serializer):
        # Asign the actual user that create the product to the field created_by
        serializer.save(created_by=self.request.user)