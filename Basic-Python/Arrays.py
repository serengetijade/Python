#ARRAY METHODS
print('''ARRAY METHODS''');

#Define an array:
variableArray = ["object1", "object2", "object3", "object4", "object5", "object6"];
print("The array object: " + str(variableArray));

#Add an object to the end of an array via .append()
variableArray.append("object7");

#Delete an object from an array via .remove()
variableArray.remove("object1");

#Delete an object from an array via del
del variableArray[3];   #delete the object at index 3- but remember it starts counting from 0

#Replace an object at a given index location:
variableArray[1] = "replaced Object";

#Now the current array is: ['object2', 'replaced Object', 'object4', 'object6', 'object7']
print("The modified array:" + str(variableArray));

print('''
Iterate through each element within an object:''');
for i in variableArray:
    print(i);
#Count() returns how many times a given 'value' appears within an object:
variableCount = variableArray.count("object2");
print(variableCount);

print('''
Sort arrays using .sort():''');
#sort descending:
variableArray.sort(reverse=True);
print(variableArray);

#sort by length of values:
def functionSortLength(n):
    return len(n);
variableArray.sort(key=functionSortLength);
print(variableArray);

#Use an element from an array as a wildcard via .format
import random;
def functionUseWildCard():
    variableList = ["a conversation", "directions", "help with their cat stuck up a tree", "donations", "a free hug", "talk of the Lord", "help socializing their puppy"]
    indexNumber = len(variableList)-1
    wildCard = variableList[(random.randint(0,indexNumber))];
    return wildCard;

print("Use a wild card for {}.".format(functionUseWildCard()));
