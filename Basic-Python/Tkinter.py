##__init__ and SELF FUNCTION REVIEW
#Example1
class ClassName0:                               #start Class Names with a Capital Letter
    def __init__(self, attributeA, attributeB): #declare "self" and list any attributes
        self.variableA = attributeA             #attributeA and attributeB are placeholders
        self.variableB = attributeB             #Create “variableA” and “variableB” to pass whatever value is later defined to parameterA/B
    #refer to the (future TBD) parameters as the variables defined above
    def classMethod(abc):                       #In a function definition, name only one parameter
        print("Hello " + abc.variableA)         #Call multiple parameters by referencing the (variables) name as defined in the Class definition


instance1 = ClassName0("Jade", "attributeB")    #Create an instance and pass in the parameter value(s)
instance1.classMethod()                         #Call the function/method
#END REVIEW

##TKINTER
import tkinter;
from tkinter import *
print(tkinter.Tcl().eval('info patchlevel'));   #see your version of tkinter

class ClassName(Frame):             #Frame is the Tkinter keyword to declare a parent class
    def __init__(self, master):     #Declaring 'self' names this class as 'self', which is then used to refrence this instance of this class (itself); so then 'master' is keyword to identify this as the parent class
        Frame.__init__(self);
        self.master = master;        #Create a varaible “master” to pass whatever value is later defined to parameter "master"
        #function statements:
        self.master.resizable(width=False,height=False);
        self.master.geometry('{}x{}'.format(500, 300));
        self.master.title("Tkinter Basics!");
        self.master.config(bg='lavender');

        #create variables at the same indentation as Frame.__init__
        self.variable0 = StringVar();
        self.variable1 = StringVar();
        #self.variable0.set("First");
        #self.variable1.set("Last");
        #print(self.variable0.get() + " " + self.variable1.get())    #use .get() method to call the value

        #ROW 0
        self.variableLabel0 = Label(self.master, text="First Name: ", font=("Helvetica", 16), bg='lavender');   #Label is a built in Tkinter 'widget'. Configure it's appearance via various keywords.
        self.variableLabel0.grid(row=0, column=0, padx=(30,0) , pady=(30,0));           #Assign a location. Whatever Geometry Manager is used, it must be used throughtout the ENTIRE document.

        self.variableEntry0 = Entry(self.master, text=self.variable0, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.variableEntry0.grid(row=0, column=1, padx=(30,0) , pady=(30,0));           #If you fail to assign a location, the element will not appear in the master object (the GUI window).

        #ROW 1
        self.variableLabel1 = Label(self.master, text="Last Name: ", font=("Helvetica", 16), bg='lavender');
        self.variableLabel1.grid(row=1, column=0, padx=(30,0) , pady=(30,0) );          

        self.variableEntry1 = Entry(self.master, text=self.variable1, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.variableEntry1.grid(row=1, column=1, padx=(30,0) , pady=(30,0) )           

        #ROW 2
        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.functionSubmit);   #Button is a built in Tkinter 'widget'. Configure it's appearance via various keywords.
        self.btnSubmit.grid(row=2, column=1, padx=(0,0) , pady=(30,0), stick=NE );

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.functionCancel);   #command is a built-in Tkinter keyword that executes a function.
        self.btnCancel.grid(row=2, column=1, padx=(0,100) , pady=(30,0), stick=NE );

        #Row 3
        self.labelDisplay = Label(self.master, text="", font=("Helvetica", 16), fg='black', bg='lavender');     #When defining this Label, leave text as null (text=""), then later use get() method to configure it
        self.labelDisplay.grid(row=3, column=1, padx=(30,0) , pady=(30,0)); 

    def functionSubmit(self):   #Define the function called by the btnSubmit command. Functions must go at the same indentation level as the class definition.            
        variableEntry1 = self.variable0.get();      #Use .get() method to pull a value from another attribute/parameter/element and insert into this variable/element
        variableEntry2 = self.variable1.get();
        self.labelDisplay.config(text="Hello {} {}!".format(variableEntry1, variableEntry2));

    def functionCancel(self):   #Define the functoin called by the btnCancel command. Functions must go at the same indentation level as the class definition.    
        self.master.destroy();
        
if __name__ == "__main__":
    instance1 = Tk();                   #Instantiate Tkninter via Tk(). The insance of the class is "instanceName"1. The frame object gets passed in from the class definition (ClassName).
    variableName = ClassName(instance1) #Attach this object (variableName) to the root object (instanceName)
    instance1.mainloop()                #Ensure the function continuously runs and doesn't close after the first iteration, until it is instructed to close (by other features/functions).

