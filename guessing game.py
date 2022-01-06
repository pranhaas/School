import random as r
num = r.randint(1,100)
x=0
while x<1:
    
    guess = int(input("What is your guess?"))
    if guess == num:
        print("correct!")
        x=x+1
    elif guess < num:
        print("Higher!")
    elif guess > num:
        print("Lower!")
input()
