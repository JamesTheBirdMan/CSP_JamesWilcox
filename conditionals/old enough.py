# James Wilcox, Old Enough Python

age = int(input("How old are you? \n"))
canVote = "Incomplete"
canDrive = "Incomplete"
canLearn = "Incomplete"
canSchool = "Incomplete"
if age >=18:
    canVote = "can"
else:
    canVote = "can't"
print(canVote)

if age >=16:
    canDrive = "can"
else:
    canDrive = "can't"
print(canDrive)

if age >=15:
    canLearn = "can"
else:
    canLearn = "can't"
print(canLearn)

if age >=18:
    canSchool = "can"
else:
    canSchool = "can't"
print(canSchool)

print(f"You {canVote} vote, {canDrive} drive, {canLearn} have a learner's permit, and {canSchool} go to school.")