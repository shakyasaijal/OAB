from django.db import models
from django.conf import settings


class AbstractTimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.created_at

    class Meta:
        abstract = True


class Category(AbstractTimeStampModel):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='categories')

    def __str__(self):
        return self.name


class Products(AbstractTimeStampModel):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    price = models.FloatField(null=False, blank=False)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    
    category = models.ManyToManyField(Category, blank=True)

    if settings.COMPANY_TYPE == 'cafeteria':
        product_includes = models.ManyToManyField("Stocks.Ingredients", blank=True)

    def __str__(self):
        return self.name
