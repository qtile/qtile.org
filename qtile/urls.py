from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^download/$', views.Download.as_view(), name='download'),
    url(r'^screenshots/$', views.Screenshots.as_view(), name='screenshots'),
    url(r'^videos/$', views.Videos.as_view(), name='videos'),
)
