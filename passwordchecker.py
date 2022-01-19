import random as r
def passcheck():
    passw = input("What is your password?\n")
    if (len(passw)<8) or (len(passw)>24):
        print("Error!\npassword needs to be between 8 and 24")
        passcheck()
    menu()
def genpass():
    letters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    otherones = ["!","$","%","&","*","(",")","-","_","=","+"]
    

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
