from rest_framework import serializers
from inventory.models import InventoryMovement

class InventoryMovementSerializer(serializers.ModelSerializer):
    # Campos de lectura para que el JSON sea amigable
    product_name = serializers.ReadOnlyField(source='product.name')
    user_username = serializers.ReadOnlyField(source='user.username')
    type_label = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = InventoryMovement
        fields = [
            'id', 'product', 'product_name', 'user', 'user_username',
            'type', 'type_label', 'quantity', 'date', 'comment'
        ]
        read_only_fields = ['id', 'user', 'date']

    def validate(self, data):
        """
        Validación integral: No permitir salidas si no hay stock suficiente.
        """
        product = data.get('product')
        movement_type = data.get('type')
        quantity = data.get('quantity')

        if movement_type == InventoryMovement.MovementType.OUTBOUND:
            if product.stock < quantity:
                raise serializers.ValidationError({
                    "quantity": f"Stock insuficiente. Disponible: {product.stock}, solicitado: {quantity}"
                })
        
        return data