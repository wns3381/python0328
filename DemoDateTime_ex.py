# DemoDateTime_ex.py

import time

#print(dir(time))

print(time.time())
print(time.sleep(1))
print(time.gmtime())
print(time.localtime())

from datetime import *
day1 = date(1977,11,10)
day2 = date(2022,3,30)
day3 = date.today()
print(day1, day2, day3)
print(day2-day1)
