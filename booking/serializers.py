from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from booking.models import Booking, Seat
from bus.serializers import BusSerializer, BusRouteSerializer
from core.serializers import UserSerializer
from .models import BusRoute



class SeatSerializer(serializers.ModelSerializer):
    source = serializers.CharField(source='booking.busroute.source', read_only=True)
    destination = serializers.CharField(source='booking.busroute.destination', read_only=True)
    date = serializers.DateField(source='booking.busroute.date', read_only=True)
    booking = serializers.UUIDField(source='booking.uuid', read_only=True)

    class Meta:
        model = Seat
        fields = [
            "uuid",
            "booking",
            "seat_number",
            "source",
            "destination",
            "date",
            "is_cancelled",
        ]
        read_only_fields = ["uuid", "booking", "source", "destination", "date", "is_cancelled"]


    
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['uuid', 'status', 'created', 'status']

        read_only_fields = ["id", "uuid", "created", "modified"]
        
   
   
class AvailableSeatsSerializer(serializers.ModelSerializer):
    bus_route = serializers.SerializerMethodField()
    total_capacity = serializers.SerializerMethodField()
    booked_seats = serializers.SerializerMethodField()
    available_seats = serializers.SerializerMethodField()
    available_seats_count = serializers.SerializerMethodField()

    class Meta:
        model = BusRoute
        fields = [
            'uuid',
            'bus_route',
            'date',
            'total_capacity',
            'booked_seats',
            'available_seats',
            'available_seats_count'
        ]

    def get_bus_route(self, obj):
        return f"{obj.source} to {obj.destination}"

    def get_total_capacity(self, obj):
        return obj.available_seats["total_capacity"]

    def get_booked_seats(self, obj):
        return obj.available_seats["booked_seats"]

    def get_available_seats(self, obj):
        return obj.available_seats["available_seats"]

    def get_available_seats_count(self, obj):
        return obj.available_seats["available_seats_count"]     
