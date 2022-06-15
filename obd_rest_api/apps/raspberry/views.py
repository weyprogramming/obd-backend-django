from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from .serializers import RaspberryDefaultSerializer, RaspberryDetailSerializer, RaspberrySettingsSerializer
from .models import Raspberry, RaspberrySettings

class RaspberryDefaultViewSet(viewsets.ModelViewSet):
    serializer_class = RaspberryDefaultSerializer
    queryset = Raspberry.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset.all()
        else:
            return self.queryset.filter(used_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user, updated_by = self.request.user)

class RaspberryDetailViewSet(viewsets.ModelViewSet):
    serializer_class = RaspberryDetailSerializer
    queryset = Raspberry.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset.all()
        else:
            return self.queryset.filter(used_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user, updated_by = self.request.user)


class RaspberrySettingsViewSet(viewsets.ModelViewSet):
    serializer_class = RaspberrySettingsSerializer
    queryset = RaspberrySettings.objects.all()
    permission_classes = [AllowAny]
