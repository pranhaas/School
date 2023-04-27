List = [1,3,12,4,2,10]
value = input("Please enter asc, desc, none")
def sort_list(List, value):
    x = 0 
    if value == "asc":
       List.sort()
       print(List)
    elif value == "desc":
        List.sort()
        List.reverse()
        print(List)
    else:
        print(List)
sort_list(List, value)
