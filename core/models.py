from django.db import models
from ehealth_tools.django_tools.mixins import HistoryFieldsMixin

class Driver(HistoryFieldsMixin):
    phone = models.CharField(max_length=50)
    name = models.CharField(max_length=50, blank=True, null=True)

class Vehicle(HistoryFieldsMixin):
    license = models.CharField(max_length=50)
    name = models.CharField(max_length=50, blank=True, null=True)
    vehicle_type = models.CharField(max_length=50, blank=True, null=True)
    tank_size = models.IntegerField(blank=True, null=True)
    fuel_type = models.CharField(max_length=20, blank=True, null=True)
    last_driver = models.ForeignKey(Driver, null=True, blank=True)

class EventType(HistoryFieldsMixin):
    code = models.IntegerField()
    name = models.CharField(max_length=50)

class Event(HistoryFieldsMixin):
    # EVENT_TYPES = (
    #     ('Car Incident',) * 2,
    #     ('Security Incident',) * 2,
    #     ('Driving Started',) * 2,
    #     ('Driving Stopped',) * 2,
    # )
    # event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    event_t = models.ForeignKey(EventType, null=True)
    lat = models.DecimalField(max_digits=19, decimal_places=6)
    lon = models.DecimalField(max_digits=19, decimal_places=6)
    driver = models.ForeignKey(Driver)
    vehicle = models.ForeignKey(Vehicle, blank=True, null=True)
    timestamp = models.DateTimeField()

class VehicleLocation(HistoryFieldsMixin):
    lat = models.DecimalField(max_digits=19, decimal_places=6)
    lon = models.DecimalField(max_digits=19, decimal_places=6)
    driver = models.ForeignKey(Driver)
    vehicle = models.ForeignKey(Vehicle, blank=True, null=True)
    timestamp = models.DateTimeField()