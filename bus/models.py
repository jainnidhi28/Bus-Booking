from django.db import models
from core.mixins import AbstractTrack
from django.apps import apps


class Bus(AbstractTrack):
    class Types(models.TextChoices):
        AC = 'AC'
        NON_AC = 'NON_AC'
        SLEEPER = 'SLEEPER'
        SEMI_SLEEPER = 'SEMI_SLEEPER'
    bus_number = models.CharField(max_length=20, unique=True)
    bus_name = models.CharField(max_length=100, null=True, blank=True)
    capacity = models.IntegerField()
    bus_type = models.CharField(
        max_length=20,
        choices=Types.choices,
        default=Types.AC,
    )
    def __str__(self):
        return f"Bus {self.bus_number}"
    
class BusRoute(AbstractTrack):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='routes')
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    def __str__(self):
        return f"Route from {self.source} to {self.destination} for Bus {self.bus.bus_number}"
    
    @property
    def available_seats(self):
        from booking.models import Seat
        booked_seats = Seat.objects.filter(
            booking__busroute=self,
            is_cancelled=False
        ).values_list('seat_number', flat=True)
        all_seats = set(range(1, self.bus.capacity + 1))
        available_seats = sorted(list(all_seats - set(booked_seats)))
        return {
            "total_capacity": self.bus.capacity,
            "booked_seats": list(booked_seats),
            "available_seats": available_seats,
            "available_seats_count": len(available_seats)
        }