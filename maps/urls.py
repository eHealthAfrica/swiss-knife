from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from views import apiview

urlpatterns = patterns('',
    url(r'^api/$', apiview), #TODO replace with api inclusion !
    url(r'^$', TemplateView.as_view(template_name='maps/index.html')),
)