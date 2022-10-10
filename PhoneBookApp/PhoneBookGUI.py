#Python Version: 3.10.7
#
#Author:        Jade Abreu
#
#Purpose:       Phone Book Demo. This project demonstrates OOP, Tkinter GUI module,
#               Tkinter parent and child class relationships.
#
#Tested OS:     This code was written and tested to work with Windows 11.

from tkinter import *;
import tkinter as tk;
from tkinter import messagebox;

import PhoneBookMain;
import PhoneBookFunctions;


def loadGUI(self):      #passing in self allows the function to be called in PhoneBookMain > ParentWindow class and be read as an element of that class.
    ##LABELS
    #ROW 0.0
    self.labelFN = tk.Label(self.master, text="First Name:")                    #Because an alias was assigned to the tkinter module (line 11) you must reference to call a tkinter widget. 
    self.labelFN.grid(row=0, column=0, padx=(27,0), pady=(10,0), sticky=N+W)    #.grid() geometry 
    #ROW 2.0
    self.labelLN = tk.Label(self.master, text="Last Name:")
    self.labelLN.grid(row=2, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    #ROW 4.0
    self.labelPhone = tk.Label(self.master, text="Phone Number:")
    self.labelPhone.grid(row=4, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    #ROW 6.0
    self.labelEmail = tk.Label(self.master, text="Email Address:")
    self.labelEmail.grid(row=6, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    #ROW 0.2
    self.labelInfo = tk.Label(self.master, text="Information:")
    self.labelInfo.grid(row=0, column=2, padx=(0,0), pady=(10,0), sticky=N+W)

    ##ENTRY
    #ROW 1.0
    self.entryFN = tk.Entry(self.master, text="");
    self.entryFN.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W);
    #ROW 3.0
    self.entryLN = Entry(self.master, text="");
    self.entryLN.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W);
    #ROW 5.0
    self.entryPhone = Entry(self.master, text="");
    self.entryPhone.grid(row=5, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W);
    #ROW 7.0
    self.entryEmail = Entry(self.master, text="");
    self.entryEmail.grid(row=7, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W);

    ##LISTBOX WITH SCROLLBAR
    self.scrollbar1 = Scrollbar(self.master, orient=VERTICAL);
    self.listbox1 = Listbox(self.master, exportselection=0, yscrollcommand=self.scrollbar1.set, width=30);
    self.listbox1.bind('<<ListboxSelect>>', lambda event: PhoneBookFunctions.onSelect(self, event));
    self.scrollbar1.config(command=self.listbox1.yview);
    self.scrollbar1.grid(row=1, column=5, rowspan=7, columnspan=1, padx=(0, 0), pady=(0,0), sticky=N+E+S);
    self.listbox1.grid(row=1, column=2, rowspan=7, columnspan=3, padx=(15,0), pady=(45,10), sticky=N+W+S);

    ##BUTTONs
    #ROW 8.0
    self.btnAdd = tk.Button(self.master, width=12, height=2, text="Add", command=lambda:PhoneBookFunctions.addToList(self));
    self.btnAdd.grid(row=8, column=0, padx=(25,0), pady=(45,10), sticky=W);
    #ROW 8.1
    self.btnUpdate = tk.Button(self.master, width=12, height=2, text="Update", command=lambda:PhoneBookFunctions.onUpdate(self));
    self.btnUpdate.grid(row=8, column=1, padx=(15,0), pady=(45,10), sticky=W);
    #ROW 8.2
    self.btnDelete = tk.Button(self.master, width=12, height=2, text="Delete", command=lambda:PhoneBookFunctions.onDelete(self));
    self.btnDelete.grid(row=8, column=2, padx=(15,0), pady=(45,10), sticky=W);
    #ROW 8.4
    self.btnClose = tk.Button(self.master, width=12, height=2, text="Close", command=lambda:PhoneBookFunctions.ask_quit(self));
    self.btnClose.grid(row=8, column=4, columnspan=1, padx=(15,0), pady=(45,10), sticky=E);

    ##CREATE THE DB
    PhoneBookFunctions.createDB(self);
    ##REFRESH
    PhoneBookFunctions.onRefresh(self);

if __name__ == "__main__":
    pass;
