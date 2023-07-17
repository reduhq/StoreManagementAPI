from rest_framework import viewsets

from apps.sales_order_header.api.serializers import sales_order_header_serializer
from apps.sales_order_header.models import SalesOrderHeader

class SalesOrderHeaderView(viewsets.ModelViewSet):
    serializer_class = sales_order_header_serializer
    queryset = SalesOrderHeader.objects.all()