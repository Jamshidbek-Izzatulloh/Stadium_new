from django.shortcuts import render

from rest_framework.views import APIView
from .models import StadiumModel, OwnerModel, BookingModel
from .serializer import StadiumModelSerializer, OwnerModelSerializer, BookingModelSerializer
from rest_framework import generics
from rest_framework import permissions
from datetime import datetime
from rest_framework.response import Response

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
        current_datetime = datetime.now()
        stadiums_data = []

        for stadium in stadiums:
            bookings = BookingModel.objects.filter(name=stadium)
            booked_times = [booking.time_slot for booking in bookings if booking.date==current_datetime.date()]

            available_times = [
                "09:00:00",
                "10:00:00",
                "11:00:00",
                "12:00:00",
                "13:00:00",
                "14:00:00",
                "15:00:00",
                "16:00:00",
                "17:00:00",
                "18:00:00",
            ]

            available_times = [time_slot for time_slot in available_times if time_slot not in booked_times]

            stadium_data = {
                "name": StadiumModel.name,
                "location": StadiumModel.address,
                "available_times": available_times,
            }

            stadiums_data.append(stadium_data)
        return Response(stadiums_data)
