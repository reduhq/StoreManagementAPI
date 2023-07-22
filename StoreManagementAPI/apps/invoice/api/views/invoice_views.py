from rest_framework import viewsets
from rest_framework import generics
from apps.invoice.api.serializers.invoice_serializers import SalesOrderDetailSerializer, SalesOrderHeaderCreateSerializer
from apps.invoice.models import SalesOrderHeader, SalesOrderDetail

# class SalesOrderHeaderView(viewsets.ModelViewSet):
#     serializer_class = SalesOrderHeaderSerializer
#     queryset = SalesOrderHeader.objects.all()

class SalesOrderHeaderCreateView(generics.CreateAPIView):
    serializer_class = SalesOrderHeaderCreateSerializer
    queryset = None #Se le puede pasar None? (Preuntar a chatgpt)

class SalesOrderDetailView(viewsets.ModelViewSet):
    serializer_class = SalesOrderDetailSerializer
    queryset = SalesOrderDetail.objects.all()

