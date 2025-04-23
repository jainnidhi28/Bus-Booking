from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from booking.models import Booking, Seat
from bus.serializers import BusSerializer, BusRouteSerializer
from core.serializers import UserSerializer


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
        
        
        

   