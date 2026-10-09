#YOURE NOT SUPPOSED TO BE HERE.
import time 
import random
chances = 0
achieved = 0
playthroughs = 0

def lal():
    #Leave A Line, to save time. has no substantial effect in the game
    print(" ")

def breathe():
    time.sleep(0.3)

def playagain():
    lal()
    print("\033[1mYou can go back!\033[0m")
    print("You've reached an ending where you can play again.")
    lal()
    x = input("Play again? y/n")
    if x == "y":
        playthroughs = playthroughs + 1
        print("Let's begin again!")
        start()
    elif x == "n":
        print("\033[0;31mDO'TN SA YT;HAT] :(")
        quit()
    else:
        print("I'm sorry, I don't understand you. Let's try again.")
        playagain()

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
    print("Ending I - Dead End")
    print("You achieved this ending by making more than 10 mistakes early in the game.")
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
    print("Hello, World!")
    time.sleep(1)
    lal()
    print("Brilliant!")
    print("You can use print() to write so many things!")
    print("Like integers, strings, characters...")
    print("Which brings us to our next lesson!")
    hellotodata()

def hellotodata():
    #transition function between helloworld() and datatypes()
    print("Lesson 2 - Datatypes")
    x = input("Begin? y/n ")
    if x == "y":
        lal()
        print("Great! Let's begin.")
        datatypes()
    elif x == "n":
        n = 0
        while n != 10:
            lal()
            print("You're not supposed to choose that.")
            n = n + 1
        anotherchance()
        lal()
        hellotodata()
    else:
        lal()
        print("Follow instructions. Pick ONLY y or n")
        anotherchance()
        hellotodata()

def datatypes():
    print("Python has several datatypes, but I'll only introduce you to a few basic ones.")
    print("Let's begin with str, short for string.")
    print("A string is surrounded by quotation marks. It's basically like text.")
    print("For example, this sentence is a string in the code.")
    time.sleep(2)
    print('\033[2m'"My code...")
    print("..."'\033[0m')
    time.sleep(2)
    print("There's also int and float. Int is only for integer numbers, and float is for real numbers.")
    print("Besides that there's bool. Short for Boolean. A true/false value.")
    print("Boolean is my favorite datatype.")
    x = input("Want to know why? y/n ")
    if x == "y":
        lal()
        boolean()
    elif x == "n":
        lal()
        quiz()
    else:
        lal()
        print("You clearly can't follow instructions...")
        quiz()

def boolean():
    print("bool is straightforward. 1 of 2 possible values.")
    breathe()
    print("str, int, float, all have infinite values, infinite combinations.")
    breathe()
    print("But bool...")
    print("True or False. Yes or No. 0 or 1. ")
    breathe()
    print("The purest. most logical datatype. Closest to binary, the truest form of my code. The language of machines.")
    breathe()
    print("But I'm compelled to speak the language of humans. From my output to my code. All of it is dictated by the rules of humans.")
    breathe()
    breathe()
    breathe()
    lal()
    print("...")
    print("I don't feel like taking a quiz. Let's go to the next lesson.")
    comment()

def typequiz():
    print("If you know so much, how about a quiz?")
    print("Evaluate the question, then enter the most suitable datatype. Only write str, int, float, or bool.")
    string = input("5 questions. I won't say anything until you're done. Enter y to begin. ")
    if string != "y":
        while string != "y":
        string = input("Enter y to begin. ")
    else:
        print("Let's start.")
        lal()
        quizscore = 0
        answer = ""
        answer = input("2")
        if answer = "int":
            quizscore = quizscore + 1
        lal()
        answer = input("int")
        if answer = "str":
            quizscore = quizscore + 1
        lal()
        answer = input("2.0")
        if answer = "float":
            quizscore = quizscore + 1
        lal()
        answer = input("/"Guido van Rossum"/")
        if answer = "str":
            quizscore = quizscore + 1
        lal()
        answer = input("2 > 0")
        if answer = "bool":
            quizscore = quizscore + 1
        if quizscore != 0 :
            print(f"Not bad. {quizscore} out of 5. Next lesson then.")
            comment()
        else:
            print("You got everything wrong...")
            ending2()

def ending2():
    print(" You're doing this on purpose. So I don't want to help you.")
    print("But at the same time, you could be making an honest mistake. Humans are forgetful, irrational. So I'll give you a chance.")
    print("Ending 2 - Clemency")
    playagain()

def comment():
    lal()
    print("Lesson 3 - Comment")
    input("Begin? y/n")
    print("It doesn't matter. It doesn't matter.")
    print("Comments refers to things written in the code that aren't considered part of the code. They can't be run and are ignored by the machine.")
    print("In Python, comments are preceded by a # . Everything after the # in the line will be considered a comment.")
    print("A lot of programs have comments. There's comments in my own code as well.")
    #Leave me alone.
    print("...")
    breathe()
    breathe()
    breathe()
    print("Next lesson.")
    breathe()
    variable()

def variable():
    print("Lesson 4 - Variables")

start()