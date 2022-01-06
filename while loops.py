while True:
    x = 0
    password = "pa55word"
    username = "bart"

    username1 = input("What is the username?")
    password1 = input("What is the password?")

    if username1 == username:
        print("The username was correct!")
        x=x+1
    else:
        print("The username was wrong!\n try again!")
    if password1 == password:
        print("the password was correct!")
        x = x+1
    else:
        print("The password was wrong!\n try again!")

    if x == 2:
        print("Password and username are correct!")
        exit()
input()
