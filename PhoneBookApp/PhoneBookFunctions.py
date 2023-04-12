#Python Version: 3.10.7
#
#Author:        Jade Abreu
#
#Purpose:       Phone Book Demo.
#               This project demonstrates OOP, Tkinter GUI module,
#               -Tkinter parent and child class relationships.
#               -Use winfo methods to calculate the x any y coordinates to center the Frame
#               in the user's viewscreen, by first assigning x and y as integer variables.
#               -SQL Module:
#                   -Create a DB and table
#                   -Insert records into the table
#                   -Count the number of records
#                   -Update table with (new) phone and/or email Entry values
#               -Declare an event, use the .curselection()[0] option, and .get() method to get the user's selection. 
#                   -Get record values for the user's selection and insert them in the Entry widget.
#               -Require a user to fill out all Entry widgets or else prompt a pop-up messagebox.
#               -Pop-ups: Use messagebox with showerror and showinfo options to display pop-up messages.
#
#Tested OS:     This code was written and tested to work with Windows 11.

import os;
from tkinter import *;
import tkinter as tk;
from tkinter import messagebox;
import sqlite3;

import PhoneBookMain;
import PhoneBookGUI;

def centerWindow(self, w, h):                               #Pass in the tkinter frame(master) refrence and widht/height dimensions PhoneBookMain.py
    viewscreenWidth = self.master.winfo_screenwidth();      #self.master is tkinter's primary window. winfo_screewidth is a method to get the width of the user's viewscreen
    viewscreenHeight = self.master.winfo_screenheight();    #viewscreenWidth|Height passes that info into variables
    #calculate x and y coordinates to center the window on teh user's viewscreen
    x = int((viewscreenWidth/2)-(w/2));                     #Mathmatics to get the screen to appear in the center of the user's viewscreen
    y = int((viewscreenHeight/2)-(h/2));
    centerGeo = self.master.geometry("{}x{}+{}+{}".format(w,h,x,y)) #Create a variable to hold the geometry for the center coordinates
    return centerGeo;                                       #Return centerGeo (which centers the GUI) to PhoneBookMain                   

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):     #messagebox widget
        self.master.destroy()                               #tkinter method to close a
        os._exit(0);                                        #os._exit(0) deletes widgets from the user's memory references. So when the program closes, it frees up the memory and avoids "memory leaks".

def createDB(self):                                         #Create a database, access the "self" object
    conn = sqlite3.connect('db_phonebook.db')               #If the database doesn't exist, the command will create it. Otherwise, it will connect to the named database, and the variable "conn" will represent that connection.
    with conn:                                              #Signal the program to recieve instructions relating to the (connected) database.
        cur=conn.cursor()                                   #cursor() is a python method to influence the (connected) database.
        cur.execute("CREATE TABLE IF NOT EXISTS table_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            First_Name TEXT, \
            Last_Name TEXT, \
            Full_Name TEXT, \
            Phone TEXT, \
            Email TEXT \
            );")                                            #.execute() is a python method to recognize SQL commands and code. \ allows the SQL code to continue onto the next line for readability purposes. 
        conn.commit()                                       #.commit() is a python method that commits any changes to the (connected) database.
    conn.close()                                            #.close() is a python method that ends the connection to the (connected) database.
    firstRun(self);                                         #The final command of this function is to call another function, firstRun().

def firstRun(self):                                         #(self) connects this function to the class named "self"
    conn = sqlite3.connect('db_phonebook.db')               #If the named database exists, the sqlite3.connect() method creates a connection to it.
    with conn:
        cur = conn.cursor()                                 #cursor() is a python method to influence the (connected) database.
        cur,count = countRecords(cur)                       #Create varaible(s) to represent the function countRecords(). Pass to it the cur variable. See below.
                                                            #after countRecords() function runds, do these commands: 
        if count < 1:                                       #Ensure there is always one entry, to avoid errors. 
            cur.execute("""INSERT INTO table_phonebook (First_Name, Last_Name, Full_Name, Phone, Email) \
            VALUES (?,?,?,?,?)""", ('John', 'Doe', 'John Doe', '503-456-1234', 'jdoe@gmail.com'))       #Use wildcards to represent future values. Add an example entry to avoid errors. 
            conn.commit()
    conn.close()                                            
