from rest_framework import serializers
from inventory.models import Product

class ProductSerializer(serializers.ModelSerializer):
    # Campos adicionales para mejorar la lectura (Read Only)
    category_name = serializers.ReadOnlyField(source='category.name')
    created_by_name = serializers.ReadOnlyField(source='created_by.username')
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'sku', 'description', 
            'category', 'category_name', 'price', 
            'stock', 'created_by', 'created_by_name',
            'created_at', 'last_update', 'active'
        ]
        # Estos campos no se pueden modificar vía API manualmente
        read_only_fields = [
            'id', 'stock', 'created_by', 
            'created_at', 'last_update'
        ]

    # Validación personalizada para el SKU
    def validate_sku(self, value):
        if not value:
            return value
        
        if not value.isalnum():
            raise serializers.ValidationError("El SKU solo debe contener letras y números.")
        return value.upper()
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser un número positivo mayor a cero.")
        return value