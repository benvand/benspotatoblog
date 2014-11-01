__author__ = 'ben'
from django.conf.urls import patterns, include, url
from .views import Login, Logout

urlpatterns = patterns('',
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
)
