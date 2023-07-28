from django.shortcuts import render
from .models import StadiumModel, OwnerModel, BronedStadiumModel
from .serializer import StadiumModelSerializer, OwnerModelSerializer, BronedStadiumModelSerializer
from rest_framework import generics

#CRUD for Stadium
class ListCreateStadiumView(generics.ListCreateAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumModelSerializer

class RetrieveUpdateDestroyStadiumView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumModelSerializer


