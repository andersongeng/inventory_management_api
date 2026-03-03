from rest_framework import serializers
from inventory.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # Definimos los campos que queremos exponer en nuestra API
        fields = ['id', 'name']
        
    # Ejemplo de validación personalizada:
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El nombre de la categoría es muy corto.")
        return value