from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, EntryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'entries', EntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]