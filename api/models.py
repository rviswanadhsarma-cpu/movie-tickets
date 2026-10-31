from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

class Theater(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, related_name='showtimes', on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    available_seats = models.IntegerField(default=100)

class Booking(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    seats_booked = models.IntegerField()
    booking_time = models.DateTimeField(auto_now_add=True)