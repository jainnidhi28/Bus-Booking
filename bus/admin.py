from django.contrib import admin
from bus.models import Bus ,BusRoute

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uuid",
        "created",
        "modified",
        "bus_number",
        "capacity",
        "bus_type",
        "bus_name",
        
        
    )
    search_fields = ("id", "bus_number", "bus_name", "bus_type", "capacity")
    list_filter = ("created", "modified")


@admin.register(BusRoute) 
class BusRouteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uuid",
        "created",
        "modified",
        "bus",
        "source",
        "destination",
        "departure_time",
        "arrival_time",
        "price",
        "date",
        
    )
    search_fields = ("id", "bus", "departure_time","arrival_time", "price", "source", "destination", "date")
    list_filter = ("created", "modified")


    
