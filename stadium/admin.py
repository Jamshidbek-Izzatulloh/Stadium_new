from django.contrib import admin
from .models import StadiumModel, OwnerModel, BronedStadiumModel

admin.site.register(StadiumModel)
admin.site.register(OwnerModel)
admin.site.register(BronedStadiumModel)

# Register your models here.
