import random as r
import time as t
while True:
    a = input("Would you like to roll?").lower()
        if a == "yes":
        t.sleep(1)
        num = r.randint(1,6)
        print("You rolled : ",num)
    else:
        exit()