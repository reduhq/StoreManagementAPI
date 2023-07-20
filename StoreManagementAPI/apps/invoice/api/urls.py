from django.urls import path, include 
from rest_framework import routers

from apps.invoice.api.views.invoice_views import SalesOrderHeaderView, SalesOrderDetailView

router = routers.DefaultRouter()
router.register(r"sales-order-header", SalesOrderHeaderView, 'Sales Order Header')
router.register(r"sales-order-detail", SalesOrderDetailView, "Sales Order Detail")

urlpatterns = [
    path('', include(router.urls))
]