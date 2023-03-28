def menu():
    global score
    score = 0
    print("Welcome to my bigger CS revision")
    choice = int(input("""
    1 - algorithms
    """))
    if choice == 1:
        algorithms(score)


def algorithms(score):
    print("Welcome to the alrgoritms section\nPlease note that you must enter the letter acosiated with the correct answer. Failure to do so will result in no points given.")
    q1 = input("what search algorithm has to be in order?\na - bubble\nb - binary\nc - merge \nd - linear\n").lower()
    if q1 == "b":
        print("Correct")
        score = score + 1
        print(f"You now have {score} points")
    else:
        print("Incorrect")
    q2 = input("What breaks a problem down into smaller peices?\na - decomposition\nb - abstraction\nc - defragmentation\nd - Galapagos Penguin Algorithm\n").lower()
    if q2 == "a":
        print("Correct")
        score = score + 1
        print(f"You now have {score} points")
    else: 
        print("incorrect")
    q3 = input("what search algorithm does not have to be in order?\na - bubble\nb - binary\nc - merge \nd - linear\n").lower()
    if q3 == "a":
        print("Correct")
        score = score + 1
        print(f"You now have {score} points")
    else: 
        print("incorrect")
    q4 = input("Which would be true if the 2 inputs were run through an AND gate?\na - 0 0\nb - 1 0\n c - 1 1\nd - 0 1\n").lower()
    if q4 == "c":
        print("Correct")
        score = score + 1
        print(f"You now have {score} points")
    else: 
        print("incorrect")
    q5 = input("Which would be true if the 2 inputs were run through an OR gate?\na - 0 0\nb - 1 0\n c - 1 1\nd - 0 1\nNote - there are more than one options avalaible, however only enter 1\n").lower()
    if q5 == "c" or q5 == "b" or q5 == "d":
        print("Correct")
        score = score + 1
        print(f"You now have {score} points")
    else: 
        print("incorrect")
    q6 = input("Which would be true if the 2 inputs were run through an XOR gate?\na - 0 0\nb - 1 0\n c - 1 1\nd - 0 1\nNote - there are more than one options avalaible, however only enter 1\n").lower()
    if q6 == "b" or q5 == "d":
        print("Correct")
        score = score + 1
        print(f"You now have {score} points")
    else: 
        print("incorrect")
    if score < 2:
        algorithms()
    elif score >= 2:
        choice = input("Would you like to repeat (1) or go back to the menu(2)")
        if choice == "1":
            algorithms()
        else: 
            menu()

    

    


menu()
input()
