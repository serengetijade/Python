"""BlueBirdBanking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include    #import to reference additional pages.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Checkbook.urls'))
]
