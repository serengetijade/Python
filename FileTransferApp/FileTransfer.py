#Python Version: 3.10.7
#
#Author:        Jade Abreu
#
#Purpose:       File Transfer App:
#               -Declare a variable type and value to set an Entry widget's option (textvariable).
#               -Get a value from an Entry widget and use it in a function.
#               -Use the filedialog method, askdirectory() option to select which location to move files from/to.
#               -Use os.listdir, os.path.join, and datetime.timestamp(os.getmtime()) to loop through files in a directory
#               and compare their time of last modification to a given time.
#               -Use shutil.move to move files that satisfy the condition statement.
#               -Use a boolean value to 'trigger' if there are no eligible files to move.
#               The code is heavily noted to serve as future tutorials.
#
#Tested OS:     This code was written and tested to work with Windows 11.

import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os, shutil, datetime, time
from datetime import datetime, timedelta

class FileTransfer(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #Configuration:
        self.master.title("File Transfer")

        #Source File(s):
        self.btnSource= Button(text="Select Source", width=20, command=self.sourceDir) #Run the function sourceDir(self) when clicked.
        self.btnSource.grid(row=0, column=0, padx=(20, 10), pady=(30,0))
        self.entrySource = Entry(width=75)
        self.entrySource.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))

        #Destination Folder:
        self.btnDestination = Button(text="Select Destination", width=20, command=self.destDir)
        self.btnDestination.grid(row=1, column=0, padx=(20, 10), pady=(15,10))
        self.entryDestination = Entry(width=75)
        self.entryDestination.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15,10))

        #Update Button and Entry(with textvaraible option):        
        self.btnUpdate = Button(text="Update", width=20, command=self.updateFiles)
        self.btnUpdate.grid(row=2, column=0, padx=(20,10), pady=(0, 15))

        updatePrompt = StringVar()
        updatePrompt.set("Enter the number of hours to search, then click 'Update'")
        self.entryUpdate = Entry(textvariable=updatePrompt, width=100)
        self.entryUpdate.grid(row=3, column=0, columnspan=3, padx=(20,10), pady=(0,10))
        
        #Transfer:
        self.btnTransfer = Button(text="Transfer Files", width=20, command=self.transferFiles)
        self.btnTransfer.grid(row=2, column= 1, padx=(200,0), pady=(0, 15))

        #Exit:
        self.btnExit = Button(text="Exit", width=20, command=self.exitProgram)
        self.btnExit.grid(row=2, column=2, padx=(10,40), pady=(0,15))
        
    def sourceDir(self):
        selectSourceDir = tk.filedialog.askdirectory()
        self.entrySource.delete(0, END)       #The .delete(0, END) will clear the content that is inserted in the Entry widget, this allows the path to be inserted into the Entry widget properly.
        self.entrySource.insert(0,selectSourceDir)       #The .insert method will insert the user selection to the source_dir Entry widget.

    def destDir(self):
        selectDestDir = tk.filedialog.askdirectory()
        self.entryDestination.delete(0, END)  #The .delete(0, END) will clear the content that is inserted in the Entry widget, this allows the path to be inserted into the Entry widget properly.
        self.entryDestination.insert(0, selectDestDir)  #The .insert method will insert the user selection to the destination_dir Entry widget.

    ##########
    def updateFiles(self):
        source = self.entrySource.get()                 #Get the file path for the source
        destination = self.entryDestination.get()       #Get the file path for the destination

        now = datetime.now()                            #Get the time now
        updatePrompt = self.entryUpdate.get()           #Get the value from user's input into the entryUpdate entry field
        updateHours = int(updatePrompt)                 #Change the user's input to an integer
        updateTime = now-timedelta(hours=updateHours)   #Calculate a time to look back to check for updates
        
        source_files = os.listdir(source)		#←create a list of all the files in the ‘path’ directory
        searchResults = False			        #←a boolean “trigger” ~ there are NO search results yet
        for i in source_files:			        #←for loop to iterate
            FullPath = os.path.join(source,i)	        #get the FullPath for each element buy using the path option .join()
            lastUpdate = datetime.fromtimestamp(os.path.getmtime(FullPath))    #Time of last modification
            if lastUpdate > updateTime:
                shutil.move(source + '/' + i, destination)  #shutil.move method from / to
                print(i + ' was successfully transfered.')                
                searchResults = True		        #←use a boolean “trigger” ~ there ARE search results 
        if not searchResults:			        #←if, at this point, there are still no search results, do this:
            print("There were no files to update");        
  
    def transferFiles(self):
        source = self.entrySource.get()                 #Get the file path for the source
        destination = self.entryDestination.get()       #Get the file path for the destination
        source_files = os.listdir(source)               #Return a list containing the names of the entries in the directory
        for i in source_files:                          #For loop to iterate through every object in source_files
            shutil.move(source + '/' + i, destination)  #shutil.move method from / to
            print(i + ' was successfully transfered.')

    def exitProgram(self):
        root.destroy()
    
if __name__ == "__main__":
    root = tk.Tk()
    App = FileTransfer(root)
    root.mainloop()
