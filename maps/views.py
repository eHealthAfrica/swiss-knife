import datetime
import simplejson as json
import decimal

from django.http import HttpResponse
from django.shortcuts import render

from core.models import Event, VehicleLocation

class DecimalEncoder(json.JSONEncoder):
    def _iterencode(self, o, markers=None):
        if isinstance(o, decimal.Decimal):
            # wanted a simple yield str(o) in the next line,
            # but that would mean a yield on the line with super(...),
            # which wouldn't work (see my comment below), so...
            return (str(o) for o in [o])
        return super(DecimalEncoder, self)._iterencode(o, markers)


def get_latest_events(request, seconds):
    response = []
    status = 200
    for f in Event.objects.filter(timestamp__gte=datetime.datetime.now()-datetime.timedelta(0,int(seconds))):
        event = {}
        event['lat'] = f.lat
        event['lon'] = f.lon
        event['event_type'] = f.event_t_id
        event['timestamp'] = f.timestamp.strftime('%s')
        event['driver'] = f.driver_id
        event['vehicle'] = f.vehicle_id
        response.append(event)
    return HttpResponse(
        json.dumps(response, use_decimal=True),
        content_type = 'application/json; charset=utf8',
        status=status
    )

def get_latest_vehicle_locations(request, seconds):
    response = []
    status = 200
    for f in VehicleLocation.objects.filter(timestamp__gte=datetime.datetime.now()-datetime.timedelta(0,int(seconds))).order_by('vehicle','timestamp'):
        event = {}
        event['lat'] = f.lat
        event['lon'] = f.lon
        event['event_type'] = f.event_t_id
        event['timestamp'] = f.timestamp.strftime('%s')
        event['driver'] = f.driver_id
        event['vehicle'] = f.vehicle_id
        response.append(event)
    return HttpResponse(
        json.dumps(response, use_decimal=True),
        content_type = 'application/json; charset=utf8',
        status=status
    )