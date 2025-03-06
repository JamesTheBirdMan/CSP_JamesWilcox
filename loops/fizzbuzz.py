# James Wilcox, FizzBuzz Python

num = 1
while num <=50:
    if (num % 3 == 0) & (num % 5 == 0):
        print("FizzBuzz")
        num +=1
    elif (num % 3 == 0):
        print("Fizz")
        num +=1
    elif (num % 5 == 0):
        print("Buzz")
        num +=1
    else:
        print(num)
        num +=1