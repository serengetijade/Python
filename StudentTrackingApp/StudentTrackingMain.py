#Python Version: 3.10.7
#
#Author:        Jade Abreu
#
#Purpose:       Student Tracking Demo. This project demonstrates OOP, Tkinter GUI module,
#               Tkinter parent and child class relationships.
#               The code is heavily noted to serve as future tutorials.
#
#Tested OS:     This code was written and tested to work with Windows 11.

from tkinter import *;
import tkinter as tk
from tkinter import messagebox;
from tkinter import messagebox, Image;
import PIL;
from PIL import ImageTk, Image;

import StudentTrackingGUI;
import StudentTrackingFunctions;

class StudentTracking(Frame):
    def __init__(self, master, *args, **kwargs):
        self.master = master;

        #master configuration
        self.master.maxsize(530,900);
        self.master.minsize(530,900);
        StudentTrackingFunctions.centerWindow(self, 530, 900);#Center the app in the user's viewscreen via a function from the document PhoneBookFunction.py
        self.master.title("Student Tracking");
        

        
        self.master.protocol("WM_DELETE_WINDOW", lambda: StudentTrackingFunctions.askQuit(self));

        #import the GUI
        StudentTrackingGUI.loadGUI(self);

if __name__ == "__main__":
    root = tk.Tk();
    App = StudentTracking(root);
    root.mainloop();
