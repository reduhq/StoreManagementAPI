from rest_framework import viewsets

from apps.product.api.serializers import product_serializer
from apps.product.models import Product

class ProductView(viewsets.ModelViewSet):
    serializer_class = product_serializer
    queryset = Product.objects.all()