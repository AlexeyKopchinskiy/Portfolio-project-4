from django.contrib import admin
from .models import Reservations
from .models import Location
from .models import Table

# Register your models here.
admin.site.register(Reservations)
admin.site.register(Location)
admin.site.register(Table)
