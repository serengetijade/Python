from django.forms import ModelForm
from .models import Account
from .models import Transaction

class AccountForm(ModelForm):   #Create a class/form object. Inherit information via ModelForm django mehtod.
    class Meta:                 #Define its meta information:
        model = Account         #Connect this ModelForm the the model object defined in mainapp/models.py
        fields = '__all__'      #'__all__' is a dunder shortcut to grab all the fields within the Product model, define in products/models.pyclass AccountForm(ModelForm):    #inherit information from ModelForm

class TransactionForm(ModelForm):    #inherit information from ModelForm
    class Meta:
        model = Transaction     #Connect this ModelForm the the model object defined in mainapp/models.py
        fields = '__all__'      #'__all__' is a dunder shortcut to grab all the fields within the Product model, define in products/models.pyclass AccountForm(ModelForm):    #inherit information from ModelForm
