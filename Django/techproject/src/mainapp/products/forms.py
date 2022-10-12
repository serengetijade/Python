from django.forms import ModelForm      #import the necessary class objects
from .models import Product

#create the class object that gets its values from a model
class ProductForm(ModelForm):    #inherit information from ModelForm, defined in products/forms.py
    class Meta:
        model = Product         #Connect this ModelForm the the model object defined in mainapp/models.py
        fields = '__all__'      #'__all__' is a dunder shortcut to grab all the fields within the Product model, define in products/models.py
