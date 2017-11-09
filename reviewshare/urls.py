#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search', views.search, name='search'),
    url(r'^new', views.new, name='new'),
    url(r'^create', views.create, name='create'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]
