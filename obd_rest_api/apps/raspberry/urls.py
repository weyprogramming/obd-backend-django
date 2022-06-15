from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import RaspberryDefaultViewSet, RaspberryDetailViewSet, RaspberrySettingsViewSet

router = DefaultRouter()
router.register("raspberries", RaspberryDefaultViewSet, basename="raspberries")
router.register("raspberry-details", RaspberryDetailViewSet, basename="raspberries")
router.register("raspberry-settings", RaspberrySettingsViewSet, basename="raspberry-settings")

urlpatterns = [
    path('', include(router.urls)),
]