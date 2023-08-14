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
        
class SalesOrderDetailOutSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='product.id')
    product_name = serializers.CharField(source='product.product_name')

    class Meta:
        model = SalesOrderDetail
        fields = (
            'product_id',
            'product_name',
            'price',
            'quantity',
            'subtotal',
            'discount',
            'total',
        )

class SalesOrderHeaderOutSerializer(serializers.ModelSerializer):
    products = SalesOrderDetailOutSerializer(source='salesorderdetail_set', many=True)

    class Meta:
        model = SalesOrderHeader
        fields = (
            'id',
            'date',
            'subtotal',
            'discount',
            'total',
            'paid_with',
            'change',
            'products'
        )

