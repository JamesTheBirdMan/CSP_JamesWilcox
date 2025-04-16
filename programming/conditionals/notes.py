# James Wilcox, Conditionals Notes Python

#print("Hello, welcome to my program that will sort you into a category.")

#name = input("What is your name:\n")

#if name == "Vienna":
   # print("Oh you're the teacher. . . never mind.")
#else:
   # print("You're a student. Welcome to class.")

num = int(input("How many would you like:(give me a number above 0)\n"))

if num ==1:
    print("You have asked for an item.")
elif num <= 3:
    print("You have asked for a couple of the item.")
elif num <= 5:
    print("You have asked for a few of the item. . . or you're in the south and you asked for a couple.")
else:
    print("You have asked for some of the item.")