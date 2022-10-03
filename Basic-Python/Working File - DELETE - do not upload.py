#ABSTRACTED METHODS:
from abc import ABC, abstractmethod

class parentClass1(ABC):  #ABC stands for Abstract Base Class
    def paySlip(self, amount):
        print("Your purchase amount: ", amount)
    @abstractmethod                     #"@abstractmethod" tells Python that what follows is an abstrac method.
    def payment(self, amount):          #Define the abstract method. An abstract method is defined, but NOT implimented here. 
        pass                            #pass means that it will not be implemented (it will not run)7 unless called (by another function)
        
class DebitCardPayment(parentClass1):   #Define a child class to (parentClass)
    def payment(self, amount):          #(Re)define the abstract class in order to use it: 
        print("Your purchase amount of {} exceeded your $100 limit.".format(amount))    #Define HOW to implement the payment method (from the parent class, parentClass) when this instance is used. 

class CreditCardPayment(parentClass1):  Define a child class to (parentClass)
    def payment(self, amount):          #(Re)define the abstract class in order to use it: 
        print("Your credit card payment amount: ", amount)  #Define HOW to implement the payment method (from the parent class, parentClass) when this instance is used.

class CashPayment(parentClass1):        #Define a child class to (parentClass)
    def payment(self, amount):          #(Re)define the abstract class in order to use it: 
        print("Your cash payment amount: ", amount) #Define HOW to implement the payment method (from the parent class, parentClass) when this instance is used.

#Create in instance of the DebitCardPayment (child) class, then use that instance to call functions (passing in a value to 'amount')
obj = DebitCardPayment()                #Instantiate an instance of the 'DebitCardPayment()' class. As part of it's definition, it 
obj.paySlip("$400")                     #With obj (an instance of DebitCardPayment) run the function 'paySlip' and pass $400 in as the 'amount'.
obj.payment("400")                      #With obj (an instance of DebitCardPayment) run the function 'payment' and pass $400 in as the 'amount'.
