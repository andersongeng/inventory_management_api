# apps/inventory/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
# Importamos el modelo desde tu estructura de carpeta
from inventory.models import InventoryMovement 

@receiver(post_save, sender=InventoryMovement)
def update_stock_on_movement(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        if instance.type == 'IN':
            product.stock += instance.quantity
        elif instance.type == 'OUT':
            product.stock -= instance.quantity
        
        # Usamos update_fields para que SOLO se guarde el stock
        # Esto evita disparar validaciones de otros campos en el save()
        product.save(update_fields=['stock'])