from wattage import *
from batlife import *
from volts import *
from ohms import *
from amperecalc import *
import time


menu = """
~~~~calculations~~~~
~~1.batterylife~~~~
~~2.wattage~~~~
~~3.voltage~~~~
~~4.ohm~~~~
~~5.ampere~~~~
"""

print("_________light project calculation_________")
time.sleep(1)
print("~~~~please choose one of the following~~~~")
time.sleep(1)
print(menu)
time.sleep(1)
usrask = input("please choose one of the following")



if str(usrask) == "1":
    batcalc()

if str(usrask) == "2":
    wattcalc()

if str(usrask) == "3":
    voltcalc()
    
if str(usrask) == "4":
    ohmcalc()
    
if str(usrask) == "5":
    ampcalc()

    