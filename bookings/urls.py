from . import views
from django.urls import path
# from bookings import views as booking_views

urlpatterns = [
    path('', views.BookingList.as_view(), name='Booking List'),
    path('table/', views.TableList.as_view(), name='Table List'),
    path('location/', views.LocationList.as_view(), name='Location List'),
]
