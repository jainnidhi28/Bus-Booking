from django.contrib import admin
from booking.models import Booking, Seat

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uuid",
        "created",
        "modified",
        "user",
        "bus",
        'status',
        "busroute"
    )
    search_fields = ("id", "user", "bus", "busroute", "status")
    list_filter = ("created", "modified")


    
@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uuid",
        "created",
        "modified",
        "booking",
        "seat_number",
        "is_cancelled",   
    )
    search_fields = ("id", "booking", "seat_number", "is_cancelled")
    list_filter = ("created", "modified")


    