#countRedords() is called by firstRun()
def countRecords(cur):                                      #You must pass in (cur) so that when the function is called in line 54, it can also call (cur) there. And because cur is defined in that function, here it will pass those values into the rest of this function.
    count=""                                                #Start 'count' as a null value
    cur.execute("""SELECT COUNT(*) FROM table_phonebook""") #use .execute() method to signal the program to recieve SQL commands from the "cur" object. Use SQL commands to count the records(rows) in the connected table.  
    count = cur.fetchone()[0]                               #Python method .fetchone() extracts the value from the cur variable
    return cur,count                                        #return the values that this function calculated for each variable: cur and count.

#This function is called by PhonebookGUI.py, listbox widget: self.listbox1.bind('<<ListboxSelect>>', lambda event: PhoneBookFunctions.onSelect(self, event));
def onSelect(self,event):                                   #Name the function, then pass in the (self, so it knows the name of the class to affect, and pass in ,event) to tell python this is an event.
    varList = event.widget                                  #Create a variable to hold the widget that is affected by the event trigger
    select = varList.curselection()[0]                      #Create a variable to hold the index number of the selection, when triggered, within the widget that is affected by the event- the index number [0] that is selected.
    value = varList.get(select)                             #Create a variable to extract the value from the the selection
    conn = sqlite3.connect('db_phonebook.db')               #Create a variable to represent the connectoin to the database
    with conn:                                              
        cursor=conn.cursor()                                #Create a variable to represent the cursor() method. cursor() is a python method to influence the (connected) database.
        cursor.execute("""SELECT First_Name, Last_Name, Phone, Email FROM table_phonebook\
            WHERE Full_Name = (?)""", [value])             #Use SQL code
        varBody = cursor.fetchall()                         #python method .fetchone() extracts the value from the cur variable. The value is returned as a tuple.
        for data in varBody:                                #Loop to access each indexed object in the tuple
            self.entryFN.delete(0,END)                      #Clear the Entry widget of whatever was displayed.
            self.entryFN.insert(0,data[0])                  #Insert the value from the selected item at index [0] into the Entry widget.
            self.entryLN.delete(0,END)
            self.entryLN.insert(0,data[1])
            self.entryPhone.delete(0,END)
            self.entryPhone.insert(0,data[2])
            self.entryEmail.delete(0,END)
            self.entryEmail.insert(0,data[3])

