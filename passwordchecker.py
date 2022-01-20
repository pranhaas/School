import random
import re

def passcheck():
    score = 0
    passw = input("What is your password?\n")
    if (len(passw)<8) or (len(passw)>24):
        print("Error!\npassword needs to be between 8 and 24")
        passcheck()
    letters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    otherones = ["!","$","%","&","*","(",")","-","_","=","+"]

    menu()
def genpass():

    pass1 = ""
    words = list("qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!$%&*()_-+=")
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
