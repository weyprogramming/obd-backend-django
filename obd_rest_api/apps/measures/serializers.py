from rest_framework import serializers

from .models import Measurement, MeasurementPoint
from apps.accounts.serializers import AccountSerializer

class MeasurementPointRaspberrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementPoint
        fields = [
            'measurement',
            'time_stamp',
            'ENGINE_LOAD',
            'RPM',
            'MAF',
            'SPEED',
            'THROTTLE_POS',
        ]

class MeasurementRaspberrySerializer(serializers.ModelSerializer):
    measurement_points = MeasurementPointRaspberrySerializer(required=False, many=True)
    class Meta:
        model = Measurement
        fields = [
            'id',
            'measurement_points',
        ]

class MeasurementSerializer(serializers.ModelSerializer):
    measurement_points = MeasurementPointRaspberrySerializer(required=False, many=True)
    account = AccountSerializer()
    class Meta:
        model = Measurement
        fields = [
            'id',
            'account',
            'measurement_points',
        ]


class MeasurementPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementPoint
        fields = [
            'measurement',
            'time_stamp',
            'ENGINE_LOAD',
            'RPM',
            'MAF',
            'SPEED',
            'THROTTLE_POS',
        ]