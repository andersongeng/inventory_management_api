from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.functions import Now
from .product import Product
from django.conf import settings

class InventoryMovement(models.Model):
    class MovementType(models.TextChoices):
        INBOUND = "IN", _("Inbound")
        OUTBOUND = "OUT", _("Outbound")

    product = models.ForeignKey(
        Product, 
        on_delete=models.PROTECT, 
        related_name='movements'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='inventory_actions'
    )
    type = models.CharField(max_length=3, choices=MovementType.choices, default=MovementType.INBOUND)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.type} - {self.product.name} ({self.quantity})"