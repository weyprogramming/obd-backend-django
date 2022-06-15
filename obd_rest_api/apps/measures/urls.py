from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import MeasurementViewSet, MeasurementPointViewSet, MeasurementRaspberryViewset, MeasurementPointRaspberryViewset

router = DefaultRouter()
router.register("measurements", MeasurementViewSet, basename="measurements")
router.register("measurementpoints", MeasurementPointViewSet, basename="measurementpoints")

urlpatterns = [
    path('', include(router.urls)),
    path('post/measurements/raspberry/', MeasurementRaspberryViewset.as_view()),
    path('post/measurementpoints/raspberry/', MeasurementPointRaspberryViewset.as_view()),
]
