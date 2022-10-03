##PROTECTED OBJECT

class Protected:                #Define a class and name it
    def __init__(self):         #Assign the value of 'self' to each instance when the object is created
        self._protectedVar = "value1";  #Further declare that 'self' is a protected value, and assign it a value of 'value1'.

obj1 = Protected()              #Instantiate the function, and name this instance 'obj1'
obj1._protectedVar = "newValue1"    #Change the value of obj1- you must recall it as obj1._protectedVar
print(obj1._protectedVar);

##PRIVATE OBJECT
class PrivateClass:             #Define a class and name it
    def __init__(self):         #Assign the value of 'self' to each instance when the object is created
        self.__privateVar= "value2" #Furter declare that 'self'is a protected object, and assign it a valeu of 'value2'.

    def getPrivate(self):       #Define a function and pass in 'self' to indicate that the instance to affect is the one named 'self'.
        print(self.__privateVar)
  
    def setPrivate(self, privateValue): #Define a function and pass in 'self' to indicate that the instance to affect is the one named 'self'. 'privateValue' is a placeholder within the function.
        self.__privateVar = privateValue    #privateValue (the parameter that is acting as a placeholder), when it is called in line 23, changes the value of the (protected) object.

obj2 = PrivateClass()		#retrieve the data of the private variable
obj2.setPrivate("newValue2")	#set a new value to the private variable:
                                #Pass in 'newValue2' as the parameter, which then passes into the funciton setPrivate as 'privateValue'(a placeholder within the function).
obj2.getPrivate()		#Result: newValue
