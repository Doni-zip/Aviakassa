from django.urls import path
from .views import flight_list

urlpatterns = [
    path("", flight_list, name="flight_list"),
]