from rest_framework import viewsets
from .models import Bus, BusRoute
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from .serializers import BusSerializer,BusRouteSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from bus.filters import BusRouteFilter 
from booking.serializers import AvailableSeatsSerializer



class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["bus_number","bus_name", "bus_type" ]
    
class BusRouteViewSet(viewsets.ModelViewSet):
    queryset = BusRoute.objects.all().select_related('bus')
    serializer_class = BusRouteSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BusRouteFilter 
    search_fields = ["source", "bus__name", "destination", "date", "price"]
    lookup_field = 'uuid'
    @action(detail=True, methods=['get'])
    def available_seats(self, request, uuid=None):
        bus_route = self.get_object()
        serializer = AvailableSeatsSerializer(bus_route)
        return Response(serializer.data)

    
@api_view(['GET'])
def get_buses_betweeen_cities(request):
    source = request.GET.get('source')
    destination = request.GET.get('destination')
    date = request.GET.get('date')
    
    if not all([source, destination]):
        return Response(
            {"error": "Missing required parameters: source and destination"}, 
            status=status.HTTP_400_BAD_REQUEST
        ) 
    query = BusRoute.objects.filter(
        source=source,
        destination=destination
    )
    if date:
        query = query.filter(date=date)
    buses = query.select_related('bus')
    serializer = BusRouteSerializer(buses, many=True)
    return Response(serializer.data)
    
        
    