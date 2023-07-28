from django.shortcuts import render
from rest_framework.views import APIView
from .models import StadiumModel, OwnerModel, BronedStadiumModel
from .serializer import StadiumModelSerializer, OwnerModelSerializer, BronedStadiumModelSerializer
from rest_framework import generics
from rest_framework import permissions

#CRUD for Stadium
class LCStadiumView(generics.ListCreateAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumModelSerializer
    permission_classes = permissions.IsAuthenticated

class RUDStadiumView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumModelSerializer
    permission_classes = permissions.IsAuthenticated

#CRUD for BronedStadiumModel
class LCBronedStadiumView(generics.ListCreateAPIView):
    queryset = BronedStadiumModel.objects.all()
    serializer_class = BronedStadiumModelSerializer
    permission_classes = permissions.IsAuthenticated

class RUDBronedStadiumView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BronedStadiumModel.objects.all()
    serializer_class = BronedStadiumModelSerializer
    permission_classes = permissions.IsAuthenticated

