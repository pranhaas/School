import random


def passcheck():
    password = input("Enter a password: \n")

    #for i in list(password):
    if (len(password)<8) or (len(password)>24):
        print("Error!\npassword needs to be between 8 and 24")
        passcheck()

    for i in list(password):
        #FAKE NEWS!!
        capsone = False
        lower = False
        num = False
        symbols = False

        #points bit
        global points
        points = 0
        points = points + len(password)
        for i in password:
            if i in "qwertyuiopasdfghjklzxcvbnm":
                lower = True
            elif i in "QWERTYUIOPASDFGHJKLZXCVBNM":
                capsone = True
            elif i in "1234567890":
                num = True
            elif i in "!$%^&*()-_=+":
                symbols = True
            #adding points
        if lower == True:
            points = points + 5
        elif capsone == True:
            points = points + 5
        elif num == True:
            points = points + 5
        elif symbols == True:
            points = points + 5
        elif symbols and num and capsone and lower == True:
            points = points + 10
            #subtracting points

            #letters only 
        elif num == False and symbols == False:
            points = points - 5
            #num only 
        elif lower == False and capsone == False and symbols == False:
            points = points - 5
            #symbols only
        elif lower == False and capsone == False and num == False:
            points = points - 5

    print(points)

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
    else:
        print("Error!\nPlease Type 1, 2 or 3")
        menu()
menu()
