from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from bus.models import Bus , BusRoute


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = [
            "id",
            "uuid",
            "bus_number",
            "capacity",
            "created",
            "modified"
        ]
        read_only_fields = ["id", "uuid", "created", "modified"]


class BusRouteSerializer(serializers.ModelSerializer):
    bus = BusSerializer(read_only=True)
    
    class Meta:
        model = BusRoute
        fields = [
            "id",
            "uuid",
            "bus",
            "source",
            "destination",
            "departure_time",
            "arrival_time",
            "price",
            "date",
            "created",
            "modified"
        ]
        read_only_fields = ["id", "uuid", "created", "modified"]
        
    def get_available_seats(self, obj):
        return obj.available_seats