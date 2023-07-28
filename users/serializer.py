from rest_framework import serializers
from .models import (UserModel,BronStadiumModel)

from django.shortcuts import get_object_or_404



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

class BronStadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = BronStadiumModel
        fields = '__all__'


