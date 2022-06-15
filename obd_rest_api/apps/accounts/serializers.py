from rest_framework.serializers import ModelSerializer
# from apps.measures.serializers import MeasurementSerializer

from .models import Car, Account
from apps.raspberry.models import Raspberry

class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'manufacturer',
            'model_name',
            'construction_year',
            'fuel_type',
            'mass_kg',
            'engine_displacement_l',
            'number_of_cylinders',
            'milage_km',
            'power_ps',
        ]

class AccountSerializer(ModelSerializer):
    car = CarSerializer(required=False)

    class Meta:
        model = Account
        fields = [
            'first_name',
            'last_name',
            'date_of_birth',
            'driving_license_since',
            'gender',
            'car',
            'used_raspberries'
        ]