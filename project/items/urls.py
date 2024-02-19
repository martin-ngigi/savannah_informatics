from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

# urls.py
from django.urls import path
from .views import ItemViewSet


# urlpatterns = [
#     path('all/', ItemViewSet.as_view({'get': 'list'}), name='all_items'),
# ]

router = DefaultRouter()
router.register(r'all', ItemViewSet, basename='my_items')

# urlpatterns = [
#     path('', include(router.urls)),
# ]
# or
urlpatterns = router.urls
