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

if age >=16:
    canDrive = "can"
else:
    canDrive = "can't"

if age >=15:
    canLearn = "can"
else:
    canLearn = "can't"

if age >=5:
    canSchool = "can"
else:
    canSchool = "can't"

print(f"You {canVote} vote, {canDrive} drive, {canLearn} have a learner's permit, and {canSchool} go to school.")