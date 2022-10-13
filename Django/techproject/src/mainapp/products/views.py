##INSTRUCTIONS for where to send link requests
#When a request is called by the user, it goes to the url 'switchboard', which directs it to a certain method (listed here)
#The method then calls the html files that the user sees....hence the 'views'.
#
#Import models, classes, and/or methods needed
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.forms import ModelForm
from .models import Product
from .forms import ProductForm

#Method to direct the user the the products_page.html, where the admin can interact view (and interact with) the Products model.
def admin_console(request):                 #The general naming convention is that methods start with lower case letters
    products = Product.objects.all()        #Create a variable to query the Products class to represent all() objects. The general naming convention is that Models start with upper case letters.
    return render(request, 'products/products_page.html', {'products':products})   #render is the keyword to display the browser Syntax: {request object, the file, {context}

def details(request, pk):                   #When a request is called by the user, it goes to the url 'switchboard', which directs it to a certain method
    pk = int(pk)                            #pk is the primary key, which gets passed in with the request. This converts that value to an integer.
    item = get_object_or_404(Product, pk=pk)#Assigns a variable to represent this built-in function from the django.shortcuts module. Query the database for the Product (using this built-in function) and it's value at that primary key (which is now converted to an integer).
    form = ProductForm(data=request.POST or None, instance=item)    #Invoke the ProductForm, get the information from the form that was sent via the post method (or provide a none value), then use that information to create an instance called item. The instance 'item' then passes back all of its values from its various fields
    if request.method == 'POST':
        if form.is_valid():                 #If the request method is post, check the form
            form2 = form.save(commit=False) #Create a varaible to hold if the form is correct
            form2.save()                    #save() is a built-in model Manager method to save an object back to the db
            return redirect('admin_console')#Redirect to the admin_console method (as defined above)
        else:
            print(form.errors)
    else:
        return render(request, 'products/present_product.html', {'form':form})  #Render the page that the user sees. This actually happens first, because nothing prior has had a chance to happen yet.

#Method to peform 'Delete' button command
def delete(request, pk):                    #When a 'delete' request is called by the user (via the urls.py 'switchboard'), direct it to this method.
    pk = int(pk)                            #pk is the primary key, which gets passed in with the request. This converts that value to an integer.
    item = get_object_or_404(Product, pk=pk)#Assigns a variable to represent this built-in function from the django.shortcuts module. Query the database for the Product (using this built-in function) and it's value at that primary key (which is now converted to an integer).
    if request.method == 'POST':
        item.delete()                       #delete() is a built-in model Manager method to delete an object from the db. Here it is being used to delete the variable 'item'
        return redirect('admin_console')    #Redirect to the admin_console method (as defined above)
    context = {"item":item,}
    return render(request, "products/confirmDelete.html", context)      #Render the page that the user sees. This actually happens first, because nothing prior has had a chance to happen yet.

#Method to perform when delete request is confirmed from the confirmDelte.html doc
def confirmed(request):                    #No pk is required for this method
    if request.method == 'POST':
        #Create form instance and bind data to it
        form = ProductForm(request.POST or None)    #Create a variable to hold the data from the ProductForm in forms.py
        if form.is_valid():
            form.delete()                   #delete() is a built-in model Manager method to delete an object from the db
            return redirect('admin_console')
    else:
        return redirect('admin_console')

def createRecord(request):                  #No pk is required for this method, it will create one for new objects as part of the Products class model (in models.py)
    form = ProductForm(request.POST or None)#Declare a variable 'form' and equate it to the existing ProductForm (as defined in forms.py); request.Post or None is the default syntax to take any input from the form and put it into this form.
    if form.is_valid():
        form.save()                         #Apply save(), a built-in model Manager method to save an object back to the db
        return redirect('admin_console')
    else:
        print(form.errors)                  #If the form cannot meet the if statement, print the built in method .errors
        form = ProductForm()                #Create an empty version of the form as the variable 'form'.
    context = {                             #Declare a variable
        'form':form,                        #Pass the 'form' variable back as a dictionary.
    }
    return render(request, 'products/createRecord.html', context)