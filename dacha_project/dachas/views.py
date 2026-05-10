from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Dacha
from .serializers import DachaSerializer
from bookings.models import Booking
from bookings.serializers import BookingSerializer
from datetime import date

class DachaListView(generics.ListAPIView):
    serializer_class = DachaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['city', 'name']

    def get_queryset(self):
        queryset = Dacha.objects.filter(is_active=True)
        city = self.request.query_params.get('city')
        if city:
            queryset = queryset.filter(city__icontains=city)
        return queryset

class DachaDetailView(generics.RetrieveAPIView):
    queryset = Dacha.objects.filter(is_active=True)
    serializer_class = DachaSerializer

class CheckAvailabilityView(APIView):
    def get(self, request, pk):
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')
        busy = Booking.objects.filter(
            dacha_id=pk,
            status__in=['partial', 'paid'],
            date_from__lt=date_to,
            date_to__gt=date_from
        ).exists()
        return Response({'available': not busy})

class CreateBookingView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()