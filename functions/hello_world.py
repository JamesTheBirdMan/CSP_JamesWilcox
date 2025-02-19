# James Wilcox, Update Hello World Python



def hello(number):
    speech = input(f"What is name #{number}:\n")
    return speech

name1 = hello("1").capitalize()
name2 = hello("2").capitalize()
name3 = hello("3").capitalize()
name4 = hello("4").capitalize()
name5 = hello("5").capitalize()
print(f"Hello, {name1}, it is nice to meet you!")
print(f"Hello, {name2} and {name1}, it is nice to meet you!")
print(f"Hello, {name3}, {name2}, and {name1}, it is nice to meet you!")
print(f"Hello, {name4}, {name3}, {name2}, and {name1}, it is nice to meet you!")
print(f"Hello, {name5}, {name4}, {name3}, {name2}, and {name1}, it is nice to meet you!")