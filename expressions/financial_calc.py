# James Wilcox, Financial Calculator Python

# Write a print statement telling the user what the program is (Budget Calculator)
print("Hello! This is a program for calculating your budget and finances!")
# Ask for monthly income (User input)
income =float(input("what is your monthly income\n"))

# Ask for monthly rent (User Input)
rent = float(input("What is your monthly expense for housing?\n"))
# Ask for monthly utilites (User Input)
utilities = float(input("What are your monthly expenses for utilities?\n"))

# Ask for monthly groceries (User Input)
groceries = float(input("What are your monthly expenses for groceries?\n"))

# Ask for monthly transportation (User Input)
transportation = float(input("What are your monthly expenses for transportation?\n"))

# Calculate savings as 10% of income
savings = float(income/10)
print("Every month you save ", savings)
# Calculate spending money income - (rent+utilities+groceries+transportation+savings) (variable)
spending = income - rent - utilities - groceries - transportation - savings
print("Every month you can spend", spending)

# Calculate percent of rent (rent/income)*100 (variable
rentpercent = ((rent/income)*100)

# Calculate percent of utilities (utilities/income)*100 (variable)
untilitiespercent = ((utilities/income)*100)

# Calculate percent of groceries (groceries/income)*100 (variable)
groceriespercent = ((groceries/income)*100)

# Calculate percent of transportation (transportation/income)*100 (variable)
transportationpercent = ((transportation/income)*100)

# Calculate percent of savings (savings/income (variable)*100
savingspercent = ((savings/income)*100)

# Calculate percent of spending (spending/income (variable)*100
spendingpercent = ((spending/income)*100)

# Tell user category spending amount and percent for rent ("You spend $XX.XX on rent and that is XX% of your income")
print("You spend $", rent, "on rent and that is %", rentpercent , "of your income")

# Tell user category spending amount and percent for utilities("You spend $XX.XX on groceries and that is XX% of your income")
print("You spend $", utilities, "on utilties and that is %", untilitiespercent, "of your income")

# Tell user category spending amount and percent for groceries("You spend $XX.XX on groceries and that is XX% of your income")
print("You spend $", groceries, "on groceries and that is %", groceriespercent, "of your income")

# Tell user category spending amount and percent for transportation("You spend $XX.XX on transportation and that is XX% of your income")
print("You spend $", transportation, "on tarnsportation and that is %", transportationpercent, "of your income")

# Tell user category spending amount and percent for savings ("You spend $XX.XX on savings and that is XX% of your income")
print("You spend $", savings, "on savings and that is %", savingspercent, "of your income")

# Tell user category spending amount and percent for spending ("You spend $XX.XX on spending and that is XX% of your income")
print("You spend $", spending, "on spending and that is %", spendingpercent, "of your income")