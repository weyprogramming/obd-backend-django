from django.shortcuts import render

from .models import Account, Car
from .serializers import AccountSerializer, CarSerializer
from rest_framework import viewsets

class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()    
