import time as t

#using subroutines thingy
while True:
    def rle():
        print("RLE has been called")
    def asciiart():
        print("ascii art has been called")
    def conasciiart():
        print("Convert to ascii art has been called")
    def conrle():
        print("convert to rle has been called")
    def quit():
        print("Terminating the program...")
        t.sleep(0.5)
        exit()

    #menue sutff 
    def menu():
        what = input("Enter the corisponding number for what function you would like to use\n\n\t1 - Enter RLE\n\t2 - Display ASCII art\n\t3 - Convert to ASCII art\n\t4 - Convert to RLE\n\t5 - Quit\n\n")
        

        #peols choice
        if what == "1":
            rle()
        elif what == "2":
            asciiart()
        elif what == "3":
            conasciiart()
        elif what == "4":
            conrle()
        elif what == "5":
            quit()
        else:
            print("Invalid number.")


    menu()
