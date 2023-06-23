from apps.product.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class meta:
        model = Product
        fields = '__all__'
        exclude = ['id']