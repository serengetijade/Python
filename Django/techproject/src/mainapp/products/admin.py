from django.contrib import admin

# Register your models here.
#Syntax: from .models import model(Class)Name
from .models import Product
admin.site.register(Product)

#then in the mainApp's settings.py file:
#in INSTALLED_APPS = [  ...add to the end:
#'appName',     #'the name of the app file'  created via >python manage.py startapp appName'

