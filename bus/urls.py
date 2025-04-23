from django.urls import include, path
from rest_framework.routers import DefaultRouter

from bus.api import BusViewSet, BusRouteViewSet, get_buses_betweeen_cities


router = DefaultRouter()
router.register(r"buses", BusViewSet, basename="bus")
router.register(r"bus-routes", BusRouteViewSet, basename="bus-route")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/search-buses/", get_buses_betweeen_cities, name="search-buses"),
]
