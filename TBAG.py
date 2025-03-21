# James Wilcox and Cairo Taylor, Text-Based Adventure Game
import random
count = 0
imbo = 0
option1 = "Go through the Hamster Tube Slide"
option2 = "Walk on the Glass Bridge"

while imbo < 0:
    print("...\n.....\nAfter waking up, you feel a little pad under you. Curious, you want to check around. After a moment of looking around, you notice you are in a giant bird cage, hanging above a lake of lava.\n") # By Cairo
    print("You can also see a slide made out of giant hamster tubes that spirals down into the darkness beneath the lava.")
    print("You can see the glass bridge from Squid Game...\n It seems to go on forever!")
    1mbo +=1

def actions(options):
    whichway = 0
    print("You have 2 options from here:\n")
    print(option1)
    print(option2)
    whichway = input("Which way do you go? (1 or 2)\n")
    print(whichway)
    

if whichway == 2:
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
                break
else:
    print("You slide down the tube.\n It smells like cat pee.")