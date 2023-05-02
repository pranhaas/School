#Guessing game
import random as r
number = r.randint(1,10)
guess = int(input("What is your guess?"))
count = 0


while guess != number:
    guess = int(input("What is your guess?"))
    count = count+1
if guess == number:
    print("correct")
    print(f"You had {count} attempts")
