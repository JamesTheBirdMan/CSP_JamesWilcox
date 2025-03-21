# James Wilcox and Cairo Taylor, Text-Based Adventure Game
import random
count = 0
option1 = "Go through the Hamster Tube Slide"
option2 = "Walk on the Glass Bridge"

 print("...\n.....\nAfter waking up, you feel a little pad under you. Curious, you want to check around. After a moment of looking around, you notice you are in a giant bird cage, hanging above a lake of lava.\n") # By Cairo
    print("You can also see a slide made out of giant hamster tubes that spirals down into the darkness beneath the lava.")
    print("You can see the glass bridge from Squid Game...\n It seems to go on forever!")

def split(choice1, choice2):
    print(f"You have 2 pathways. Do you want to: \n{choice1},\nOR\n{choice2}?")

firstpick = split("1. Go down hampster tube slide", "2. Jump across the glass bridge")
choice = int(input("1 or 2:\n"))
if choice == 1:
    print("You decide to go down the hampster tube slide.")
else:
    print("You decide to go on the glass bridge.")
    count = 0
    while count != 26:
        strong = random.randint(1,2)
        panes = int(input("You are on the glass bridge. Pick 1 or 2."))
        if panes == strong:
            print("You have made it to the next pane.")
        else:
            print("You have fallen into the lava.\nYou lost!")
        

 while count <= 25:
    strong = random.randint(1,2)
        print("Pick 1 or 2. One panel will make you fall into lava, while the other will allow you to continue.")
     print(strong)
     choice = input("So, Which do you choose? 1 or 2? ")
         if strong == 1 and choice == 1 or strong == 2 and choice == 2:
            print("You chose the right pane!\n")
            count += 1
            else:
                print("Oh no! You chose the wrong glass pane! The glass shatters under your feet as you jump on it, resulting in you falling into the lava.\nYou lost!")