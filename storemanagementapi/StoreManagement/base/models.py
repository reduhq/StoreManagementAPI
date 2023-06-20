from django.db import models

# Create your models here.
class BaseModel(models.Model):

    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True
        verbose_name = ("Base Model")
