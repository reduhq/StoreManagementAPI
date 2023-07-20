from rest_framework import viewsets
from apps.sales_order_detail.api.serializers.sales_order_detail_serializer import SalesOrderDetailSerializer
from apps.sales_order_detail.models import SalesOrderDetail

class SalesOrderDetailView(viewsets.ModelViewSet):
    serializer_class = SalesOrderDetailSerializer
    queryset = SalesOrderDetail.objects.all()