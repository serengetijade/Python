#Add a comment by starting a line with #
#This is a comment. Remember that it is very important to comment your code thoroughly.
#or Add a comment to a codeblock via a docstring: __doc__

def functionName():
    """This is a docstring of this function"""
    return statement;
print(functionName.__doc__);


print('Hello World')

#data type()
print(type("Hello"));
print(type((3<2)));

#bool()
print(bool(5<1));

#isinstance() returns True if the specified object is of the specified type, otherwise False.
print(isinstance("Hello", str));
      
##FUNCTION BASICS
print('''
FUNCTION BASICS''');
def functionBasics(parameter1, parameter2): #name a function and parameters
    variableResult= parameter1 + parameter2
    print("The answer is {}.".format(variableResult));

functionBasics(2,4);

variableCallFunction = functionBasics;
variableCallFunction(2,5);

##STRING METHODS
print('''
STRING METHODS''');
myString = "Hello World";
print(myString);
print(len(myString));   #Count the number of characters in an object.
print(myString[1]);     #Remember that python index starts at 0 ZERO

#strings with .format example1
fname = "Jade"
lname = "Abreu"

print(fname + " " + lname); #Concatenate
print("Hello {} {}, welcome to Python".format(fname, lname));

#string with .format example2
stringVariable = "I love the color";
listVariable = ["red", "green", "blue", "yellow", "pink", "black"];
import random;

def functionName1():
    print(listVariable[0]);

def functionName2():
    print("{} {}".format(stringVariable, listVariable[(random.randint(0,5))]));
    
def functionName3():
    for i in listVariable:
        print("{} {}".format(stringVariable,i));
    
functionName1(); #call the function
functionName2();
functionName3();

#multiline string with triple '''
multilineStringVariable = '''Dear Alice,

Please follow the White Rabbit, it will lead to afternoon tea.

Sincerely,
The Red Queen
'''
print(multilineStringVariable);

print("Slice a string: " + multilineStringVariable[20:43]); #slice()

print("What is the length of a string? Use len(): " + str(len(multilineStringVariable)));

stringVariable = "Alice went underground anyway.";
print(stringVariable.strip('anyway.')); #strip()
print(stringVariable.upper()); #upper()
print("Alice\'s day turned into quite the adventure.")   #escape character \

##LIST AND TUPLE METHODS
print('''
LIST AND TUPLE METHODS''');
animal = ("Zebra", "Alligator", "Giraffe", "Goat", "Ox");
listofAnimals = list(animal);
listofAnimals.append ("Honey Badger");
print(listofAnimals);
print("Index 2: " + animal[2]); #select an object at a given index position. This is called a "slice".
for i in listofAnimals:     #print all objects in a list
    print(i);
print(len(listofAnimals));  #count the number of elements in a list
print(listofAnimals.count("Alligator"));    #count how many times a given value appears on a list

stringTuple = "A string object is considered a tuple";
newString = list(stringTuple);
newString = stringTuple.split(" "); #Separate a string into objects, using a " " blank space as the division mark to identify objects.
print(newString);

concatenatedList = listofAnimals + newString;   #concatenate works with strings
print(concatenatedList);

newString.reverse();
print(newString);

stringTuple2 = "Python";
print(len(stringTuple2));
for i in enumerate(stringTuple2):
    print(i);

##SET METHODS
print('''
SET METHODS''');
setName1 = {"objectA", "objectB", "objectC", "objectD"};

setName1.add("objectE");
setName1.remove("objectB");
print(setName1);
#Return a set that contains the items that only exist in set 1, and not in set 2:
setName2 = {"objectD", "objectB"};
setDifference = setName1.difference(setName2);
print(setDifference);

##DICTIONARY METHODS
print('''
DICTIONARY METHODS''');
dictionary1 = {"index0":1, "index1":2, "index2":3}
print(dictionary1["index0"]);

#change a value
dictionary1["index2"]=4;  

#add a key value pair
dictionary1["index3"]=5;
print(dictionary1);

#assign a variable (or print) using .get() method
variableName = dictionary1.get("index1");   
print(dictionary1.get("index1"));

dictionary2 = {
    "emp_1234": {"fname": "Bob", "lname":"Smith","phone":"123-456-7890"},
    "emp_1235":{"fname":"Mary", "lname":"Jones", "phone":"432-123-4567"}};
