from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include        #import to reference additional pages.

urlpatterns = [
    #URL syntax: ('pattern to watch for', file.methodName, name="shortcut name")
    path('', views.home, name='index'),
    #Set the url path to Create New Account page
    path('create/', views.createAccount, name='create'),
    #Set the url path to Balance Sheet page
    path('<int:pk>/balance/', views.balance, name='balance'),
    #Set the url path to Add New Transaction page
    path('transaction/', views.transaction, name='transaction')
]