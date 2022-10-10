#Python Version: 3.10.7
#
#Author:        Jade Abreu
#
#Purpose:       Student Tracking Demo.
#               This project demonstrates OOP, Tkinter GUI module,
#               -Tkinter parent and child class relationships.
#               -Image Label
#               -Text Label
#               -Buttons
#               -Listbox with (bound) Scrollbar
#               -Call functions from other files
#               The code is heavily noted to serve as future tutorials.
#
#Tested OS:     This code was written and tested to work with Windows 11.

import tkinter as tk;
from tkinter import *;
from tkinter import messagebox, Image;

import PIL;
from PIL import ImageTk, Image;

import StudentTrackingMain;
import StudentTrackingFunctions;

def loadGUI(self):
    self.master.config(bg='lightblue');
    ##LOGO
    # Create a photoimage object of the image in the path
    # Create an object of tkinter ImageTk
    self.img = ImageTk.PhotoImage(Image.open("logo.png"))
    self.labelImg = tk.Label(self.master, image=self.img, bg='lightblue')
    self.labelImg.grid(row=0, column=0, columnspan=5, padx=(0,0), pady=(10,0), sticky=N)
    
    ##LISTBOX WITH SCROLLBAR
    self.scrollbar1 = Scrollbar(self.master, orient=VERTICAL);
    self.listbox1 = Listbox(self.master, exportselection=0, yscrollcommand=self.scrollbar1.set, width=40);
    self.listbox1.bind('<<ListboxSelect>>', lambda event: StudentTrackingFunctions.onSelect(self, event));
    self.scrollbar1.config(command=self.listbox1.yview);
    self.scrollbar1.grid(row=2, column=4, rowspan=6, columnspan=1, padx=(0, 0), pady=(0,0), sticky=N+E+S);
    self.listbox1.grid(row=2, column=0, rowspan=6, columnspan=5, padx=(30,0), pady=(10,10), sticky=N+W);

    ##LABELS
    #ROW 1.0
    self.labelInfo = tk.Label(self.master, text="Student Tracking Information:", font=('Sans-serif', 18), bg='lightblue', fg='#3366cc')
    self.labelInfo.grid(row=1, column=0, columnspan=5, padx=(0,0), pady=(0,0), sticky=N)
    #Row 8.0 
    self.labelFN = tk.Label(self.master, text="First Name:", bg='lightblue')                    
    self.labelFN.grid(row=8, column=0, padx=(27,0), pady=(10,0), sticky=N+W)    
    #ROW 10.0
    self.labelLN = tk.Label(self.master, text="Last Name:", bg='lightblue')
    self.labelLN.grid(row=10, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    #ROW 12.0
    self.labelPhone = tk.Label(self.master, text="Phone Number:", bg='lightblue')
    self.labelPhone.grid(row=12, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    #ROW 14.0
    self.labelEmail = tk.Label(self.master, text="Email Address:", bg='lightblue')
    self.labelEmail.grid(row=14, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    #ROW 16.0
    self.labelCurrentCourses = tk.Label(self.master, text="Current Course(s):", bg='lightblue')
    self.labelCurrentCourses.grid(row=16, column=0, padx=(27,0), pady=(10,0), sticky=N+W)

    ##ENTRYs
    #ROW 9.0
    self.entryFN = tk.Entry(self.master, text="");
    self.entryFN.grid(row=9, column=0, rowspan=1, columnspan=4, padx=(30,40), pady=(0,0), sticky=N+E+W);
    #ROW 11.0
    self.entryLN = Entry(self.master, text="");
    self.entryLN.grid(row=11, column=0, rowspan=1, columnspan=4, padx=(30,40), pady=(0,0), sticky=N+E+W);
    #ROW 13.0
    self.entryPhone = Entry(self.master, text="");
    self.entryPhone.grid(row=13, column=0, rowspan=1, columnspan=4, padx=(30,40), pady=(0,0), sticky=N+E+W);
    #ROW 15.0
    self.entryEmail = Entry(self.master, text="");
    self.entryEmail.grid(row=15, column=0, rowspan=1, columnspan=4, padx=(30,40), pady=(0,0), sticky=N+E+W);
    #ROW 17.0
    self.entryCurrentCourses = Entry(self.master, text="");
    self.entryCurrentCourses.grid(row=17, column=0, rowspan=1, columnspan=4, padx=(30,40), pady=(0,0), sticky=N+E+W);

    ##BUTTONs
    #ROW 18.0
    self.btnAdd = tk.Button(self.master, width=12, height=2, text="Add", command=lambda:StudentTrackingFunctions.addToList(self));
    self.btnAdd.grid(row=18, column=0, padx=(15,0), pady=(45,10), sticky=E);
    #ROW 18.1
    self.btnUpdate = tk.Button(self.master, width=12, height=2, text="Update", command=lambda:StudentTrackingFunctions.onUpdate(self));
    self.btnUpdate.grid(row=18, column=1, padx=(15,0), pady=(45,10), sticky=W);
    #ROW 18.2
    self.btnDelete = tk.Button(self.master, width=12, height=2, text="Delete", command=lambda:StudentTrackingFunctions.onDelete(self));
    self.btnDelete.grid(row=18, column=2, padx=(15,0), pady=(45,10), sticky=W);
    #ROW 18.4
    self.btnClose = tk.Button(self.master, width=12, height=2, text="Close", command=lambda:StudentTrackingFunctions.askQuit(self));
    self.btnClose.grid(row=18, column=4, columnspan=1, padx=(15,0), pady=(45,10), sticky=W);

    ##CREATE THE DB
    StudentTrackingFunctions.createDB(self);

    ##REFRESH
    StudentTrackingFunctions.onRefresh(self);

if __name__ == "__main__":
    pass;
