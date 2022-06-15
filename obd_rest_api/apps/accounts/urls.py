from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CarViewSet, AccountViewSet

router = DefaultRouter()
router.register("cars", CarViewSet, basename="cars")
router.register("accounts", AccountViewSet, basename="accounts")

urlpatterns = [
    path('', include(router.urls)),
]