def addToList(self):                                        #Function to add to the list within the self class object.
    var_fname= self.entryFN.get()                           #Create a varaible to hold the value that is extracted from the Entry widget
    var_lname = self.entryLN.get()
    #Normalize the values
    var_fname = var_fname.strip()                           #Remove any blank spaces before and after the user's entry
    var_lname = var_lname.strip()                           #Ensure that the first character in each word is capitalized
    var_fname = var_fname.title()                           #Make the first letter a capital
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname, var_lname))   #The full name is a string made up of the first and last names.
    print("var_fullname: {}".format(var_fullname))          #Check to make sure the full name works
    var_phone = self.entryPhone.get().strip()
    var_email = self.entryEmail.get().strip()
    if not "@" or not "." in var_email:                     #Ensure a valid email address is entered.
        print("Incorrect email format. Please retry.")
    if (len(var_fname)>0) and (len(var_lname)>0) and (len(var_phone)>0) and (len(var_email)>0): #Force the user to fill out all fields.
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT COUNT(Full_Name) FROM table_phonebook \
                WHERE Full_Name = '{}'""".format(var_fullname)) #Check through the table to see any full name is equal to any that is being entered.
            count = cursor.fetchone()[0]                    #Use cursor.fetchone() method to extract the value of the executed count from the line above.
            checkName = count                               #Create a varaible to represent the value of the count
            if checkName == 0:                              #If the full name does NOT already exist in the table, do this:
                print("checkName: {}".format(checkName))
                cursor.execute("""INSERT INTO table_phonebook (First_Name, Last_Name, Full_Name, Phone, Email) \
                    VALUES (?,?,?,?,?)""",(var_fname, var_lname, var_fullname, var_phone, var_email)) #Check the database for existance of the fullname, if so we will alert user and disregard request. When count != 0, the name is already in use.
                self.listbox1.insert(END, var_fullname)     #Insert the values into the listbox in the self class
                onClear(self)                               #Call the onClear() function to clear all of the textboxes
            else:
                messagebox.showerror("Name Error", "'{}' already exists in the database. Please choose a different name.".format(var_fullname)) #When there IS a full name that matches the (attempted) entry, show this message. 
                onClear(self)                               #Call the onClear() function to clear all of the textboxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Editor", "Please ensure that there is data in all fields.")
                             
def onDelete(self):
    var_select = self.listbox1.get(self.listbox1.curselection())    #Create a variable to represent the value of the cursor selection from the listbox of the self class.
    conn = sqlite3.connect('db_phonebook.db')
    with conn:                                              #Create a variable to represent the cursor() method. cursor() is a python method to influence the (connected) database.
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM table_phonebook""")     #Use .execute() to enter a SQL command to count all rows in the table.
        count = cur.fetchone()[0]                           #python method .fetchone() extracts the value from the cur variable, i.e the number of objects from table_phonebook
        if count > 1:                                       #So long as the count is GREATER than 1, the database is NOT empty.
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with ({}) \nwill be deleted permenantly from the database.\n\nProceed with the deletion request?".format(var_select))
            if confirm:                                     #This treats confirm as a boolean value, so as long as it is true, do the following code:
                conn = sqlite3.connect('db_phonebook.db')   #Connect to the database
                with conn:                                  #While the connection is open:
                    cursor = conn.cursor()                  #Resent the cursor variable
                    cursor.execute("""DELETE FROM table_phonebook WHERE Full_Name = '{}'""".format(var_select)) #Use the exectute() method to perform SQL commands.
                onDeleted(self)                             #Call the onDeleted()function and pass in (self) so that it affects the self class object.
                conn.commit()
        else:                                               #If the (row) count is LESS THAN one, no entries exist to delete, so show this error message. 
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time.\n\nPlease add another record first before you can delete ({}).".format(var_select, var_select))
    conn.close()

def onDeleted(self):                                        #Pass in self so that the self class object is referenced.
    #clear the text in these entry forms
    self.entryFN.delete(0,END)                              #Use .deleted() method to delete the defined object.
    self.entryLN.delete(0,END)
    self.entryPhone.delete(0,END)
    self.entryEmail.delete(0,END)

    try:                                                    #Try Catch block prevents an invalid delete option. 
        index = self.listbox1.curselection()[0]             #Create a varaible to represent the selected object within the listbox         
        self.listbox1.delete(index)                         #Delete the selected object
    except IndexError:                                      #If the try block cannot execute, show this error message.
        pass                                                #If the try block cannot exectue, don't do anything.

def onClear(self):                                          #Pass in self so that the self class object is referenced.
    #clear the text in these entry forms
    self.entryFN.delete(0,END)                              #Use .deleted() method to delete the defined object.
    self.entryLN.delete(0,END)
    self.entryPhone.delete(0,END)
    self.entryEmail.delete(0,END)

