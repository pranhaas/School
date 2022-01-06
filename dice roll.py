import random
while True:
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)

    if roll1 == roll2:
        print('you rolled a dobble! \n ',roll1)
        exit()
    else:
        print("you did not roll a dobble :( \n your numbers were:", roll1, roll2)

