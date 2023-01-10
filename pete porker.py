def menu():
    global egg
    global pie
    global tart
    egg = int(input("How many schotch eggs would you like?"))
    pie = int(input("How many pork pies would you like?"))
    tart = int(input("How many quiche tarts would you like?"))
    check()
def check():
    print(f"""Please confirm your order of:
    {egg} - eggs
    {pie} - pies
    {tart} - tarts
    To proceed please type 'confirm'
    To go back please enter anything other than 'confirm'""")
    ans = input().lower()
    if ans == "confirm":
        total()
    else:
        menu()
def total():
    price_egg = egg * 0.49
    price_pie = pie * 0.85
    price_tart = tart * 1.45
    total = price_tart + price_pie + price_egg
    r_total = round(total, 2)
    print(f"""Recepit for pete proker's pork pie emporium:
    {egg} scotch eggs = £{price_egg}
    {pie} pork pies = £{price_pie}
    {tart} quiche tarts = £{price_tart}
    Your total is £{r_total}
    """)
menu()                             