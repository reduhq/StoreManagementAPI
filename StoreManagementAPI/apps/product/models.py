from django.db import models
from apps.base.models import BaseModel

# Create your models here.
class Product(BaseModel):
    product_name = models.CharField("Product Name", max_length=100, blank=False, null= False, db_index=True, unique=True)
    description = models.CharField("Product Description", max_length=300)
    price = models.DecimalField("Product Price",max_digits=10, decimal_places=4, blank=False, null= False)
    quantity = models.IntegerField("Product Quantity", blank=False, null=False)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
    
    def __str__(self):
        return self.name
