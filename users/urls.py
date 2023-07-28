from django.urls import path
from .views import(LCUserView,LCBronStadiumView)




urlpatterns= [
    path('user/',LCUserView.as_view()),
    path('user/<pk>/',LCBronStadiumView.as_view)
]