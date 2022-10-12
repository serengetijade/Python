##The project 'switchboard'. A urls.py file doesn't hold the actual file paths, but rather, it puts together the path to the correct method, as defined in views.py.
from django.contrib import admin
from django.urls import path
from . import views                         #import the views.py file from this directory
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include        #import to reference additional pages.

urlpatterns = [
    #URL syntax: ('pattern to watch for', file.methodName, name="shortcut name")
    path('admin_console', views.admin_console, name="admin_console") ,       #admin_console is a method defined in product/views.py
    path('<int:pk>/details/>', views.details, name="details"),                #calls the details view (which calls the details method and passes along the primary key- an integer)
]