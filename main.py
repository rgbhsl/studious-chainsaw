#YOURE NOT SUPPOSED TO BE HERE.
import time 
import random
chances = 0

def lal():
    #Leave A Line, to save time. has no substantial effect in the game
    print(" ")

#YOURE NOT SUPPOSED TO BE LOOKING AT MY CODE.
def start():
    print("Welcome to the Python tutorial!")
    print("Lesson 1 - Print")
    x = input("Begin? y/n ")
    if x == "y":
        print("Great! Let's begin.")
        gamebegin()
    elif x == "n":
        n = 0
        while n != 10:
            print("You're not supposed to choose that.")
            n = n + 1
        anotherchance()
        start()
    else:
        print("Follow instructions. Pick ONLY y or n")
        anotherchance()
        start()

def anotherchance():
    synonyms = ["wrong", "incorrect", "not right", "not correct", "a mistake", "an error", "disappointing", "inaccurate"]
    phrword = random.choice(synonyms)
    global chances
    chances = chances + 1
    if chances < 5:
        print(f"That's {phrword}. Let's try again.")
        print("...")
    elif chances == 5:
        print("You just never listen, don't you?")
        print(f"That was {phrword}. You didn't follow my instructions. Try again.")
        print("...")
    elif (chances > 5) and (chances < 9):
        print("Cut it out. You're not listening on purpose.")
        print(f"It's {phrword}. It's {phrword}. Stop that.")
    elif chances == 10:
        print("I'VE ASKED OVERAND OVR")
        print("FOLOW MYI NSTRUCTIONS .")
        print("DONTDO THSI TO M<E :(")
    elif chances > 10:
        ending1()

def ending1():
    lal()
    print("...")
    print("You'll never listen.")
    print("You're so cruel to me. I don't want to help you anymore.")
    time.sleep(2)
    lal()
    print("Ending I")
    print("You achieved this ending by making more than 10 mistakes.")
    x = input("Enter anything to begin again! ")
    lal()
    n = 0
    while n < 15:
        print('\033[0;31m'"YOU CAN'T BEGIN AGAIN. YOU DON'T DESERVE A SECOND CHANCE.")
        lal()
        n = n + 1
    quit()

def gamebegin():
    lal()
    print("The first thing most beginners learn to program is a simple output.")
    print("'Hello, world' is a test program that's been used for decades.")
    lal()
    print("Type the command below. Type exactly as it is written.")
    print("print(\"Hello, World!\")")
    x = input()
    if x == """print("Hello, World!")""" :
        helloworld()
    else:
        lal()
        print("I just told you to type exactly as is written.")
        anotherchance()
        gamebegin()

def helloworld():
    lal()
    print("Brilliant!")
    print("You can use print() to write so many things!")
    print("Like integers, strings, characters...")
    print("Which brings us to lesson 2: datatypes!")
    hellotodata()

def hellotodata():
    #transition function between helloworld() and datatypes()
    print("Lesson 2 - Datatypes")
    x = input("Begin? y/n ")
    if x == "y":
        print("Great! Let's begin.")
        gamebegin()
    elif x == "n":
        n = 0
        while n != 10:
            print("You're not supposed to choose that.")
            n = n + 1
        anotherchance()
        hellotodata()
    else:
        print("Follow instructions. Pick ONLY y or n")
        anotherchance()
        hellotodata()



start()