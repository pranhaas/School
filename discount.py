name = input("What is your name? \n")
budegt = float(input("What is your budet \n"))
age = int(input("What is your age? \n"))
dept = input("What department would you like to shop in?\n")
if age >= 60:
    budegt = budegt * 0.75
elif age <= 18:
    budegt = budegt * 0.90
elif dept == "homewear":
    budegt = budegt * 0.9
elif dept == "womenswear":
    budegt = budegt * 0.95
elif dept == "menswear":
    budegt = budegt * 0.85
elif dept == "shoes" and age == 30:
    budegt = budegt * 0.5
print(budegt)

