from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .api import BookingViewSet, SeatViewSet, cancel_seat, cancel_booking, book_seat, list_bookings, get_available_seats

router = DefaultRouter()
router.register(r"bookings", BookingViewSet,  basename="booking")
router.register(r"seats", SeatViewSet , basename = "seat")

urlpatterns = [
    path("", include(router.urls)),
    path('bookings/<uuid:booking_uuid>/cancel-seat/', cancel_seat, name='cancel-seat'),
    path('bookings/<uuid:booking_uuid>/cancel/', cancel_booking),
    path("bookings/<uuid:booking_uuid>/book-seat/", book_seat, name="book-seat"),
    path('bookings/busroute/<uuid:busroute_uuid>/', list_bookings),
    path("available-seats/", get_available_seats, name="available-seats"),
]
