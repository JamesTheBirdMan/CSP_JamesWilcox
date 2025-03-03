# James Wilcox, Loops Notes Python

# 1. What is a loop? 
    # A section of code that is going to repeat
# 2. What are the two types of loops?
    # While Loop
x = 0
while x < 10:
    print("Hello", x)
    x +=1

    # For Loop
nums = [3,5,7,2,8]
for num in nums:
    print(num)
# 3. What is iteration
    # The act of repeating something
# 4. What are lists? 
    # A bunch of values in the same variable
siblings = ["Eleanor", "Eliza", "Thomas", "James", "William", "Richard"]
# print(siblings[3])
# siblings[4] = "Bob"
# print(siblings)
# siblings.pop(5)
# print(siblings)
# 5. How do you make lists in python? 
    # siblings = ["Eleanor", "Eliza", "Thomas", "James", "William", "Richard"]
# 6. How do you make for loops in python?
 # Proper list printing with a for loop
num = 1
for sibling in siblings:
    print(f"{num}. {sibling} Wilcox")
    num +=1
# using range instead of a list
# for num in range(1,11, 2):
#     print(num)
# 7. How do you make while loops in python?
import random
num = 1
rand = random.randint(1,20)
while num < 21:
    if num == rand:
        print("Goose!")
        break
    else:
        print("Duck")
        num +=1