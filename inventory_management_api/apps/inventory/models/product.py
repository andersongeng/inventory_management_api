from django.db import models
from django.conf import settings
from .category import Category
from django.core.validators import MinValueValidator
from decimal import Decimal


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    sku = models.CharField(max_length=50, unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='products'
    )
    price = models.DecimalField(max_digits=16, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    stock = models.PositiveIntegerField(db_default=0)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        related_name='created_products'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, db_default=True)

    def __str__(self):
        return f"{self.name} ({self.sku})"
    
    def save(self, *args, **kwargs):
        if self.pk:  # Si el producto ya existe (estamos editando)
            # Obtenemos el valor que está grabado en el disco
            original_stock = Product.objects.get(pk=self.pk).stock
            if self.stock != original_stock:
                # Si alguien intentó cambiar el stock a mano, lanzamos error
                raise ValueError("El stock solo puede modificarse mediante movimientos de inventario.")
        super().save(*args, **kwargs)