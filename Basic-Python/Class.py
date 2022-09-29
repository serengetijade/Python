#CLASS BASICS

#DEFINE A CLASS WITH ARGUMENTS
class className:
    #Define the attributes of the class
    attribute0 = "value"	    #←value may be something like “Name”
    attribute1 = "value"	    #←value may be something like “Email”
    attribute2 = "value"	    #←value may be something like “Password”
    attribute3 = 42	            #←value may be something like “Account#”

    #Define the methods of the class while indented at the same level as the attributes
    def login(self):
        input_email = input("Enter your email: ")
        input_password = input ("Enter your password: ")
        if (input_email == self.attribute1 and input_password == self.attribute2):
            print("Welcome back, {}!".format(self.attribute0))
        else:
            print("You shall not pass!!!!");

#Create a class instance
new_user = className();

#Call the login method using the new object
new_user.login();

#DEFINE A CLASS WITH __init__
#First, define a class as you would above.
#The def __init__() needs to be at the same indentation level as the attributes of the class so that it will be part of the class definition.
class className2:
    #Define the attributes of the class
    attribute0 = "value"	    #←value may be something like “Name”
    attribute1 = "value"	    #←value may be something like “Email”
    attribute2 = "value"	    #←value may be something like “Password”
    attribute3 = 42	            #←value may be something like “Account#”

    #Define the __init_funcgtion after the class definition        
    def __init__(self, attribute0, attribute1, attribute2, attribute3):
        self.attribute0 = attribute0
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = attribute3
        
    #Define the methods of the class while indented at the same level as the attributes
    def login(self):
        input_email = input("Enter your email: ")
        input_password = input ("Enter your password: ")
        if (input_email == self.attribute1 and input_password == self.attribute2):
            print("Welcome back, {}!".format(self.attribute0))
        else:
            print("You shall not pass!!!!");

#Create a class instance
newInstance2 = className2("attribute0value", "attribute1value", "attribute2value", "attribute3value");
#Call the login method using the new object
newInstance2.login();

#ADD A CHILD CLASS
class childClassName1(className):
    attribute4_1 = "value"      #added attributes are unique to this "child" class
    attribute5_1 = True
    
class childClassName2(className):
    attribute4_2 = "value"     #added attributes are unique to this "child" class
    attribute5_2 = 11


#ACCESS A CLASS INSTANCE:
class className3:
    attribute1 = "Hello"
    attribute2 = "World!";


if __name__ == "__main__":
    x = className3()        #Instantiate the class and name this instance
    print(x.attribute1+"!")
    print("{} {}".format(x.attribute1, x.attribute2))
