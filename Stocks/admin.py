from django.contrib import admin
from django.conf import settings
from . import models


admin.site.register(models.Measure)
admin.site.register(models.Vendor)

if settings.COMPANY_TYPE == 'cafeteria':
    admin.site.register(models.Ingredients)

admin.site.register(models.Stocks)
