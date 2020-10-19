from django.contrib import admin
from . import models

admin.site.register(models.Discounts)
admin.site.register(models.OrderItems)
admin.site.register(models.Orders)
admin.site.register(models.ServiceCharge)
admin.site.register(models.Table)
