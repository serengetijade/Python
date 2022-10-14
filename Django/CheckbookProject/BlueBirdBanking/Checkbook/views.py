from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction

# Create your views here.
def home(request):
    form = TransactionForm(data=request.POST or None)   #Retrieve the form
    if request.method == 'POST':
        pk = request.POST['account']    #If the form is submitted, retrieve selected account
        return balance(request, pk)     #Call this function to render information about that pk
    content = {'form':form}             #Pass content to the template as a dictionary
    return render(request, 'checkbook/index.html', content)

def createAccount(request):
    form = AccountForm(data=request.POST or None)  # Declare a variable 'form' and equate it to the existing Account form (as defined in forms.py); request.Post or None is the default syntax to take any input from the form and put it into this form.
    if request.method == 'POST':
        if form.is_valid():
            form.save()  # Apply save(), a built-in model Manager method to save an object back to the db
            return redirect('index')
        else:
            print(form.errors)  # If the form cannot meet the if statement, print the built in method .errors
            form = AccountForm()  # Create an empty version of the form as the variable 'form'.
    content = {         # Declare a variable
         'form': form,   #Pass the 'form' variable back as a dictionary.
    }
    return render(request, 'checkbook/CreatenewAccount.html', content)

def balance(request,pk):
    account = get_object_or_404(Account, pk=pk)     #Retrieve the requested account using its pk(primary key)
    transactions = Transaction.Transactions.filter(account=pk)  #Retrieve all of that accounts' transactions via the model Manager. Apply the filter option, filter by pk.
    current_total = account.Starting_Balance        #Create account total variable, starting with whatever was declared when record was created
    table_contents = {}     #Create a dictionary into which transaction info will be placed
    for t in transactions:  #Loop through (every attribute of) transactions and determine which meets the following condition
        if t.Type_of_Transaction == 'Deposit':
            current_total += t.Amount #If type=deposit, add Amount* to balance. *Amount is an attribute defined in the model definition in models.py.
            table_contents.update({t:current_total})    #Add transaction and total to the dictionary
        else:
            current_total -= t.Amount   #If type is a withdrawl (the only other option), subtract the amount from balance
            table_contents.update({t:current_total})    #Add transaction and total to the dictionary
    #Create a variable to pass account, account total balance, and transaction ifo to the template:
    content = {'account':account, 'table_contents':table_contents, 'balance':current_total}
    return render(request, 'checkbook/BalanceSheet.html',content)

def transaction(request):
    form = TransactionForm(data=request.POST or None)  # Declare a variable 'form' and equate it to the existing Account form (as defined in forms.py); request.Post or None is the default syntax to take any input from the form and put it into this form.
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['account']        #Retrieve the 'account' variable as defined in models.py. ('account' is a reference to the foreign key to the Account method, also in models.py)
            form.save()  # Apply save(), a built-in model Manager method to save an object back to the db
            return balance(request, pk)         #balance is a response method defined above
        #else:
        #    print(form.errors)  # If the form cannot meet the if statement, print the built in method .errors
        #    form = TransactionForm()  # Create an empty version of the form as the variable 'form'.
    content = {'form': form}    #Declare a variable and pass the 'form' variable back as a dictionary.
    return render(request, 'checkbook/AddTransaction.html', content)