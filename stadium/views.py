from django.shortcuts import render
from .models import StadiumModel, OwnerModel, BronedStadiumModel
from .serializer import StadiumModelSerializer, OwnerModelSerializer, BronedStadiumModelSerializer
from rest_framework import generics

#CRUD for Stadium
class LCStadiumView(generics.ListCreateAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumModelSerializer

class RUDStadiumView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumModelSerializer

#CRUD for BronedStadiumModel
class LCBronedStadiumView(generics.ListCreateAPIView):
    queryset = BronedStadiumModel.objects.all()
    serializer_class = BronedStadiumModelSerializer

class RUDBronedStadiumView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BronedStadiumModel.objects.all()
    serializer_class = BronedStadiumModelSerializer


