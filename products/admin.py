from django.contrib import admin
from . import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name', 'price']
    list_per_page = 25


admin.site.register(models.Products, ProductAdmin)
admin.site.register(models.Category)