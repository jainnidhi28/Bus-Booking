import django_filters
from bus.models import BusRoute

class BusRouteFilter(django_filters.FilterSet):
    source = django_filters.CharFilter(lookup_expr='icontains')
    destination = django_filters.CharFilter(lookup_expr='icontains')
    date = django_filters.DateFilter()
    price = django_filters.NumberFilter()

    class Meta:
        model = BusRoute
        fields = ['source', 'destination', 'date', 'price']