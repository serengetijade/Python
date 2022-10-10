#OS MODULE
import os;
#print(dir(os));
#print(help(os));

#comment out this section: 
print("Get the current working directory cwd file path:");
print(os.getcwd());

#OPEN COMMANDS
#print(help(open));
print("\nOPEN COMMANDS");

#READ A FILE
print("\nREAD A FILE");
with open('TestOS.txt', 'r') as file:
    data = file.read()
    print(data)
    file.close();

#APPEND TO A FILE
print("\nAPPEND TO A FILE");
def functionWriteData():
    data = "\nHello World!"
    with open('TestOS.txt', 'a') as file:
        file.write(data)
        file.close();
#Print to the screen what was appended    
def functionOpenFile():
    with open('TestOS.txt', 'r') as file:
        data = file.read()
        print(data)
        file.close();

#OS PATH()
print("\nOS PATH()");
fileName = "Hello.txt";

filePath = "C:\\Users\\jad24\\Documents\\Coding Projects\\Assignments&Notes\\";

variableFP = os.path.join(filePath, fileName);
print(variableFP);

#SEARCH A DIRECTORY FOR CERTAIN FILE TYPE OR OBJECT
print("\nCHECK A FOLDER FOR CERTAIN FILE TYPES");
import os, time;
from datetime import datetime;

CheckFor = input("What file do you wish to check for?\nPlease enter a file name or or extensions:\n>>> ");
Path = "C:\\Users\\jad24\\Documents\\Coding Projects\\Assignments&Notes\\sampleDirectory";
def functionSearchFiles():
    ListDir = os.listdir(Path)
    found = False
    for i in ListDir:
        if i.endswith(CheckFor):
            FullPath = os.path.join(Path,i);
            print(i + " Time of last modification: " + str(datetime.fromtimestamp(os.path.getmtime(FullPath))))
            found = True
    if not found:
        print("There were no search matches");        

#SEARCH A DIRECTORY FOR CERTAIN FILE TYPE OR OBJECT USING FILTER METHOD
CheckFor = input("What file do you wish to check for?\nPlease enter a file name or or extensions:\n>>> ");
Path = "C:\\Users\\jad24\\Documents\\Coding Projects\\Assignments&Notes\\sampleDirectory";
ListDir = os.listdir(Path)

def functionFilterMethod(i):
    if i.endswith(CheckFor):
        return True
    else:
        return False;
    
SearchListDir = filter(functionFilterMethod, ListDir);

for i in SearchListDir:
    FullPath = os.path.join(Path,i);
    print(i + " Time of last modification: " + str(datetime.fromtimestamp(os.path.getmtime(FullPath))));

#Select which functions you want to run:
if __name__=="__main__":
    #functionWriteData()
    #functionOpenFile()
    functionSearchFiles();
    #functionFilterMethod(i);