def onRefresh(self):                                        #Populate the listbox within the self class, coinciding with the database
    self.listbox1.delete(0,END)                             #Use .deleted() method to delete the defined object (the listbox).
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM table_phonebook""")  #Use the exectute() method to perform SQL commands.
        count = cursor.fetchone()[0]                        #python method .fetchone() extracts the value from the cur variable, i.e the number of objects from table_phonebook
        i = 0                                               #Start from 0
        while i < count:                                    #Create an iteration loop that runs as long as i is less than the value of the count variable (the number of objects from table_phonebook)
            cursor.execute("""SELECT Full_Name FROM table_phonebook""")    #Select the Full Name for every row
            varList = cursor.fetchall()[i]                  #Create a varaible to hold the value of the object at index[i]
            for items in varList:                           #Create an inner loop to check through every object in varList
                self.listbox1.insert(0,str(items))          #Add each item (object in varList) and insert it into the listbox within teh self class. Add it to the end of the list. 
                i = i + 1                                   #Change the value of i, causing the loop to iterate.
    conn.close()

def onUpdate(self):                                         #Function to allow updates to the database, and therefore the listbox.
    try:
        var_select = self.listbox1.curselection()[0]        #Create a variable to hold the index number of the selection, when triggered, within the widget that is affected by the event- the index number [0] that is selected.
        var_value = self.listbox1.get(var_select)           #Create a variable to extract the value from the the selection
    except:                                                 #If the try block cannot execute, show this message via the showinfo() method.
        messagebox.showinfo("Missing selection", "No name was selected from the list box.\nCancelling the update request.")
        return
    #The user will only be allowed to update changes for phone and emails.
    #For name changes, the user will need to delete the entire record and start over.
    var_phone = self.entryPhone.get().strip()               #Normalize the entries.
    var_email = self.entryEmail.get().strip()
    if (len(var_phone)>0) and (len(var_email)>0):           #Enforce that the phone and email are NOT empty in order to access the database.
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
            cur = conn.cursor()
            cur.execute("""SELECT COUNT(Phone) FROM table_phonebook WHERE Phone='{}'""".format(var_phone))  #Ensure the provided Phone is already in the database.
            count1 = cur.fetchone()[0]                      #Python method .fetchone() extracts the value from the cur variable, i.e the 'Phone' column value from the table 'table_phonebook'.
            print(count1)
            cur.execute("""SELECT COUNT(Email) FROM table_phonebook WHERE Email='{}'""".format(var_email))  #Ensure the provided Email is already in the database.
            count2 = cur.fetchone()[0]                      #Python method .fetchone() extracts the value from the cur variable, i.e the 'Email'
            print(count2)
            if count1 == 0 or count2 == 0:                  #Count records to see if the user's changes are already in the database. If they are already there, there are no changes to update. If one return value is 0, that means there was no match and there IS something that can be updated.
                response = messagebox.askokcancel("Update Request","The following changes ({}) and ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_phone, var_email, var_value))
                print(response)
                if response:                                #This treats 'response' as a boolean value, so as long as it is true, do the following code:
                    #conn = sqlite3.connect('db_phonebook.db')
                    with conn:
                        cursor = conn.cursor()              #Connect to the database, and allow access to it
                        cursor.execute("""UPDATE table_phonebook SET Phone = '{0}', Email = '{1}' WHERE Full_Name = '{2}'""".format(var_phone, var_email, var_value)) #Use .execute() method to enter SQL commands.
                        onClear(self)                       #Call the onClear() function and tell it to affect the class 'self'
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request","No changes have been made to ({}).".format(var_value))#If 'response' is false, and the changes were not made, show this message.
            else:
                messagebox.showinfo("No changes detected", "Both ({}) and ({})\nalready exist in the database for this name.\n\nYour update request has been cancelled.".format(var_phone, var_email)) #If the name and email return 1, they must already exist. So therefore they cannot be updated to their own value.
            onClear(self)                                   #Call the onClear() function and tell it to affect the class 'self'
        conn.close()
    else:
        messagebox.showerror("Missing information", "Please select a name from the list.\n\nThen edit the phone or email information.") #Enforce that a selection is made.
    onClear(self)                                           #Call the onClear() function and tell it to affect the class 'self'

if __name__ == "__main__":
    pass;
