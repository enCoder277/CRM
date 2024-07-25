from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganizationViewSet, ContactViewSet, DealViewSet

router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'deals', DealViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
