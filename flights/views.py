from django.shortcuts import render
from django.utils import timezone
from .models import Flight

def flight_list(request):
    today = timezone.now().date()

    flights = Flight.objects.filter(date=today)

    from_search = request.GET.get("from", "")
    to_search = request.GET.get("to", "")

    if from_search:
        flights = flights.filter(departure_countrynameicontains=from_search)

    if to_search:
        flights = flights.filter(arrival_countrynameicontains=to_search)
        
    context = {
        'flights': flights,
        'from_search': from_search,
        'to_search': to_search
    }

    return render(request, "flight.html", context)
