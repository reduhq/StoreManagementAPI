from rest_framework import viewsets
from apps.invoice.api.serializers.invoice_serializers import SalesOrderHeaderSerializer, SalesOrderDetailSerializer
from apps.invoice.models import SalesOrderHeader, SalesOrderDetail

class SalesOrderDetailView(viewsets.ModelViewSet):
    serializer_class = SalesOrderDetailSerializer
    queryset = SalesOrderDetail.objects.all()


class SalesOrderHeaderView(viewsets.ModelViewSet):
    serializer_class = SalesOrderHeaderSerializer
    queryset = SalesOrderHeader.objects.all()