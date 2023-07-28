from django.urls import path
from .views import (LCStadiumView, RUDStadiumView,
                    LCBronedStadiumView, RUDBronedStadiumView)

urlpatterns = [
    #stadium urls
    path('stadium/', LCStadiumView.as_view()),
    path('stadium/<pk>/', RUDStadiumView.as_view()),
    #broned urls
    path('broned/', LCBronedStadiumView.as_view()),
    path('broned/<pk>', RUDBronedStadiumView.as_view()),
]