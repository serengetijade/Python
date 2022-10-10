#Python Version: 3.10.7
#
#Author:        Jade Abreu
#
#Purpose:       This project demonstrates OOP, Tkinter GUI module,
#               
#               The code is heavily noted to serve as future tutorials.
#
#Tested OS:     This code was written and tested to work with Windows 11.
import tkinter as tk
from tkinter import *
from tkinter import messagebox, Image

win = tk.Tk()                       #Create an root widget. This is the Parent Class. Tkinter must be instantiated in order to use it, and that's what this does.
#win.mainloop()                     #Use the .mainloop() method to keep the instance open until contrary instructions are recieved. 

##BUTTONS
f = Frame(win)                      #Create an INSTANCE of the Parent Class (win), and name that instance f.
b1 = Button(f, text="Uno");         #'f' indicates that this Button widget is within the instance named 'f', in this case that is also the Parent Class. 
b2 = Button(f, text="Two");         #'text' is an option of this widget. It is what appears on the face of the button.
b3 = Button(f, text="Three");
b1.pack(side=LEFT)                  #.pack() is a method  of the Button widget. It is a geometry manager method, like .grid() is.
b2.pack(side=LEFT)                  #'side' is an option of the .pack() geometry method.
b3.pack(side=LEFT)
labelOver = Label(win, text="This label is over all buttons")   #Label is a tkinter widget. 'win' indicates that this widget is within the Parent Class named 'win', so it will appear before the frame.
labelOver.pack()
f.pack()                            #Apply the pack() geometry method to the class named 'f'.

##CONFIGURE METHOD- Use .configure() to change buttons or assign functions
b1.configure(text="One")            #Use .configure() to change a widget option

def btn1():
    print("Button 'One' was clicked.")

b1.configure(command=btn1)          #Use .configure() to change/add a widget option. Here it is adding command, which is an option of the Button widget. command identifies the function/method to be called when the buttton is clicked.  

##ENTRY WIDGET
v = StringVar()                     #To use a variable in tkinter, the first step it to declare its type.
e = Entry(win, textvariable=v, width=55)      
e.pack(padx=(10))
v.set("This is set by the programer, but the user can change this value")#Set the value of the entry widget.
v.get()                             #The .get() method will retrieve whatever is the value of the entry widget.

def getEntry():
    v2 = v.get()                    #Retrieve the current value of the entry widget.
    print("The entry widget\'s current value is: " + v2);
b2.configure(command=getEntry)


##LISTBOX WIDGET
labellb = Label(win, text="Listbox:")#'win' indicates that it is inside the Parent Class 'win'. 
labellb.pack()                      #Within the pack() method, display this widget after the last win object (the Entry box).
lb = Listbox(win, height=3)         #Create a listbox widget. Make it a widget in the 'win' Parent Class. 
lb.pack(side=LEFT, padx=(10,0), pady=(0,10))   #Within the pack() method, display this widget after the last win object (the labellb)
lb.insert(END, "First entry")       #Use the listbox method .insert to add a value to the END of the list.
lb.insert(END, "Second entry")
lb.insert(END, "Third entry")
lb.insert(END, "Fourth entry")

##SCROLLBAR WIDGET
sb = Scrollbar(win, orient=VERTICAL, cursor='gumby')
sb.pack(side=LEFT, fill=Y)
sb.configure(command=lb.yview)      #Use the command option of the configure method to Use the lsitbox method yview to make the lisstbox vertially scrollable- must set the command options of the associated vertical scrollbar with this method.
lb.configure(yscrollcommand=sb.set) #Use the listbox option yscrollcommand to .set(a method) it equal to sb(the scrollbar)

#CURSOR SELECTION - a listbox method
#.curselection() returns a tuple containing the line numbers of the selected element or elements, counting from 0. If nothing is selected, returns an empty tuple.
def getCurSelection():
    var = lb.curselection()
    print("The line number selected: " +str(var))
b3.configure(command=getCurSelection)
