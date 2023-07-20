from django.db import models
from apps.base.models import BaseModel

from apps.product.models import Product

# Create your models here.
class SalesOrderHeader(BaseModel):
    date = models.DateField("Date of sale", auto_now=False, auto_now_add=True)
    subtotal = models.DecimalField("Subtotal", max_digits=10, decimal_places=4, null=False, blank=False)
    discount = models.DecimalField("Discount", max_digits=10, decimal_places=4, null=False, blank=False)
    total = models.DecimalField("Total", max_digits=10, decimal_places=4, null=False, blank=False)
    paid_with = models.DecimalField("Paid with $", max_digits=10, decimal_places=4, null=False, blank=False)
    change = models.DecimalField("Change $", max_digits=10, decimal_places=4, null=False, blank=False)
    
    # products = models.ManyToManyField(Product, through='SalesOrderDetail', verbose_name='Products', null=False, blank=False)
    
    class Meta:
        verbose_name = "Sales Order Header"
        verbose_name_plural = "Sales Order Headers"

    def __str__(self):
        return self.name
