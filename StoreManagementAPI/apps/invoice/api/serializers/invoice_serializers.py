from rest_framework import serializers
from apps.invoice.models import SalesOrderHeader, SalesOrderDetail

from apps.product.api.serializers.product_serializer import ProductSerializer

# class SalesOrderHeaderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SalesOrderHeader
#         fields = '__all__'

class SalesSerializer(serializers.Serializer):
    id_product = serializers.IntegerField(required=True)
    product_price = serializers.DecimalField(max_digits=10, decimal_places=4, coerce_to_string=False)
    quantity = serializers.IntegerField()

class SalesOrderSerializer(serializers.Serializer):
    sales_data = SalesSerializer(many=True)
    paid_with = serializers.DecimalField(max_digits=10, decimal_places=4,coerce_to_string=False)

class SalesOrderHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrderHeader
        fields = '__all__'

class SalesOrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrderDetail
        fields = '__all__'

