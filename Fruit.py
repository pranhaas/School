fruit = ["apple","pare","orange"]

search1 = input("fruit?")
while True:
    if search1 == fruit[0]:
        print("found!")
        exit()

    if search1 == fruit[1]:
        print("found!")
        exit()

    if search1 == fruit[2]:
        print("found!")
        exit()

    else:
        print("Not found")