print(dictionary2["emp_1235"]);
print(dictionary2["emp_1234"]["phone"]); #call a value from an inner dictionary

print("User: {} {}\nPhone: {}"
    .format(
    dictionary2["emp_1235"]["fname"],
    dictionary2["emp_1235"]["lname"],
    dictionary2["emp_1235"]["phone"]));

#create a dictionary using a list via fromkeys()
keysListName = ('key1', 'key2', 'key3');
values = 0;
dictionary3 = dict.fromkeys(keysListName, values)

print(dictionary3);

##ARRAY METHODS
print('''
ARRAY METHODS''');
variableArray = ['value1', 'value2', 'value3', 'value4'];
print(type(variableArray));
variableString = "Bob";
print(type(variableString));

##BASIC MATH WITH VARIABLES
print("\nBASIC MATH WITH VARIABLES"); #\n prints string on a new line
print(4+10)

num1 = 4;               #instantiate a variable by defining it with =
num2 = 5;
print(type(num1));      #what is the data type?

num3 = num1 + num2;     #Use variables in math
print(num3);

num1 = 1.2;             #Because python is an interpreted language, you can reassing variable values.
num2 = 2.1;

print(num1 + num2);

#MATH Module
print("\nMATH MODULE");
#you must import a method before you can use it!
import math;

print(math.floor(3.56));

#LAMBDA FUNCTIONS
print('''
LAMBDA FUNCTIONS''');
def multiply(i):
    return i*i;
print(multiply(3));

y = lambda x: x * x * x;
print(y(20));

z = lambda a: a +10;
print(z(5));

#lambda function with multiple variables:
x = lambda a, b, c : a + b + c;
print(x(5, 6, 2));

