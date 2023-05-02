name = input("What is your name?")
budegt = float(input("What is your budet"))
age = int(input("What is your age?"))
if age >= 60:
    budegt = budegt * 0.75
elif age <= 18:
    budegt = budegt * 0.90
print(budegt)
