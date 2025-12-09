from django.urls import path
from .views import flights_page

urlpatterns = [
    path("", flights_page),
]