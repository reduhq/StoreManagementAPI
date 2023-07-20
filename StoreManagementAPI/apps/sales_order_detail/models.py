from django.db import models
from apps.base.models import BaseModel
from apps.product.models import Product
from apps.sales_order_header.models import SalesOrderHeader

# Create your models here.
class SalesOrderDetail(BaseModel):
    id_sales_order_header = models.ForeignKey(SalesOrderHeader, on_delete=models.CASCADE, verbose_name="Sales Order Header", null=False, blank=False)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product", null=False, blank=False)
    price = models.DecimalField("Price", max_digits=10, decimal_places=4, null=False, blank=False)
    quantity = models.IntegerField("Quantity", null=False, blank=False)
    discount = models.DecimalField("Discount", max_digits=10, decimal_places=4, null=False, blank=False)
    
    class Meta: 
        verbose_name = "Sales Order Detail"
        verbose_name_plural = "Sales Order Details"