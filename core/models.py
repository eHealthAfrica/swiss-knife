from django.db import models
from ehealth_tools.django_tools.mixins import HistoryFieldsMixin

class Driver(HistoryFieldsMixin):
    name = models.CharField(max_length=50)

class Vehicle(HistoryFieldsMixin):
    name = models.CharField(max_length=50)
    plate_number = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=50, blank=True, null=True)
    tank_size = models.IntegerField(blank=True, null=True)
    fuel_type = models.CharField(max_length=20, blank=True, null=True)
    last_driver = models.ForeignKey(Driver, null=True, blank=True)

class Event(HistoryFieldsMixin):
    EVENT_TYPES = (
        ('Car Incident',) * 2,
        ('Security Incident',) * 2,
        ('Driving Started',) * 2,
        ('Driving Stopped',) * 2,
    )
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    driver = models.ForeignKey(Driver)
    timestamp = models.DateTimeField()

