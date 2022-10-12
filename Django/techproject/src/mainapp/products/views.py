##INSTRUCTIONS for where to send link requests
#
# #import necessary modules
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

# Create your Product views here. This will call the html files that users see.
def admin_console(request):                 #The general naming convention is that methods start with lower case letters
    products = Product.objects.all()        #Create a variable to query the Products class to represent all() objects. The general naming convention is that Models start with upper case letters.
    return render(request, 'products/products_page.html', {'products':products})   #render is the keyword to display the browser Syntax: {request object, the file, {context}

def details(request, pk):                   #When a request is called by the user, it goes to the url 'switchboard', which directs it to a certain method
    pk = int(pk)                            #pk is the primary key, which gets passed in with the request. This converts that value to an integer.
    item = get_object_or_404(Product, pk=pk)#assigns a variable to represent this built-in function from the django.shortcuts module. Query the database for the Product and it's value at that primary key (which is now converted to an integer).
    form = ProductForm(data=request.POST or None, instance=item)    #Invoke the ProductForm, get the information from the form that was sent via the post method (or provide a none value), then use that information to create an instance called item. The instance 'item' then passes back all of its values from its various fields
    if request.method == 'POST':
        if form.is_valid():                 #If the request method is post, check the form
            form2 = form.save(commit=False) #if the form is correct, save the form's information into the database
            form2.save()
            return redirect('admin_console')#Redirect to the admin console
        else:
            print(form.errors)
    else:
        return render(request, 'products/present_product.html', {'form':form})  #Render the page that the user sees. This actually happens first, because nothing prior has had a chance to happen yet.