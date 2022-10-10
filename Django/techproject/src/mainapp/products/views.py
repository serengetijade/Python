#import necessary modules
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your Product views here. This will call the html files that users see.
def admin_console(request):
    products = Product.objects.all()         #Create a variable to query the Products class to represent all() objects
    return render(request, 'products/products_page.html', {'products':products})   #render is the keyword to display the browser Syntax: {request object, the file, {context}