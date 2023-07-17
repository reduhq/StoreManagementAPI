from django.urls import path, include 
from rest_framework import routers

from apps.sales_order_header.api.views.sales_order_header_view import SalesOrderHeaderView

router = routers.DefaultRouter()
router.register(r"", SalesOrderHeaderView, 'Sales Order Header')

urlpatterns = [
    path('sales-order-header/', include(router.urls))
]
