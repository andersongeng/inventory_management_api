from django.contrib import admin

# Register your models here.
from inventory.models import Category, Product, InventoryMovement

from django.contrib import admin
from .models import Category, Product, InventoryMovement

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'price', 'stock', 'active')
    list_filter = ('category', 'active')
    search_fields = ('name', 'sku')

@admin.register(InventoryMovement)
class InventoryMovementAdmin(admin.ModelAdmin):
    list_display = ('date', 'product', 'type', 'quantity', 'user')
    list_filter = ('type', 'date')