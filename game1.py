answer = "mobile"
x = 0
while x < 10:
    guess = input("What is your guess?\n If you would like to exit, say 'exit'").lower()

    if guess == "mobile":
        print("Winner!")
        x = 10
    elif guess == "exit":
        exit()
    else:
        print("Try again")
        x=x + 1

