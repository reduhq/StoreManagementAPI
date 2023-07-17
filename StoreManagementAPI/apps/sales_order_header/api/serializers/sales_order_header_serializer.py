from rest_framework import serializers 
from apps.sales_order_header.models import SalesOrderHeader

class SalesOrderHeaderSerializer(serializers.ModelSerializer):
    class meta:
        model = SalesOrderHeader
        fields = '__all__'