#OPERATORS
print('''
OPERATORS''')
print("879 / 5 = " + str(879/5));
print(879%5);           #arithmetic operator: modulus returns any leftover
print(879//5);          #arithmetic operator: floor division rounds down to the nearest whole number
x = 879;                #define a variable
x /= 5;                 #assignment operator
print(x);   
print(879>5);           #a comparison operator
print(5 == 5);          #== compare for equality. This will return a boolean statment: True
print(879 != 5);        #!= =is not

if 879>5 and 5>4:
    print("The statements is TRUE");

a=60;
b=13;
c=0;

#bitwise operator
c = a & b;
print ("Line 1-Value of c is " + str(c));

##IF ELSE STATMENTS
print('''
IF ELSE STATEMENTS''');

if 5 > 1 and 1 < 10:
    print("Both conditions are True")
else:
    print("Both conditions are False");

#example2 AND with a Boolean Value
number1 = 12;
key = True;

if number1 == 12:
    if key:
        print("Num1 is equal to 12 and they have the Key")
    else:
        print("Num1 is equal to 12 but they don't have the Key")
elif number1 > 12:
    print("Num1 is larger than 12")
else:
    print("Num1 is not equal to 12");

#if in | if not in functions
listOfObjects =["item1", "item2", "item3", "item4"];

if "item2" in listOfObjects:
    print("Yes");
if "item5" not in listOfObjects:
    print("Also Yes");

##CREATE A MODULE
print("\nCREATE A MODULE");
#def getNumbers(num1, num2):
#    results = num1 * num2
#    return results;
#if __name__ == "__main__":
#    pass


#Syntax to use a function from another module: createdModule.functionName(parametersIfAny)
import createdModule;
if __name__ == "__main__":
    results = createdModule.moduleName(5, 9)
    print(results); 

#INPUTS
print("\nINPUTS");
#basic input
variableInput1 = input("Enter the prompt here, such as \"What is your name?\"\n>>> "); #use an escape sequence to have the input start on the next line

#Normalize an input using various string methods
variableInput2 = input("With .capitalize, whatever entered will return with only the first letter capitalized").capitalize();
print("Ta da...: {}".format(variableInput2));

input("Press Enter to continue");

#LOOPS
print("\nLOOPS");
print("Start counting from i=0");
#for loop
i = 0;
for i in range(10):
    print("{} iteration(s) through the loop.".format(i))
    i += 1;
else:                   #optional else statement
    print("The loop is ended");

#for loop + break statement: end a loop at a given condition
variableName = ["array1", "array2", "array3", "array4", "array5", "array6", "array7"];
for x in variableName:    
    if x == "array6":
        break
    print(x);

#for loop + continue statement "skips" a given condition
variableName = ["array1", "array2", "array3", "array4", "array5", "array6", "array7"];
for x in variableName:    
    if x == "array1":
        continue
    elif x == "array2":
        continue
    print(x);

#For loop to ADD together all the elements in a list, array, or dictionary
def functionName():
    variableName = {"element0": 120, "element1": 1200, "element2": 60, "element3": 75, "element4": 65}
    variableTotal = 0
    for i in variableName:
        variableTotal += variableName[i]
    variableGrandTotal= "The total of all the elements is: {}".format(variableTotal)
    return variableGrandTotal;

#while loop
i= 0; 
while i < 10:
    print("{} interation(s) through the loop.".format(i))
    i += 1
else:
    print("An else statement is optional");

#while loop + break statement: end a loop at a given condition
i= 0;
while i < 10:
    print("{} is less than 10".format(i));
    if i == 3:
        break
    i += 1
else:
    print("An else statement with a while loop only prints when the variable didn't meet the conditions to begin with.");

#while loop + continue statement "skips" a given condition
i = 0;
while i < 5:
    i += 1;
    if i == 3:
        continue
    print(i)
else:
    print("A continue statements 'skip' a given condition");

##.format FUNCTIONS WITH PARAMETERS AND ARGUMENTS
print('''
.format FUNCTIONS WITH PARAMETERS AND ARUGMENTS''');
variableString = "loves the color"
variableList = ["red", "green", "blue", "yellow", "pink", "black"];

print("Iterate through all objects in a list:");
def functionName11(variableName):
    for i in variableList:
        print("{} {} {}".format(variableName,variableString,i));

functionName11("Daniel"); #call the function and pass in a parameter

print('''
Return statment INSIDE loop returns first object in the array:''');
#whereas return statement OUTSIDE loop returns the last object in the array
def functionName12(variableName):
    for i in variableList:
        variableReturn = "{} {} {}".format(variableName,variableString,i)
        return variableReturn;

print(functionName12("Sam"));   #call the function and pass in a parameter

print('''
Return ALL objects in the array via .append:''');
def functionName13(variableName):
    variableToAppend = []       #define an empty list- this tells python that this variable has a data type of list
    for i in variableList:
        variableReturn = "{} {} {}".format(variableName,variableString,i)
        variableToAppend.append(variableReturn)
    return variableToAppend;    #must be OUTSIDE the for loop or it will only return the first object the array

print(functionName13("Jane"));
print('''Then to iterate through and print each result:''')
variableListIteration= functionName13("Jane");
for i in variableListIteration:
    print(i);

print('''
.format() can also define an object's data type''');
variableINT = format(1234,'%');
print(variableINT);

print("binary: {0:b}, hexadecimal: {0:x}, percentage {0:%}".format(2));

##FUNCTIONS WITH INPUT VALUES
print('''
FUNCTIONS WITH INPUT VALUES''');

def functionUseInput():
    variableInput = input("What is your name?") #create a variable from an input
    variableNewList = functionName13(variableInput) #create a variable to call another function
    for i in variableNewList:   #Iterate through all elements in an object
        print(i)
#To call:
#functionUseInput();

#require an input               #review loops with boolean data types above
def functionUseInput2():
    go = True
    while go:
        variableInput = input("What is your name?")
        if variableInput == "":
            print("Please provide an input")
        elif variableInput =="value":
            print("Elif message or other function/statement")
        else:
            go = False
    variableNewList = functionName13(variableInput)
    for i in variableNewList:
        print(i)

functionUseInput2();

##DATETIME MODULES
print("\nDATETIME MODULE");

import datetime
from datetime import datetime

x = datetime.datetime.now()
print(x);

#Simple Counter: 
#for counter in range(1,11):
#   print(counter)
#   time.sleep(.5)

##RANDOM MODULE
import random

print(random.randint(1,50));    #print a random integer between 1 and 50

##GET CURRENT WORKING DIRECTORY CWD FILE PATH
print("\nGET CURRENT WORKING DIRECORY CWD FILE PATH");
import os;
print(os.getcwd());

##*ARGS ARGUMENTS
def functionArgs(*args):
    for arg in args:
        print(arg);

functionArgs("This is an an example of args:", "string", "and then an integer", 5);

##**KWARGS KEYWORD ARGUMENTS
def functionKwargs(**kwargs):
    print("kwargs:", kwargs);

functionKwargs(first = "1", second = "2", third = "3")   
