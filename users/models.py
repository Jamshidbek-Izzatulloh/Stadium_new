from django.db import models
from datetime import datetime

class UserModel(models.Model):
    name = models.CharField(max_length=100, default='')
    lname = models.CharField(max_length=100, default='')
    date_of_birth = models.DateField(default=datetime.now)
    address = models.CharField(max_length=150)
    contact = models.CharField(max_length=30, default='')
    email = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="User_photo/%Y/%m/%d", blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'user_model'

class BronStadiumModel(models.Model):
    from stadium.models import StadiumModel
    name = models.ForeignKey(StadiumModel, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=datetime.now)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'bron_stadium_model'
