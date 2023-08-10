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

class ProductOnInvoiceSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(allow_null=False)
    product_name = serializers.CharField(required=True)
    quantity = serializers.IntegerField(required=True, allow_null=False)
    price = serializers.DecimalField(max_digits=10, decimal_places=4, coerce_to_string=False)
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=4, coerce_to_string=False)
    discount = serializers.DecimalField(max_digits=10, decimal_places=4, coerce_to_string=False)
    total = serializers.DecimalField(max_digits=10, decimal_places=4, coerce_to_string=False)

class InvoiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True) 
    date = serializers.DateField(required=True)
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=4, coerce_to_string=False)
    discount = serializers.DecimalField(max_digits=10, decimal_places=4, coerce_to_string=False)
    total = serializers.DecimalField(max_digits=10, decimal_places=4, coerce_to_string=False)
    paid_with = serializers.DecimalField(max_digits=10, decimal_places=4, coerce_to_string=False)
    change = serializers.DecimalField(max_digits=10, decimal_places=4, coerce_to_string=False)
    products = ProductOnInvoiceSerializer(many=True)
