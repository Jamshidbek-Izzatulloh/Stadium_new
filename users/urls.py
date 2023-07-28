from django.urls import path
from .views import(ListCreatUserView,ListCreatBronStadiumView)




urlpatterns= [
    path('user/',ListCreatUserView.as_view()),
    path('user/<pk>/',ListCreatBronStadiumView.as_view)
]