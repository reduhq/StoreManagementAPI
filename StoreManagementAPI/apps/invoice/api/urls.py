from django.urls import path, include 
from rest_framework import routers

# from apps.invoice.api.views.invoice_views import SalesOrderHeaderCreateView, SalesOrderDetailView
from apps.invoice.api.views.invoice_views import InvoiceView

router = routers.DefaultRouter()
# router.register(r"sales-order-header", SalesOrderHeaderCreateView.as_view, 'Sales Order Header')
router.register(r"invoice", InvoiceView, "Sales Order Detail")

urlpatterns = [
    # path('create-invoice/', SalesOrderHeaderCreateView.as_view()),
    path('', include(router.urls))
]