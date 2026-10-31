from rest_framework import serializers
from .models import Movie, Theater, Showtime, Booking

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ShowtimeSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    theater_name = serializers.CharField(source='theater.name', read_only=True)
    
    class Meta:
        model = Showtime
        fields = ['id', 'movie_title', 'theater_name', 'start_time', 'available_seats']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'