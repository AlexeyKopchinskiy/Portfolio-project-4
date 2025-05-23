from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import Reservations
from .models import Table
from .models import Location

# Create your views here.


class BookingList(generic.ListView):
    model = Reservations


class TableList(generic.ListView):
    model = Table


class LocationList(generic.ListView):
    model = Location
# def index(request):
#     return HttpResponse("Hello, world. You're at the bookings index.")
