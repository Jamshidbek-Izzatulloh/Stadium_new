from django.shortcuts import render
from rest_framework.views import APIView
from .models import StadiumModel, OwnerModel, BookingModel
from .serializer import StadiumModelSerializer, OwnerModelSerializer, BookingModelSerializer
from rest_framework import generics
from rest_framework import permissions
from datetime import datetime, time 

#CRUD for Stadium
class LCStadiumView(generics.ListCreateAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumModelSerializer
    permission_classes = permissions.IsAuthenticated

class RUDStadiumView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumModelSerializer
    permission_classes = permissions.IsAuthenticated

#CRUD for Broned Stadium 
class LCBronedStadiumView(generics.ListCreateAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = BookingModel
    permission_classes = permissions.IsAuthenticated

class RUDBronedStadiumView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = BookingModelSerializer
    permission_classes = permissions.IsAuthenticated

class AvailableTimesView(APIView):
    def get(self,reqeust):
        stadiums = StadiumModel.objects.all()
        timeNow = datetime.now()
        stadiums.data = []

        for stadium in stadiums:
            bron = BookingModel.objects.filter(name=stadium)
            bron_times = [BookingModel.time]