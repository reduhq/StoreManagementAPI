from rest_framework import routers
from django.urls import path, include

from apps.sales_order_detail.api.views.sales_order_detail_view import SalesOrderDetailView

router = routers.DefaultRouter()
router.register(r"sales-order-detail", SalesOrderDetailView, "Sales Order Detail")

urlpatterns = [
    path('', include(router.urls))
]
