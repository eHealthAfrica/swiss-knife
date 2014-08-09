from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from . import views

urlpatterns = patterns('',
    url(r'^latest_events/(?P<seconds>\d+)/$', views.get_latest_events, name='latest events'),
    url(r'^latest_vehicle_locations/(?P<seconds>\d+)/$', views.get_latest_vehicle_locations, name='latest vehicle locations'),
    url(r'^$', TemplateView.as_view(template_name='maps/index.html')),
)