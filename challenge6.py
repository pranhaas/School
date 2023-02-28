import time as t
a = t.time()
input("Press the enter key when you think 10 seconds has passed")
b = t.time()
a = round(a)
b = round(b)
total = b-a
print(f"Your time was {total}s.\n You were {10-total}s far away")

input()
