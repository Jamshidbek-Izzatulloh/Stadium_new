from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .models import UserModel,BronStadiumModel
from .serializer import UserSerializer,BronStadiumSerializer
from rest_framework import generics


class ListCreatUserView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class ListCreatBronStadiumView(generics.ListCreateAPIView):
    queryset = BronStadiumModel
    serializer_class = BronStadiumSerializer