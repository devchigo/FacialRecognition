from django.urls import path
from . import views
from .views import CriminalList, CriminalDetail, CriminalCreate, CriminalUpdate

urlpatterns = [
    # path('criminal', views.criminal_list, name='criminal_list'),
    path('criminal', CriminalList.as_view(), name="criminal_list" ),
    path('criminal_detail/<int:pk>', CriminalDetail.as_view(), name="criminal_detail"),
    path('criminal_create/', CriminalCreate.as_view(), name="criminal_create"),
    path('criminal_update/<int:pk>', CriminalUpdate.as_view(), name="criminal_update"),
]