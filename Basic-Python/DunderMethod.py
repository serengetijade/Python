#DUNDER METHODS
def functionDunder():
    variableName = (__name__)  #__name__ = the name of the document
    return variableName;

print(functionDunder());
#Result: __main__

#Dunder init Method Example 1
class name: 
    def __init__(self, firstName, lastName):
        #Initializing values for future objects created from this class
        self.firstName = firstName
        self.lastName = lastName
    def printName(self):
        print("Hello, I am {0} {1}.".format(self.firstName, self.lastName));

#Pass in the object values later:
person = name('Dustin', 'Smith');
person.printName();

#Dunder init Method Example 1
class functionName: 
    def __init__(self, parameterA, parameterB):
        #Initializing values for future objects created from this class
        self.variableA = parameterA     #variableA and parameterA usually share the same name
        self.variableB = parameterB     #variableB and parameterB usually share the same name
    def functionName2(self):
        print("Hello, I am {0} {1}.".format(self.variableA, self.variableB));

#Pass in the object values later:
variableName = functionName('Jade', 'A');
variableName.functionName2();

#Dunder __name__ method
import createdModule;

def print_app():
    name = (__name__)
    return name;

if __name__ == "__main__":
    #The following is calling code from within thes script
    print("I am running code from {}".format(print_app()))
    #The following is calling code from the imported DunderMethod2
    print("I am running code from {}".format(createdModule.functionDunder()))
    
