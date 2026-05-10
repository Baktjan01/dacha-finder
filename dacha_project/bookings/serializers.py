from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id', 'dacha', 'telegram_id', 'telegram_username',
            'date_from', 'date_to', 'total_price', 'deposit_amount', 'status'
        ]
        read_only_fields = ['total_price', 'deposit_amount', 'status']