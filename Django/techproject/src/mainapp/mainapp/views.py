from django.http import HttpResponse
from django.shortcuts import render

#View instructions for the home directory
def home(request):          #Define a view method named 'home'
    ##request method to get the user's username:
    #user = request.user     #request is a method of the python request module.
    #return HttpResponse("<h1>Welcome {}!</h1>".format(user))

    #user = request.user
    #context = {'user': user,}
    #return render(request,"home.html", context)      #render this is the keyword to display the browser Syntax: {request object, the file, {context}

    products = ["Cherries", "Apples", "Oranges", "Strawberries", "Pears", "Watermelons"]
    context = {'products': products,}
    return render(request, "home.html", context)