def calc(x,y,z):
    if y == "-":
        ans = x-z
    elif y == "+":
        ans = x+z
    elif y == "/":
        ans = x/z
    elif y == "*":
        ans = x*z
    print(ans)
x = int(input("Enter the first number"))
y = input("Enter the operator")
z = int(input("Enter the second number"))
calc(x,y,z)
