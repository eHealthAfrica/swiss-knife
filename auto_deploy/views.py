import json

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from fabfile import auto_deploy

@csrf_exempt
def home(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        if payload['ref'] == 'refs/heads/master':
            deployed = False
            try:
                auto_deploy()
                deployed = True
            except:
                e = sys.exc_info()
                print e
            finally:
                return HttpResponse('Deployed: %s' %deployed)
        return HttpResponse('Not deployed')
    return HttpResponse('Not deployed')
