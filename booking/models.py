from django.db import models
from core.mixins import AbstractTrack
from core.models import User
from bus.models import Bus, BusRoute

class Booking(AbstractTrack):
    class Status(models.TextChoices):
        PENDING = 'PENDING'
        CONFIRMED = 'CONFIRMED'
        CANCELLED = 'CANCELLED'
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "bookings")
    bus = models.ForeignKey(Bus, on_delete= models.CASCADE,related_name="bookings")
    busroute = models.ForeignKey(BusRoute, on_delete=models.CASCADE,related_name="bookings")
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    def __str__(self):
        return f"Booking {self.id} by {self.user.first_name} {self.user.last_name} for {self.bus.bus_number}"
    
class Seat(AbstractTrack):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name = "seats")
    seat_number = models.IntegerField()
    is_cancelled = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Seat {self.seat_number} for {self.booking}"