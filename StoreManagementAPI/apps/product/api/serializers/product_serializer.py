from apps.product.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'price': {
                'coerce_to_string': False,
                'min_value': 0
            }
        }