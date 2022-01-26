import random
import re

def passcheck():
    score = 0
    passw = input("What is your password?\n")
    allowed = list("qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!$%&*()_-+=1234567890")
    not_allowed_bad_human_stuff = ["qwe","rty","uio","QWE","RTY","UIO","asd","fgh", "jkl", "ASD", "FGH", "JKL", "zxc", "vbn", "ZXC", "VBN"]
    if (len(passw)<8) or (len(passw)>24):
        print("Error!\npassword needs to be between 8 and 24")
        passcheck()
    else:
        for i in allowed:
            score = score + 1
            print(score)
    print(allowed)
    
    if socre > 15:
        print("Your password is strong!")
    elif score <15 and >7:
        print("Password is moderate in strenth")
    else: 
        print("PASSWORD IS VERY WEEK!!")


    menu()
def genpass():

    pass1 = ""
    words = list("qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!$%&*()_-+=1234567890")
    ammount = 0
    while ammount < 24:
        part = random.choice(words)
        pass1 = pass1 + part
        
        ammount = ammount + 1
    print(pass1)
    menu()

def leave():
    sure = input("Are you sure you would like to leave?").lower()
    if sure == "yes" or "y":
        print("terminating")
        exit()
    else:
        menu()

def menu():
    what = int(input("""Please select the number for what task you would like to be compleated:
        1 - Check password
        2 - Generate password
        3 - Quit """))

    if what == 1:
        passcheck()
    if what == 2:
        genpass()
    if what == 3:
        leave()
menu()
