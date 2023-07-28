from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .models import UserModel,BronStadiumModel
from .serializer import UserSerializer,BronStadiumSerializer
from rest_framework import generics
from rest_framework import permissions
from config.permissions import OwnerPermission

class LCUserView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = permissions.IsAuthenticated
    
class RUDUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = permissions.IsAuthenticated

class LCBronStadiumView(generics.ListCreateAPIView):
    queryset = BronStadiumModel
    serializer_class = BronStadiumSerializer
    permission_classes = permissions.IsAuthenticated

class RUDBronStadiumView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BronStadiumModel
    serializer_class = BronStadiumSerializer
    permission_classes = permissions.IsAuthenticated