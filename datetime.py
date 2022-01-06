import datetime as d
import time as t
while True:
    da = d.datetime.today()
    print(da.hour, da.minute, da.second) 
    t.sleep(1)
input()