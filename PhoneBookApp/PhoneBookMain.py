#Python Version: 3.10.7
#
#Author:        Jade Abreu
#
#Purpose:       Phone Book Demo. This project demonstrates OOP, Tkinter GUI module,
#               Tkinter parent and child class relationships.
#               The code is heavily noted to serve as future tutorials.
#
#Tested OS:     This code was written and tested to work with Windows 11.

from tkinter import *;
import tkinter as tk;
from tkinter import messagebox;

import PhoneBookGUI;        #this document holds the the GUI widgets
import PhoneBookFunctions;  #this document holds the functions 

def guiLayout():
    from PIL import Image
    im = Image.open("GUILayout.jpg")
    im.show();
    


class ParentWindow(Frame):                              #Frame is a widget to hold other widgets
    def __init__(self,master, *args, **kwargs):         #self is the name of this class, which is used to access it throughout this document(s). Master is a tkinter keyword that gives access to the root/parent window(Tk).
        self.master = master;                           #Create a variable “master” to represent the attribute "master” within this instance. 

        #master configuration
        self.master.maxsize(550, 450);                  #(width, height)
        self.master.minsize(550, 450);
        PhoneBookFunctions.centerWindow(self, 550, 450);#Center the app in the user's viewscreen via a function from the document PhoneBookFunction.py
        self.master.title("Tkinter Phone Book",);
        self.master.config(bg="#F0F0F0");
        
        self.master.protocol("WM_DELETE_WINDOW", lambda: PhoneBookFunctions.ask_quit(self)) #windows command code

        PhoneBookGUI.loadGUI(self);                     #load the GUI widgets from PhoneBookGUI.py module

        #GUI Menu
        menubar = Menu(self.master)        
        filemenu = Menu(menubar,tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1, accelerator="Ctrl+Q", command=lambda:PhoneBookFunctions.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About this Phonebook Demo")
        helpmenu.add_separator()
        helpmenu.add_cascade(label="Help", menu=helpmenu)

        self.master.config(menu=menubar, borderwidth='1')
        

if __name__ == "__main__":
    #guiLayout(); #run to see the image guide for the GUI layout
    root = tk.Tk();                                     #To initialize tkinter, create a root widget, which is a window with a title bar and etc. The root widget has to be created before any other widgets and there can only be one root widget. root = tk.Tk()  
    App = ParentWindow(root);                           #Create an instance of the class ParentWindow, pass in root, and name it 'App'
    root.mainloop();                                    #Add .mainloop() method to 'root' object.
