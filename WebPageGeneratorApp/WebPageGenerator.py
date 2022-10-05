#Python Version: 3.10.7
#
#Author:        Jade Abreu
#
#Purpose:       Web Page Generator App:
#               Automatially generate a HTML template with a few basic elements. The template even has notes
#               to offer basic explanations and provides a framework that can be expanded and added to easily.
#               -Declare a variable type and value to set an Entry widget's option (textvariable).
#               -.get() value from Entry widget via a variable and use it in a function
#               -Pop-ups: Use messagebox with showerror options to display pop-up messages.
#               The code is heavily noted to serve as future tutorials.
#
#Tested OS:     This code was written and tested to work with Windows 11.

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import webbrowser
import PIL
from PIL import ImageTk, Image

class htmlTemplate(Frame):                      #Define a class and declare it as a Frame widget - a widget to hold other widgets
    def __init__(self,master):                 #Class Constuctor: Create a class, name it self, and use master to declare that it is the Parent Class.
        Frame.__init__(self,master)            #Instantiate the Frame widget, name it self, and use master to declare that it is the Parent Class.
        #Configuration:
        self.master.title("HTML Template Generator")

        #Logo
        self.img = ImageTk.PhotoImage(Image.open("logo.png"))
        self.labelImg = tk.Label(self.master, image=self.img)
        self.labelImg.grid(row=0, column=0, columnspan=2, padx=(0,0), pady=(10), sticky=N)

        #Title Label
        self.lblTitle = Label(self.master, text="Create a Basic Web Page:", font=('Sans-serif', 20))
        self.lblTitle.grid(row=1, column=0, columnspan=2)
        
        #Buttons
        self.btn = Button(self.master, text="Generate!", width=30, height=2, bg='lightgray', command=self.customHTML)
        self.btn.grid(row=2, column=0, columnspan=2, padx=(10), pady=(10))
        
        self.btn = Button(self.master, text="Generate a Default Page", width=30, bg='lightgray', command=self.defaultHTML)
        self.btn.grid(row=6, column=0, columnspan=2, padx=(10), pady=(10))

        #User Inputs
        customHeading = StringVar()
        self.lblHeading = Label(self.master, text="Enter a custom heading:")
        self.lblHeading.grid(row=3, column=0, padx=(10), pady=(5), sticky=W)
        self.entryHeading = Entry(self.master, text=customHeading, width=40)
        self.entryHeading.grid(row=3, column=1, padx=(0,10), pady=(5), sticky=W)
        
        customText = StringVar()
        self.lblText = Label(self.master, text="Enter custom text:")
        self.lblText.grid(row=4, column=0, padx=(10), pady=(5), sticky=W)
        self.entryText = Entry(self.master, text=customText, width=40)
        self.entryText.grid(row=4, column=1, padx=(0,10), pady=(5), sticky=W)

        customBG = StringVar()
        self.lblBG = Label(self.master, text="Enter a custom background color:")
        self.lblBG.grid(row=5, column=0, padx=(10), pady=(5), sticky=W)
        self.entryBG = Entry(self.master, text=customBG, width=40)
        self.entryBG.grid(row=5, column=1, padx=(0,10), pady=(5), sticky=W)

    def customHTML(self):
        customHeading = self.entryHeading.get()
        customText = self.entryText.get()
        customBG = self.entryBG.get()
        if customHeading =="" and customText =="":
            messagebox.showerror("Missing Text", "Please ensure that there is data in at least one field.")
        else:
            htmlFile = open("index.html", "w")
            htmlContent = "<!DOCTYPE html>\n \
            <html lang='en'>\n \
            <head>\n \
            <meta charset='utf-8'>\n \
            <meta name='viewport' content='width=device-width' />\n \
            <link rel='stylesheet' type='text/css' href='../css/fileName.css' >	                        <!--Source CSS file-->\n \
            <link rel='icon' type='image/x-icon' href='../Img/Icons/'>		                        <!--Page icon to display in browser tab-->\n \
            <script src='../js/jsfileName.js' defer></script> 					        <!--Source JavaScript file-->\n \
            <script src='http://code.jquery.com/jquery-latest.min.js' type='text/javascript'></script> 	<!--Source jQuery-->\n \
            <script src='https://cdnjs.cloudflare.com/ajax/libs/react/0.14.3/react.js'></script>		<!--Source React-->\n \
            <script src='https://cdnjs.cloudflare.com/ajax/libs/react/0.14.3/react-dom.js'></script>	<!--Source React DOM-->\n \
            <script src='https://unpkg.com/babel-standalone@6.15.0/babel.min.js'></script>		        <!--Source JSX-->\n \
            <title>HTML Template</Title>\n \
            <style>\n \
                html { \n \
                    scroll-behavior: smooth; /*specifies whether to smoothly animate the scroll position, instead of a straight jump*/ \n \
                    box-sizing: border-box;  /*include the padding and border in an element's total width and height. Default value: content-box*/ \n \
                } \n \
                body { \n \
                    text-align: center; \n \
                    background-color:"+customBG+" \n \
                } \n \
            </style> 	<!--If not using a .css stylesheet, put style element at the top of the document-->\n \
            </head>\n \
            <body>\n \
            <header></header>\n \
            <nav></nav>\n \
            <main>\n \
            <h1>"+customHeading+"</h1>\n \
            <p>"+customText+"</p></main>\n \
            <footer></footer>\n \
            <script></script> <!--If including any JavaScript, place it at the bottom of the document, before the closing /body tag-->\n \
            </body>\n \
            </html>"	
            htmlFile.write(htmlContent)
            htmlFile.close()
            webbrowser.open_new_tab("index.html")

    def defaultHTML(self):
        defaultText = 'Welcome to your Default Page'
        htmlFile = open("index.html", "w")
        htmlContent = "<!DOCTYPE html>\n \
        <html lang='en'>\n \
        <head>\n \
        <meta charset='utf-8'>\n \
        <meta name='viewport' content='width=device-width' />\n \
        <link rel='stylesheet' type='text/css' href='../css/fileName.css' >	                        <!--Source CSS file-->\n \
        <link rel='icon' type='image/x-icon' href='../Img/Icons/'>		                        <!--Page icon to display in browser tab-->\n \
        <script src='../js/jsfileName.js' defer></script> 					        <!--Source JavaScript file-->\n \
        <script src='http://code.jquery.com/jquery-latest.min.js' type='text/javascript'></script> 	<!--Source jQuery-->\n \
        <script src='https://cdnjs.cloudflare.com/ajax/libs/react/0.14.3/react.js'></script>		<!--Source React-->\n \
        <script src='https://cdnjs.cloudflare.com/ajax/libs/react/0.14.3/react-dom.js'></script>	<!--Source React DOM-->\n \
        <script src='https://unpkg.com/babel-standalone@6.15.0/babel.min.js'></script>		        <!--Source JSX-->\n \
        <title>HTML Template</Title>\n \
        <style>\n \
            html { \n \
		scroll-behavior: smooth; /*specifies whether to smoothly animate the scroll position, instead of a straight jump*/ \n \
		box-sizing: border-box;  /*include the padding and border in an element's total width and height. Default value: content-box*/ \n \
            } \n \
        </style> 	<!--If not using a .css stylesheet, put style element at the top of the document-->\n \
        </head>\n \
        <body>\n \
        <header></header>\n \
        <nav></nav>\n \
        <main>"+defaultText+"</main>\n \
        <footer></footer>\n \
        <script></script> <!--If including any JavaScript, place it at the bottom of the document, before the closing /body tag-->\n \
        </body>\n \
        </html>"	
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

if __name__ == "__main__":
    root= tk.Tk()
    App = htmlTemplate(root)
    root.mainloop()
