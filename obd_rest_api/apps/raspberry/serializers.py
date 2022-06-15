from rest_framework import serializers

from .models import Raspberry, RaspberrySettings

from apps.accounts.serializers import AccountSerializer

class RaspberrySettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaspberrySettings
        fields = '__all__'
        extra_fields = ['raspberries']

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(RaspberrySettingsSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields

class RaspberryDetailSerializer(serializers.ModelSerializer):
    used_by = AccountSerializer(read_only=True)
    raspberry_account = AccountSerializer(read_only=True)
    created_by = AccountSerializer(read_only=True)
    updated_by = AccountSerializer(read_only=True)
    settings = RaspberrySettingsSerializer(read_only=True)

    class Meta:
        model = Raspberry
        fields = '__all__'

class RaspberryDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raspberry
        fields = '__all__'