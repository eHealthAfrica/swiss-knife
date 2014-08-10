import datetime
import simplejson as json
import decimal

from django.http import HttpResponse
from django.shortcuts import render

from core.models import Event, VehicleLocation

from django.shortcuts import render_to_response

from maps.models import ReportPDF

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
    for f in Event.objects.filter(timestamp__gte=datetime.datetime.now()-datetime.timedelta(seconds=int(seconds))):
        event = {}
        event['lat'] = f.lat
        event['lon'] = f.lon
        event['event_type'] = f.event_t_id
        event['event_code'] = f.event_t.code
        event['event_name'] = f.event_t.name
        event['timestamp'] = f.timestamp.strftime('%s')
        event['driver'] = f.driver_id
        event['driver_name'] = f.driver.name
        event['driver_phone'] = f.driver.phone
        event['vehicle'] = f.vehicle_id
        if f.vehicle_id:
            event['vehicle_license'] = f.vehicle.license
        response.append(event)
    return HttpResponse(
        json.dumps(response, use_decimal=True),
        content_type = 'application/json; charset=utf8',
        status=status
    )

def get_latest_vehicle_locations(request, seconds):
    response = []
    status = 200
    for f in VehicleLocation.objects.filter(timestamp__gte=datetime.datetime.now()-datetime.timedelta(seconds=int(seconds))).order_by('vehicle','timestamp'):
        event = {}
        event['lat'] = f.lat
        event['lon'] = f.lon
        event['timestamp'] = f.timestamp.strftime('%s')
        event['driver'] = f.driver_id
        event['vehicle'] = f.vehicle_id
        response.append(event)
    return HttpResponse(
        json.dumps(response, use_decimal=True),
        content_type = 'application/json; charset=utf8',
        status=status
    )

def show_daily_reports(request):
    response = {}
    status = 200
    response['reports'] = ReportPDF.objects.all().order_by('-timestamp')
    return render_to_response('maps/report_overview.html',
        response)#,
        #context_instance=RequestContext(request))
        
def dashboard(request):
    response = {}
    status = 200
    response['reports'] = ReportPDF.objects.all().order_by('-timestamp')
    return render_to_response('maps/index.html',
        response)        