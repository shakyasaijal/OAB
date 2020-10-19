from django.db import models
from django.conf import settings
from products import models as product_models


class Measure(product_models.AbstractTimeStampModel):
    measuring = models.CharField(max_length=50, null=False, blank=False, unique=True)

    def __str__(self):
        return self.measuring


class Vendor(product_models.AbstractTimeStampModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


if settings.COMPANY_TYPE == 'cafeteria':
    class Ingredients(product_models.AbstractTimeStampModel):
        name = models.CharField(max_length=255, null=False, blank=False, unique=True)

        def __str__(self):
            return self.name


    class Stocks(product_models.AbstractTimeStampModel):
        ingredients = models.OneToOneField(Ingredients, null=False, blank=False, on_delete=models.CASCADE)
        stock = models.FloatField(null=False, blank=False)
        measure_in = models.ForeignKey(Measure, on_delete=models.PROTECT, null=False, blank=False)
        vendor = models.ForeignKey(Vendor, null=True, blank=True, on_delete=models.PROTECT)

        def __str__(self):
            return "{} --> {} {}".format(self.ingredients.name, self.stock, self.measure_in)
        

if settings.COMPANY_TYPE == 'medicine' or settings.COMPANY_TYPE == 'grocery':
    class Stocks(product_models.AbstractTimeStampModel):
        product = models.OneToOneField(product_models.Products, on_delete=models.CASCADE, null=False, blank=False)
        quantity = models.FloatField(null=False, blank=False)
        measured_in = models.ForeignKey(Measure, on_delete=models.PROTECT, null=False, blank=False)
        vendor = models.ForeignKey(Vendor, null=True, blank=True, on_delete=models.PROTECT)

        def __str__(self):
            return self.product.name
        

if settings.COMPANY_TYPE == 'tailor':
    class Stocks(product_models.AbstractTimeStampModel):
        name = models.CharField(max_length=255, null=False, blank=False, unique=True)
        quantity = models.FloatField(null=False, blank=False)
        measured_in = models.ForeignKey(Measure, on_delete=models.PROTECT, null=False, blank=False)
        vendor = models.ForeignKey(Vendor, null=True, blank=True, on_delete=models.PROTECT)

        def __str__(self):
            return self.name
        