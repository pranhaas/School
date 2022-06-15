def algorithm():
    score = 0 
    c = "correct" 
    nc = "not correct"
    print("You chose ALGORIHM!")
    q1 = int(input("""enter the corrisponding number:
    what is an algorithm?
    1 - a step of instructions to compleate a task
    2 - a peice of code
    3 - a type of language    """))
    if q1 == 1:
        print(c)
        socre = score +1
        print(socre)
    else:
        print(nc) 
    q2 = int(input("""what is decomposition?
    1 - adding more to make it run better
    2 - breaking down a problem into smaller parts
    3 - removing unessessary data"""))
    if q2 ==2:
        print(c)
        socre = score +1
        print(socre)
    else:
        print(nc)
    q3 = int(input("""what is abstraction?
    1 - the process of removing unessessary data
    2 - breaking down a problem in to smaller peices
    3 - a step of instructions to compleate a task """))
    if q3 == 1:
        print(c)
        socre = score +1
        print(socre)
    else:
        print(nc)
    q4 = int(input("""What is binary search?
    1 - has to be in order and goes along 1 by 1
    2 - has to be in order and works by splitting it in half
    3 - does not have to be in order and searches 1 by 1"""))
    if q4 == 2:
        print(c)
        socre = score +1
        print(socre)
    else:
        print(nc)
    q5 = int(input("""what is linear search?
    1 - has to be in order and goes along 1 by 1
    2 - has to be in order and works by splitting it in half
    3 - does not have to be in order and searches 1 by 1"""))
    if q5 == 3:
        print(c)
        socre = score +1
        print(socre)
    else:
        print(nc)
    q6 = int(input("""what is bubble sort?
    1 - works by swapping the order of the numbers 1 by 1
    2 - goes by the term 'devide and conqer'
    3 - it searches them 1 by 1"""))
    if q6 == 1:
        print(c)
        socre = score +1
        print(socre)
    else:
        print(nc)
    q7 = int(input("""what is merge sort?
    1 - works by swapping the order of the numbers 1 by 1
    2 - goes by the term 'devide and conqer'
    3 - it searches them 1 by 1"""))
    if q7 == 2:
        print(c)
        socre = score +1
        print(socre)
    else:
        print(nc)
    print("your socre was ", score)
    menu()
def programming():
    c = "correct"
    nc = "not correct"
    socre = 0
    q1 = int(input("""what is an integer?
    1 - a whole number
    2 - a decimal
    3 - a letter"""))
    if q1 == 1:
        print(c)
        socre = score +1
        print(socre)
    else:
        print(nc)
    q2 = int(input("""what is a float?
    1 - a whole number
    2 - a decimal
    3 - a letter"""))
    if q2 == 2:
        print(c)
        socre = score +1
        print(socre)
    else:
        print(nc)
    q3 = int(input("""whats a boolean?
    1 - a whole number
    2 - true or false
    3 - a sequence of chars"""))
    if q3 == 2:
        print(c)
        socre = score +1
        print(socre)
    else:
        print(nc)
    q4 = int(input("""what is concatonation?
    1 - merging items together
    2 - seperating items
    3 - not a word"""))
    if q4 == 1:
        print(c)
        socre = score +1
        print(socre)
    else:
        print(nc)
    q5 = int(input("""what is DIV?
    1 - the number which is not the remainder
    2 - the remainder
    3 - 2 numbers taken away"""))
    if q5 == 1:
        print(c)
        socre = score +1
        print(socre)
    else:
        print(nc)
    q6 = int(input("""what is MOD?
    1 - the number which is not the remainder
    2 - the remainder
    3 - 2 numbers taken away"""))
    if q6 == 2:
        print(c)
        socre = score +1
        print(socre)
    else:
        print(nc)
    q7 = int(input("""what is selection?
    1 - a section of code that is only run if a condition has been met
    2 - seperates code
    3 - a variable"""))
    if q7 == 1:
        print(c)
        socre = score +1
        print(socre)
    else:
        print(nc)
    q8 = int(input("""what is a varable?
    1 - an item which controls the flow of code
    2 - stores data 
    3 - a true or false"""))
    if q8 == 2:
        print(c)
        socre = score +1
        print(socre)
    else:
        print(nc)
    print("Your socre was ",score)
    menu()
def data_rep():
    q1 = int(input("""what is binary?
    1 - it is the only thing a computer reads
    2 - it is a programming language
    3 - it is used to create websites"""))
    q2 = int(input("""hat is hexadecimal?
    1 - it goes from 1-9 and a-f
    2 - only language a computer undersatands
    3 - a programming language"""))
    q3 = int(input("""how many colors would 2^6 be in an image?
    1 - 2
    2 - 100
    3 - 64"""))
    q4 = int(input("""what is a vector image?
    1 - consists of shapes, curves and lines
    2 - each pixle contains  binary data
    3 - a programming language"""))
    q5 = int(input("""what is a bitmap image?
    1 - each pixle contains bianry data 
    2 - a complex programming language
    3 - consists of shapes and lines"""))
    q6 = int(input("""what is file size = to?
    1 - base*hight*debth
    2 - with*hight*color debth
    3 - 5"""))
    
def menu():
    choice = int(input("please enter the corrisponding number:\n\t1 - algorithms\n\t2 - programming\n\t 3 - data representation\n\t4 - computer systems\n\t 0 - exit"))
    if choice == 1:
        algorithm()
    elif choice == 2:
        programming()
    elif choice == 3:
        data_rep()
    elif choice == 4:
        comp_sys()
    elif choice == 0:
        exit()
    
menu()