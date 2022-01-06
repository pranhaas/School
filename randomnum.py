import random as r
while True:
    print("guess my number between 1-100")
    guess = int(input())
    answer = r.randint(1,100)
    while guess != answer:
        if guess == answer:
            print("Welldone!")
        else:
            print("Try again")
            print("guess my number between 1-100")
            guess = int(input())
