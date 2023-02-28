studentnames = ["rob","anna","huw","emma","patrice","iqbal"]
present = 0
absent = 0 
for n in studentnames:
    print(n)
    here = input("Are they here?")
    if here == "yes":
        present = present + 1
    else: 
        absent =absent + 1
print(f"the total present {present} absent {absent}")
input()