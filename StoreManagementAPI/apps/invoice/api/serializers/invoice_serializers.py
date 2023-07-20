from rest_framework import serializers
from apps.invoice.models import SalesOrderHeader, SalesOrderDetail

class SalesOrderHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrderHeader
        fields = '__all__'


class SalesOrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrderDetail
        fields = '__all__'
