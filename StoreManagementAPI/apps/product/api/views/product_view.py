from rest_framework import viewsets

from apps.product.api.serializers.product_serializer import ProductSerializer
from apps.product.models import Product

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()