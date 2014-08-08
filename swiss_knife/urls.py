from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.models import User
from core.models import Driver, Vehicle, Event

import auto_deploy

from django.contrib import admin
admin.autodiscover()

from rest_framework import viewsets, routers

# ViewSets define the view behavior.

class UserViewSet(viewsets.ModelViewSet):
    model = User

class VehicleViewSet(viewsets.ModelViewSet):
    model = Vehicle

class DriverViewSet(viewsets.ModelViewSet):
    model = Driver

class EventViewSet(viewsets.ModelViewSet):
    model = Event


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'drivers', DriverViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'events', EventViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('maps.urls')),
    #url(r'^$', 'swiss_knife.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url( r'^autodeploy/', include('auto_deploy.urls', namespace='auto_deploy')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest/', include(router.urls)),
    url(r'^rest-auth/', include('rest_framework.urls', namespace='rest_framework'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
