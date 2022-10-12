##Models are class objects that map to a database.
#Class = a database table
#An instance of that class = A record (a row) of that table

from django.db import models

##Create a drop down list of otptions- these are specific tuples that will appear when the choices option is selected for an attribute in a given class.
TYPE_CHOICES = {
    ('appetizers', 'appetizers'),   #The first element in each tuple is the value that will be stored in the database. The second element is displayed by the field’s form widget.
    ('entrees', 'entrees'),         #...the second element is displayed by the field’s form widget.
    ('desserts', 'desserts'),
    ('drinks', 'drinks'),           #The last item IS followed by a comma
    }

##Define a Model class
class Product(models.Model):        #name the Model class 'Product' (remember that general convention is to capitalize class names).'models.Models' is the Parent class which this is inheriting from.
    #Syntax: attribute = models.fieldType(field option, field option, etc)
    type = models.CharField(max_length=60, choices=TYPE_CHOICES)                    #invoke models, then define the type. 'CharField' is a text string. Its always good to set a max_length. Create a field called 'choices' and inherit the info from 'TYPE_CHOICES'.
    name = models.CharField(max_length=60, default="", blank=True, null=False)      #default sets the value as empty. blank=True means the forms that show up on the website can be blank, whereas an option of null=False means in the database null cannot be accepted.
    description = models.TextField(max_length=300, default="", blank=True)          #TextField allows for longer inputs.
    price = models.DecimalField(default=0.00, max_digits=10000 , decimal_places=2)  #DecimalField requires max_digit and decimal_places
    image = models.CharField(max_length=255, default="", blank=True)

    objects = models.Manager()      #define 'objects' as the model Manager. The Manager is what manages the link between the framework and the table.

    #List any objects by name of the attribute, in this case the attribute named 'name':
    def __str__(self):              # __str__ is a method automatically given to each model- it coerces and displays a plain string, like when you display an object ni an interative console or in the admin.
        return self.name            #Define that this method will return the actually name of the object, within the named 'self' class.

    #Change the DISPLAY name of the class:
    #class Meta:
    #    verbose_name = "Products"        #Optional override the pluralized name. Use this if you want to change the name of a class after it has been initialized.

##in the  app's admin file (NOT in the mainapp directory), add:
#from .modules import Profiles
#admin.site.register(Profile)
##then in the mainApp's settings.py file:
##in INSTALLED_APPS = [  ...add to the end:
##'appName',     #'the name of the app file'  created via >python manage.py startapp appName'

 
