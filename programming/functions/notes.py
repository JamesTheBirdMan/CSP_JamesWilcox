# James Wilcox, Functions Notes Python

# Function is an action stored in a keyword
number = int(input("Can I get a number:\n"))
def add(numOne, numTwo):#parameters go in the parentheses separated by commas
    numOne = int(input("Give me a number:\n"))
    numTwo = int(input("Give me a number:\n"))
    print(numOne+numTwo)

#add(2, 4)# arguments are given when the function is called, AND must match the number of parameters
#add(7, 21)

def user(word):
    return input(f"Tell me a {word}:\n")

name = user("name")
verb = user("present-tense verb")
place = user("place")
print(f"{name} was {verb} and somehow got to {place}.")