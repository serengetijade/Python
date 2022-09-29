#CLASS BASICS

"""
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
instanceName= className();

#Call the login method using the new object
instanceName.login();

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

"""

##CHILD CLASS POLYMORPHISM
#parent class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None             #Data type is "nothing"
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True     #boolean value

    def information(self):  #self is a keyword
        message = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name, self.species, self.legs, self.arms, self.dna, self.origin, self.carbon_based)
        return message;

#child class #1
class Human(Organism):      #inherit the parent class: (parentName)
    name = "MacGuyver"      #can change attribute values in a child class
    species = "Homo Sapien"
    legs = 2
    arms = 2
    origin = "Earth"

    def ingenuity(self):   #a method of this class
        message = "\nCreate a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!"
        return message;
    
#child class #2    
class Dog(Organism):
    name = "Spot"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = "Earth"
    weakness = "Treats"     #can add additonal attributes to children
    special_ability = "Cuteness"

    def addMessage(self):   
        message = "Weakness: {}\nSpecial Ability: {}".format(self.weakness, self.special_ability)
        return message;
        
    def bite(self):         #a method of this class
        message = "\nEmit a loud, menacing growl and bite down ferociously on target."
        return message;

#child class #3
class Virus(Organism):
    name = "SARS-CoV-2"
    species = "Virus"
    legs = 0
    arms = 0
    dna = "Sequence C"
    origin = "Mars"
    cure = "TBD"
    target = "Homo sapiens"

    
    def information(self):  #use polymorphis to change functions that may also be in the parent function
        message = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}\nCure: {}\nTarget: {}".format(self.name, self.species, self.legs, self.arms, self.dna, self.origin, self.carbon_based, self.cure, self.target)
        return message;
    
    def replication(self):  #a method of this class
        message = "\nThe virus is highly contagious and can pass via airborn particles."
        return message;
    
#instantiate objects
if __name__ == "__main__":
    #pass                  #run nothing
    human = Human();        #instantiate Human() and give in the name 'human'
    print(human.information());
    print(human.ingenuity());

    dog = Dog();
    print(dog.information());
    print(dog.addMessage());
    print(dog.bite());
    
    virus = Virus();
    print(virus.information());
    print(virus.replication());
        

