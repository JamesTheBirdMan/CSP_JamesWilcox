# James Wilcox, Financial Calculator Update Python

def info(income, amount, type):
    pertype = amount/income*100
    print(f"You spend ${round(amount, 2)} on {type} and that is {pertype}% of your income")

print("Hello! This is a program for calculating your budget and finances!")
income =float(input("what is your monthly income?\n"))

rent = float(input("What is your monthly expense for housing?\n"))
utilities = float(input("What are your monthly expenses for utilities?\n"))
groceries = float(input("What are your monthly expenses for groceries?\n"))
transportation = float(input("What are your monthly expenses for transportation?\n"))

savings = float(income/10)
print("Every month you save $", savings)

spending = income - rent - utilities - groceries - transportation - savings
print("Every month you can spend $", spending)

info(income, rent, "rent")

info(income, utilities, "utilities")

info(income, groceries, "groceries")

info(income, transportation, "transportation")