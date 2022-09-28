#Python: 3.10.7
#
#Author: Jade Abreu
#
#Purpose:   A simple game
#           to demonstrate how to pass variables from function to function,
#           as well as other basic python concepts.
#
#           Remember, function_name(variable) means that we pass in the variable.
#           return_variable means that we are returnign the variable back to the calling funcion.
import time;
import random;

def start(nice=0, mean=0, name=""):
    #get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name);

def describe_game(name):
    """ check if this is a new game or not.
        If it is new, get the user's name.
        If it is not, that the playing again and continue.
    """
    if name != "":        
        time.sleep(.5)
        print("\nThank you for plaing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name?\n>>> ").capitalize()
                if name != "":
                    time.sleep(.5)
                    print("\nWelcome {}!".format(name))
                    time.sleep(.5)
                    print("\nIn this game, you will be greeted \nby several different people.\nYou can choose to be nice or mean.")
                    print("But at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name;      

def UseWildCard():
    variableList = ["a conversation", "directions", "help with their cat stuck up a tree", "donations", "a free hug", "talk of the Lord", "help socializing their puppy"]
    indexNumber = len(variableList)-1
    wildCard = variableList[(random.randint(0,indexNumber))];
    return wildCard;

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        time.sleep(.5)
        pick = input("\nA strager approaches you for {}.\nWill you be nice or mean?\nEnter N or M:\n>>> ".format(UseWildCard())).lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            time.sleep(.75)
            stop = False
        if pick == "m":
            print("\nThe stranger stares at you menacingly and storms off..")
            mean = (mean +1)
            time.sleep(.75)
            stop = False
    score(nice,mean,name); #pass the 3 variables to the score() function

def show_score(nice,mean,name):
    time.sleep(.5)
    print("\n{}, your current total is: \nNice: {}\nMean: {}".format(name,nice,mean));

def score(nice,mean,name):
    if nice > 2:
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name);

def win(nice,mean,name):
    print("\nNice job {}!\nEveryone loves you and you've made lots of friends along the way!".format(name))
    #win image
    from PIL import Image
    im = Image.open("YouWin.jpg")
    im.show()
    again(nice,mean,name);

def lose(nice,mean,name):
    print("\nSorry {}. \nYou didn't impress anyone with your attitude.".format(name))
    again(nice,mean,name);

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you wan't to play again?\nEnter Y or N:\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter Y for 'Yes', or N for 'No':\n>>> ");

def reset(nice,mean,name):
    nice = 0
    mean = 0
    start(nice,mean,name);

if __name__ == "__main__":
    start()
