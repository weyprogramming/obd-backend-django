from django.shortcuts import render

from apps.measures.models import Measurement, MeasurementPoint
from .serializers import MeasurementSerializer, MeasurementPointSerializer, MeasurementRaspberrySerializer, MeasurementPointRaspberrySerializer
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

class MeasurementViewSet(viewsets.ModelViewSet):
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()
    permission_classes = [AllowAny]


class MeasurementPointViewSet(viewsets.ModelViewSet):
    serializer_class = MeasurementPointSerializer
    queryset = MeasurementPoint.objects.all()
    permission_classes = [IsAdminUser]

class MeasurementRaspberryViewset(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = MeasurementRaspberrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(account=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MeasurementPointRaspberryViewset(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = MeasurementPointRaspberrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

