from rest_framework import viewsets

from apps.sales_order_header.api.serializers.sales_order_header_serializer import SalesOrderHeaderSerializer
from apps.sales_order_header.models import SalesOrderHeader

class SalesOrderHeaderView(viewsets.ModelViewSet):
    serializer_class = SalesOrderHeaderSerializer
    queryset = SalesOrderHeader.objects.all()