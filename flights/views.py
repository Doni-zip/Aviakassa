from django.shortcuts import render
from .models import Flight, Country

def flights_page(request):

    flights_list = Flight.objects.all()
    country_list = Country.objects.all()
    context = {
        'flights_list': flights_list,
        'country_list': country_list
    }

    return render(request, "flights.html", context)
