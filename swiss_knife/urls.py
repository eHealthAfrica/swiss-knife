from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.models import User

import auto_deploy

from django.contrib import admin
admin.autodiscover()

from rest_framework import viewsets, routers

# ViewSets define the view behavior.

class UserViewSet(viewsets.ModelViewSet):
    model = User


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'swiss_knife.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url( r'^autodeploy/', include('auto_deploy.urls', namespace='auto_deploy')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest/', include(router.urls)),
    url(r'^rest-auth/', include('rest_framework.urls', namespace='rest_framework'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
