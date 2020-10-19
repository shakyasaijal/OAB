from django.db import models
from products import models as product_models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Table(product_models.AbstractTimeStampModel):
    table_number = models.CharField(max_length=255, null=False, blank=False, unique=True)
    floor = models.CharField(max_length=255, null=True, blank=True)
    descibe = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.floor:
            return "Table: {} --> Floor: {}".format(self.table_number, self.floor)
        else:
            return "Table: {}".format(self.table_number)

    class Meta:
        ordering = ['table_number']
        verbose_name = "Table"
        verbose_name_plural = "Tables"


class Discounts(product_models.AbstractTimeStampModel):
    discount_type_choices = (
        ("1", "In Price"),
        ("2", "In Percantage"),
    )
    discount_for_choice = (
        ("1", "Category"),
        ("2", "Products"),
        ("3", "For All"),
    )
    discount_type = models.CharField(max_length=50, null=False, blank=False, choices=discount_type_choices)
    discount_for = models.CharField(max_length=50, null=False, blank=False, choices=discount_for_choice)

    categories = models.ManyToManyField(product_models.Category)
    products = models.ManyToManyField(product_models.Products)


    def __str__(self):
        return self.discount_type


class ServiceCharge(SingletonModel, product_models.AbstractTimeStampModel):
    charge = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.charge


class OrderItems(product_models.AbstractTimeStampModel):
    order_type_choices = (
        ("1", "On Table"),
        ("2", "Packing"),
        ("3", "Deliver"),
    )
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(product_models.Products, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.FloatField(null=False, blank=False)
    order_type = models.CharField(max_length=50, null=False, blank=False, default="1", choices=order_type_choices)

    def __str__(self):
        return "{} --> {}".format(self.product.name, self.product.quantity)


class Orders(product_models.AbstractTimeStampModel):

    order_status_choices = (
        ("1", "On Process"),
        ("2", "Paid"),
    )

    products = models.ManyToManyField(OrderItems, blank=False)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True, blank=True)
    order_status = models.CharField(max_length=50, null=False, blank=False, default="1", choices=order_status_choices)
    total = models.FloatField(null=False, blank=False)
    discount = models.ForeignKey(Discounts, on_delete=models.DO_NOTHING, null=True, blank=True)
    service_charge = models.ForeignKey(ServiceCharge, on_delete=models.DO_NOTHING, null=True, blank=True)
    grand_total = models.FloatField(null=False, blank=False)

    def __str__(self):
        return "{} --> {}".format(self.table.table_number, self.order_status)

