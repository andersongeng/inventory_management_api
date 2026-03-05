from django_filters import rest_framework as filters
from inventory.models import Product

class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    sku = filters.CharFilter(lookup_expr='iexact')
    
    # Price range
    min_price = filters.NumberFilter(
        field_name="price",
        lookup_expr='gte',
        label="Minimum price (Greater than or equal)"
    )
    max_price = filters.NumberFilter(
        field_name="price",                             
        lookup_expr='lte',
        label="Maximum price (Less than or equal)"
    )
    # Stock Range
    min_stock = filters.NumberFilter(
        field_name="stock",
        lookup_expr='gte',
        label="Minimum stock level"
    )
    max_stock = filters.NumberFilter(
        field_name="stock",
        lookup_expr='lte',
        label="Maximum stock level"
    )
    
    class Meta:
        model = Product
        fields = ['category']