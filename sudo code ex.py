num1 = int(input("first number"))
num2 = int(input("second number"))

while num1 != num2:
    if num1 > num2:
        num1 = num1 - num2
    else:
        num2 = num2 - num1

    print(num1, num2)


