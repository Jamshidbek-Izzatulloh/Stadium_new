from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('o','Owner'),
        ('u','User'),
    )
    roles =     models.CharField(max_length=1,choices=ROLE_CHOICES)

class OwnerModel(models.Model):
    name = models.CharField(max_length=100, default='')
    lname = models.CharField(max_length=100, default='')
    date_of_birth = models.DateField(default=datetime.now)
    address = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    # photo = models.ImageField(upload_to="Owner_photo/%Y/%m/%d", blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'stadium_owner_model'


class StadiumModel(models.Model):
    name = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=500, default='')
    contact = models.CharField(max_length=30, default='')
    # photo = models.ImageField(upload_to="stadium_photo/%Y/%m/%d", blank=True)
    price1hour = models.IntegerField(default=0)
    owner = models.ForeignKey(OwnerModel, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'stadium_model'


class BronedStadiumModel(models.Model):
    from users.models import BronStadiumModel
    name = models.ForeignKey(BronStadiumModel, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'broned_stadium_model'











