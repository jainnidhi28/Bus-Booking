from rest_framework import viewsets
from .models import Booking, Seat, BusRoute
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import BookingSerializer, SeatSerializer
from datetime import datetime
from django.shortcuts import get_object_or_404

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().select_related(
        'user', 'bus', 'busroute'
    ).prefetch_related('seats')
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        'user__first_name',
        'user__last_name',
        'bus__bus_number',
        'busroute__route_name',
        'status'
    ]
    filterset_fields = ['status', 'created']

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["booking", "seat_number", "is_cancelled" ]

@api_view(['GET'])
def list_bookings(request, busroute_uuid):
    date_str = request.query_params.get('date')
    filters = {'busroute__uuid': busroute_uuid}

    if date_str:
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            filters['created__date'] = date
        except ValueError:
            return Response(
                {"error": "Invalid date format. Use format: YYYY-MM-DD"},
                status=status.HTTP_400_BAD_REQUEST
            )

    bookings = Booking.objects.filter(**filters).select_related(
        'user', 'bus', 'busroute'
    ).prefetch_related('seats')

    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def cancel_seat(request, booking_uuid):
    booking = get_object_or_404(Booking, uuid=booking_uuid)
    seat_number = request.data.get("seat_number")
    try:
        seat = Seat.objects.get(
            booking=booking,
            seat_number=seat_number,
            is_cancelled=False
        )
    except Seat.DoesNotExist:
        return Response({"error": "Seat not found or already cancelled."}, status=status.HTTP_400_BAD_REQUEST)
    seat.is_cancelled = True
    seat.save()
    return Response(SeatSerializer(seat).data, status=status.HTTP_200_OK)

@api_view(['POST'])
def cancel_booking(request, booking_uuid):
        booking = Booking.objects.get(uuid=booking_uuid)
        booking.status = 'CANCELLED'
        booking.save()
        booking.seats.update(is_cancelled=True)

        serializer = BookingSerializer(booking)
        return Response({
            "message": "Booking cancelled successfully",
            "booking": serializer.data
        })

@api_view(['POST'])
def book_seat(request, booking_uuid):
    booking = get_object_or_404(Booking, uuid=booking_uuid)
    serializer = SeatSerializer(data=request.data, context={'booking': booking})
    if serializer.is_valid():
        seat = serializer.save(booking=booking)
        response_serializer = SeatSerializer(seat)
        return Response({
            "message": "Seats booked successfully.",
            "data": response_serializer.data
        }, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

