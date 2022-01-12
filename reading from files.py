import time as t
def menu():
    print("Welcome to my text files")
    option = input("""Please chose an option
        1 - reading
        2 - writing
        3 - appending
        4 - quit""")

    if option == "1":
        reading()
    elif option == "2":
        writing()
    elif option == "3":
        appending()
    elif option == "4":
        leave()
    else:
        print("invalid choice")
        menu()






def reading():
    file = open("doc1","r")
    print(file.read())
    file.close()
    print("File has been read")
    again = input("Would you like to reread?").lower()
    if again == "yes":
        reading()
    else:
        t.sleep(0.5)
        menu()
def writing():
    file = open("doc1","w+")
    print(file.read())
    aresure = input("Are you sure you would like to overwrite?").lower()
    if aresure =="yes":
        edit = input("please enter what you would like to write:\n")
        file.write(edit)
        file.close()

    else:
        menu()
    menu()
def appending():
    file = open("doc1","a+")
    print(file.read())
    what = input("Please enter what you would like to write:\n")
    file.write(what)
    file.close()
    menu()
def leave():
    sure = input("Are you sure you want to quit?").lower()
    if sure == "yes":
        
        print("terminating program..")
        exit()
    else:
        menu()

menu()
input()
