from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlPatterns = [ url(r'^$', 'AlmondApp.views.main'), ]