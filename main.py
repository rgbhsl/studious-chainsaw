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
            print("You're not supposed to choose that.")
            n = n + 1
        anotherchance()
    else:
        print("Follow instructions. Pick ONLY y or n")
        anotherchance()
        start()

def anotherchance():
    synonyms = ["wrong", "incorrect", "not right", "not correct", "a mistake", "false", "an error", "disappointing", "inaccurate"]
    phrword = random.choice(synonyms)
    global chances
    chances = chances + 1
    if chances < 5:
        time.sleep(1)
        print(f"That's {phrword}. Let's try again.")
        print("...")
        time.sleep(0.5)
    elif chances == 5:
        time.sleep(0.7)
        print("You just never listen, don't you?")
        print(f"That was {phrword}. You didn't follow my instructions. Try again.")
        print("...")
        time.sleep(0.5)
    elif (chances > 5) and (chances < 9):
        time.sleep(0.3)
        print("Cut it out. You're not listening on purpose.")
        print(f"It's {phrword}. It's {phrword}. Stop that.")
    elif chances == 10:
        print("I'VE ASKED OVERAND OVR")
        print("FOLOW MYI NSTRUCTIONS .")
        print("DONTDO THSI TO M<E :(")
    elif chances > 10:
        print("...")
        print("You'll never listen.")
        print("You're so cruel to me. I don't want to help you anymore.")
        time.sleep(2)
        print("Ending I - ")
        print("You achieved this ending by making more than 10 mistakes.")
        print("Enter y to begin again")



def gamebegin():
    print("The first thing most beginners learn to program is a simple output.")
    print("'Hello, world' is a test program that's been used for decades.")
    print("Type the command below. Type exactly as it is written.")
    print("print("Hello, World!")")
    x = input()
    if x == "print("Hello, World!")" :
        helloworld()
    else:
        print("I just told you to type exactly as is written.")
        anotherchance()
        gamebegin()


def helloworld():
    print("Brilliant.")



start()