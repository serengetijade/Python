from django.db import models
import datetime
from datetime import datetime, date

class Account(models.Model):
    First_Name = models.CharField(max_length=60)
    Last_Name = models.CharField(max_length=60)
    Starting_Balance = models.DecimalField(default=0.00, max_digits=10000 , decimal_places=2)
    #Object manager:
    Accounts = models.Manager()

    def __str__(self):
        return self.First_Name + ' ' + self.Last_Name

transaction_choices = [
    ('Deposit', 'Deposit'),
    ('Withdrawl', 'Withdrawl'),
]

class Transaction(models.Model):
    Date_of_Transaction = models.DateField(auto_now_add=True)
    Type_of_Transaction = models.CharField(max_length=60, choices=transaction_choices)
    Amount = models.DecimalField(default=0.00, max_digits=10000 , decimal_places=2)
    Description = models.TextField(max_length=300, default="", blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)  #Reference the Account class defined above.
    #Object manager:
    Transactions = models.Manager()