from django.contrib import admin
from .models import product, pedido

# Register your models here. Para poder gestionarlos en /admin

# class ProductAdmin(admin.ModelAdmin):
#     readonly_fields = {'description'}

admin.site.register(product)
admin.site.register(pedido)