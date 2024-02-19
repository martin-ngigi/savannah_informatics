from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

# urls.py
from django.urls import path
from .views import OrderViewSet

router = DefaultRouter()
router.register(r'all', OrderViewSet, basename='my_orders')

# urlpatterns = [
#     path('', include(router.urls)),
# ]
urlpatterns = router.urls