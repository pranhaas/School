import random as r
score = 0
while True:
    print("""Would you like to:
    add = +
    divide = /
    subtract = -
    times = *
    or if you would like to exit do exit""")
    what = input()
    if what == "exit":
        exit()
    num1 = r.randint(0,10)
    num2 = r.randint(0,10)
    print("The question is \n",num1, what, num2,"\n what is your guess?")
    guess = int(input())

    if what == "*":
        answer = num1 * num2
        if guess == answer:
            print("Welldone! you were right!")
            score = score + 1
            print("Your score is: ",score)
        else:
            print("You were wrong :(")
    elif what == "+":
        answer = num1 + num2
        if guess == answer:
            print("Welldone! you were right!")
            score = score + 1
            print("Your score is: ",score)
        else:
            print("You were wrong :(")
    elif what == "-":
        answer = num1 - num2
        if guess == answer:
            print("Welldone! you were right!")
            score = score + 1
            print("Your score is: ",score)
        else:
            print("You were wrong :(")
    elif what == "/":
        answer= num1/num2
        if guess == answer:
            print("Welldone! you were right!")
            score = score + 1
            print("Your score is: ",score)
        else:
            print("You were wrong :(")
