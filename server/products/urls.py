from django.urls import path, include
from .apiviews import ProductsViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'products', ProductsViewSet, basename='products')


urlpatterns = router.urls