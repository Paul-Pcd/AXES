#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import patterns, url
from systemmanage import views

urlpatterns = patterns(
    '',
    url(r'^idc/$', views.idcListView, name='idclisturl'),
    url(r'^game/$', views.gameListView, name='gamelisturl'),
    url(r'^addgame/$', views.addGameView, name='addgameurl'),
    url(r'^addidc/$', views.addIdcView, name='addidcurl'),
    url(r'^editidc/(?P<ID>[^/]+)/$', views.editIdcView, name='editidcurl'),
    url(r'^delidc/$', views.delIdcView, name='delidcurl'),
    url(r'^editgame/(?P<ID>[^/]+)/$', views.editGameView, name='editgameurl'),
    url(r'^delgame/$', views.delGameView, name='delgameurl'),
)
