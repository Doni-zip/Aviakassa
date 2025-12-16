from django.urls import path
from .views import *

urlpatterns = [
    path("", flights_page, name='flights_page'),
    path("register/", register_view, name='register'),
    path("login/", login_view, name='login'),  
    path("logout/", logout_view, name='logout'),  
]