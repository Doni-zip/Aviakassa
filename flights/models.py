from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    flag_url = models.URLField()

    def str(self):
        return self.name


class Flight(models.Model):
    date = models.DateField()
    departure_country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="departures"
    )
    arrival_country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="arrivals"
    )

    def str(self):
        return f"{self.departure_country} → {self.arrival_country} ({self.date})"
