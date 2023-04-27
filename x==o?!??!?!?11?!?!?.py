def equal(a):
    List = []
    x = 0
    o = 0
    for n in a:
        if n == "x":
            x += 1
        elif n == "o":
            o +=1
    if x == o:
        return(True)
    else:
        return(False)
a = input("Please enter the str\n")
print(equal(a))
    
