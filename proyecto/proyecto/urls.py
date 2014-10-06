from django.conf.urls import patterns, include, url
from django.contrib import admin
from proyecto.apps.usuario.views import *

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^inicio/', include("proyecto.apps.usuario.url")),   
)