from rest_framework import serializers
from apps.invoice.models import SalesOrderHeader, SalesOrderDetail

from apps.product.api.serializers.product_serializer import ProductSerializer

# class SalesOrderHeaderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SalesOrderHeader
#         fields = '__all__'

class SalesOrderSerializer(serializers.Serializer):
    id_product = serializers.IntegerField(required=True)
    product_price = serializers.DecimalField(max_digits=10, decimal_places=4)
    quantity = serializers.IntegerField()

class SalesOrderHeaderCreateSerializer(serializers.ModelSerializer):
    sales_data = SalesSerializer(many=True)
    class Meta:    
        model = SalesOrderHeader
        fields = ('sales_data', 'paid_with', )


class SalesOrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrderDetail
        fields = '__all__'

