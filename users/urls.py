from django.urls import path
from .views import(LCUserView,RUDUserView)

urlpatterns= [
    path('user/',LCUserView.as_view()),
    path('user/<pk>/', RUDUserView.as_view()),
]