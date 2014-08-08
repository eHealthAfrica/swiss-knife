from django.conf.urls import patterns, include, url
from auto_deploy import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='auto_deploy'),
)
