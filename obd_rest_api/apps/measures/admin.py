from django.contrib import admin

from .models import Measurement, MeasurementPoint

admin.site.register(Measurement)
admin.site.register(MeasurementPoint)

