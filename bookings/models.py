from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Reservations(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    booked_on = models.DateTimeField(auto_now_add=True)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    number_of_guests = models.IntegerField()
    special_requests = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-booked_on"]

    def __str__(self):
        return f"Booking by {self.user_id.username} on {self.booking_date}"


# Define Locations Table


class Location(models.Model):
    location_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Location {self.location_name}"

# Define Tables Table


class Table(models.Model):
    table_number = models.IntegerField(unique=True)  # Unique table number
    capacity = models.IntegerField()  # Number of seats per table
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="tables")

    def __str__(self):
        return f"Table {self.table_number} ({self.location.name})"
