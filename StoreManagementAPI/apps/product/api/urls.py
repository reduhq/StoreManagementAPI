from django.urls import path, include
from rest_framework import routers

from apps.product.api.views.product_view import ProductView

router = routers.DefaultRouter()
router.register(r"product", ProductView, 'Product')

urlpatterns = [
    path('',include(router.urls))
]
