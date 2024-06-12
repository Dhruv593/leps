from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prediction', views.prediction, name='prediction'),
    path('result', views.result, name='result'),
    path('team', views.team, name='team'),
]