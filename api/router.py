from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ProductViewSet, PriceViewSet

router = DefaultRouter()

router.register(r'products', ProductViewSet)
router.register(r'products/(?P<product_id>\d+)/prices', PriceViewSet, basename='price')
urlpatterns = router.urls