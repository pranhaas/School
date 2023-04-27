import math 
pi = math.pi

def radians(x):
    degrees = x *(180/pi)
    print(degrees)
num = int(input("Please enter the radian to convert to degrees"))
radians(num)
