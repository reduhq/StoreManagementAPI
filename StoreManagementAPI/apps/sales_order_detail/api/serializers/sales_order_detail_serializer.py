from rest_framework import serializers
from apps.sales_order_detail.models import SalesOrderDetail

class SalesOrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrderDetail
        fields = '__all__'