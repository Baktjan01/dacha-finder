from rest_framework import serializers
from .models import Dacha, DachaPhoto, Amenity


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['id', 'name', 'icon']


class DachaPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DachaPhoto
        fields = ['id', 'image', 'is_main']


class DachaSerializer(serializers.ModelSerializer):
    photos = DachaPhotoSerializer(many=True, read_only=True)
    amenities = AmenitySerializer(many=True, read_only=True)

    class Meta:
        model = Dacha
        fields = [
            'id', 'name', 'description', 'address', 'city',
            'latitude', 'longitude', 'price_per_day',
            'max_guests', 'num_rooms', 'amenities', 'photos'
        ]