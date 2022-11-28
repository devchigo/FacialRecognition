from django.urls import path
from . import views

urlpatterns = [
    path('citizen', views.citizenList, name='citizen'),
]