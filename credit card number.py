def number(num):
    List = []
    x = len(num)
    x = x-4
    result = ""
    for n in num:
        List.append(n)
    for n in range (x):
        List[n] = "*"
    return(List)
num = input("Please enter your credit card details :) \n")
print(number(num))
