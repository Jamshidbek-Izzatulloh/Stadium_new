from django.contrib import admin

from .models import StadiumModel, OwnerModel, BookingModel

admin.site.register(StadiumModel)
admin.site.register(OwnerModel)
admin.site.register(BookingModel)


