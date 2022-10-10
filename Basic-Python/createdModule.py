#CREATE A MODULE
#These modules are referenced by several documents to demonstrate basic Python concepts

#called in BasicPython.py
def moduleName(num1, num2):
    results = num1 * num2
    return results;

if __name__ == "__main__":
    pass


#called in DunderMethod.py:
def functionDunder():
    variableName = (__name__)   #__name__ = the name of the document
    return variableName;

if __name__ == "__main__":
    pass;

##ABSTRACTED METHODS

class ABC():                    #ABC stands for Abstract Base Class
    amount = 100
