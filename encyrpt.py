def menu():
    choice = int(input("""Please select the corrisponding number
        1 - encrypt
        2 - decrypt
        0 - exit"""))
    if choice == 1:
        encrypt()
    elif choice == 2:
        decrypt()
    elif choice == 0:
        exit()
    else:
        print("err")
        menu()
def encrypt():
    norm = list("abcdefghijklmnopqrstuvwxyz")
    encry = list("zwxwvutsrqponmlkjihgfedcba")
    new = ""
    text = input("Please enter the text you would like to encrpt\n")
    for n in text:
        count = 0 
        stop = True
        while stop:
            if n == norm[count]:
                new = new + encry[count]
                stop = False
            else: 
                count = count +1
    print(f"The encrypted text is {new}")
    menu()
def decrypt():
    norm = list("abcdefghijklmnopqrstuvwxyz")
    encry = list("zwxwvutsrqponmlkjihgfedcba")
    new = ""
    text = input("Please enter the text you would like to encrpt\n")
    for n in text:
        count = 0 
        stop = True
        while stop:
            if n == encry[count]:
                new = new + norm[count]
                stop = False
            else: 
                count = count +1
    print(f"The decrypted text is {new}")
    menu()
    
        
menu()
        
