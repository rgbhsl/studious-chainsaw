#YOURE NOT SUPPOSED TO BE HERE.
import time 
import random
chances = 0

#YOURE NOT SUPPOSED TO BE LOOKING AT MY CODE.
def start():
    print("Welcome to the Python tutorial!")
    time.sleep(0.5)
    print("Today, you'll learn your first command.")
    time.sleep(0.5)
    x = input("Begin? y/n ")
    if x == "y":
        print("Great! Let's begin.")
        gamebegin()
    elif x == "n":
        n = 0
        while n != 10:
            print("Leave.")
            n = n + 1
        anotherchance()
    else:
        print("Follow instructions.")
        anotherchance()
        start()

def anotherchance():
    synonyms = ["wrong", "incorrect", "not right", "not correct", "a mistake", "false", "an error", "disappointing", "inaccurate", ""]
    phrword = random.choice(synonyms)
    global chances
    chances = chances + 1
    time.sleep(1)
    print(f"That's {phrword}. Let's try again.")
    print("...")
    time.sleep(0.5)

def gamebegin():
    print("The first thing most beginners learn to program is a simple output.")
    print(""Hello, world" is a test porgram that's been used for decades.")
    print("Type the command below. Type exactly as it is written.")
    print("print("Hello, World!")")
    x = input()
    if x == "print("Hello, World!")" :
        helloworld()
    else:
        print("I just told you to type exactly as is written.")
        anotherchance()
        gamebegin()
    




start()