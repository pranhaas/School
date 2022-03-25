import time

def menu():
    what = int(input("""Please choose one of the following options:
        0 - exit
        1 - sound 
        2 - image
        3 - text"""))

    if what == 0:
        exit0()
    elif what == 1:
        sound()
    elif what == 2:
        image()
    elif what == 3:
        text_conversion()
    else:
        print("Choose a number duh")
        menu()
def exit0():
    print("Exiting...")
    time.sleep(1)
    exit()
def sound():
    sampler = int(input("What is the sample rate?\n"))
    time = int(input("How long in seconds is the song\n"))
    sampleres = int(input("What is the sample reselution?\n"))
    tot = sampler * sampleres * time

    whatin = int(input("""Select the corrisponding number:
        1 - bit
        2- bytes
        3 - Kb
        4 - Mb
        5 - Gb
        6 - Tb"""))
    bit = tot
    bytess = bit / 8
    kb = bytess / 1000
    mb = kb / 1000
    gb = mb / 1000
    tb = gb / 1000
    if whatin == 1:
        print(bit)
        menu()
    elif whatin == 2:
        print(bytess)
        menu()
    elif whatin == 3:
        print(kb)
        menu()
    elif whatin == 4:
        print(mb)
        menu()
    elif whatin == 5:
        print(gb)
        menu()
    elif whatin == 6:
        print(tb)
        menu()
    else:
        print("ERROR!")
        menu()

def image():
    width = int(input("what is the width?"))
    hight = int(input("What is the hight?"))
    color = int(input("What is the color debth?"))
    tot = width*hight*color
    whatin = int(input("""Select the corrisponding number:
    1 - bit
    2- bytes
    3 - Kb
    4 - Mb
    5 - Gb
    6 - Tb"""))
    bit = tot
    bytess = bit / 8
    kb = bytess / 1000
    mb = kb / 1000
    gb = mb / 1000
    tb = gb / 1000
    if whatin == 1:
        print(bit)
        menu()
    elif whatin == 2:
        print(bytess)
        menu()
    elif whatin == 3:
        print(kb)
        menu()
    elif whatin == 4:
        print(mb)
        menu()
    elif whatin == 5:
        print(gb)
        menu()
    elif whatin == 6:
        print(tb)
        menu()
    else:
        print("ERROR!")
        menu()
def text_conversion():
    text = input("Please enter your sentance(s)\n")
    whatin = int(input("""Select the corrisponding number:
    1 - bit
    2- bytes
    3 - Kb
    4 - Mb
    5 - Gb
    6 - Tb"""))
 
    lenth =len(text)
    bits = lenth * 8
    bytess = bit / 8
    kb = bytess / 1000
    mb = kb / 1000
    gb = mb / 1000
    tb = gb / 1000
    if whatin == 1:
        print(bit)
        menu()
    elif whatin == 2:
        print(bytess)
        menu()
    elif whatin == 3:
        print(kb)
        menu()
    elif whatin == 4:
        print(mb)
        menu()
    elif whatin == 5:
        print(gb)
        menu()
    elif whatin == 6:
        print(tb)
        menu()
    else:
        print("ERROR!")
        menu()
    print(lenth)
    menu()
menu()

