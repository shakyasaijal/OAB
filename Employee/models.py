from django.db import models
from django.contrib.auth.models import User
from products import models as product_models

class Employee(product_models.AbstractTimeStampModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()
