from django.contrib import admin
from django.urls import path
from . import views                         #import the views.py file from this directory
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include        #import to reference additional pages.

urlpatterns = [
    #URL syntax: ('pattern to watch for', file.methodName, name="shortcut name")
    path('admin_console', views.admin_console, name="admin_console")        #admin_console is a method defined in product/views.py
]