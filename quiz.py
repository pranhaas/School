import time
while True:
    score = 0
    answer = input("What Does JS stand for?\n").lower
    if answer == "javascript":
        socre = socre +1
        print("Well done! You Got it right!\nYour score is now: ",score)
    else:
        print("You were wrong!")
    answer1 = input("Which of the following is NOT a programming language?\n a = Pug\n B = Python\n C= Stone\n D= java").lower()
    if answer1 == "C":
        score = score +1
        print("Well done! You Got it right!\nYour score is now: ",score)
    else:
        print("You were wrong!")
    answer2 = input("What is python not liked for in the coding community?").lower()
    if answer2 == "Syntax"or "Syntax errors":
        score = score +1
        print("Well done! You Got it right!\nYour score is now: ",score)
    else:
        print("You were wrong!")
    answer3 = input("Which of the following is a type of database? \n A = redex\n B = sql \n c = ecl\n D = windows \n").lower()
    if answer3 == "b":
        print("Well done! You Got it right!\nYour score is now: ",score)
    else:
        print("You were wrong!")
    time.sleep(0.25)
    print("\n")
    time.sleep(0.25)
    print("\n")
    time.sleep(0.25)
    print("\n")
    time.sleep(0.25)
    print("\n")
    print("You are past the coding section, this is more general knolage!")

    answer4 = input("What is the capital city of England?").lower()
    if answer4 == "london":
        score = score +1
        print("Well done! You Got it right!\nYour score is now: ",score)
    else:
            print("You were wrong!")
    answer5 = input("What is the capital city of france?").lower()
    if answer5 == "paris":
        score = score +1
        print("Well done! You Got it right!\nYour score is now: ",score)
    else:
        print("You were wrong!")
    answer6 = input("What is the capital city of the USA?").lower()
    if answer6 == "washington":
        score = score +1
        print("Well done! You Got it right!\nYour score is now: ",score)
    else:
        print("You were wrong!")
    
    answer7=input("what continant is china located in? ").lower()
    if answer7 == "asia":
        score = score +1
        print("Well done! You Got it right!\nYour score is now: ",score)
    else:
        print("You were wrong!")
    
    answer8 = input("What is the capital of germany?").lower()
    score = score +1
    if answer8 == "berlin":
        print("Well done! You Got it right!\nYour score is now: ",score)
    else:
        print("You were wrong!")
    
    answer9 = input("What is the capital of north korea?").lower()
    if answer9 == "pyongyang":
        score = score +1
        print("Well done! You Got it right!\nYour score is now: ",score)
    else:
        print("You were wrong!")

        print("That is the end! the code is in a loop!\n p.s this has not been tested")
    
