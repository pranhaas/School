def converter(decimal):
    convert = [128,64,32,16,8,4,2,1]
    binary = []
    for n in convert:
        if n <= decimal:
            decimal -=n
            binary.append(1)
        elif n > decimal:
            binary.append(0)
        else:
            return("ERROR")
    print(binary)
        
decimal = int(input("Please enter a decimal number to convert into binary!\n"))
converter(decimal)
