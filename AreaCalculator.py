"""Area Calculator"""

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print "Start to calculate!"

print "Current time: %s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)

sleep(1)

hint = "Don't forget to include the correct units!\nExiting..."

option = raw_input("Enter C for Circle and T for Triangle:")

option = option.upper()

if option == "C":
  radius = float(raw_input("Enter radius:"))
  area = pi * radius ** 2
  print "The pie is baking..."
  sleep(1)
  print("Area: %.2f \n%s" % (area, hint))
elif option == "T":
  base = float(raw_input("Enter base:"))
  height = float(raw_input("Enter height:"))
  area = base * height / 2
  print("Uni bi Tri...")
  sleep(1)
  print("Area: %.2f \n%s" % (area, hint))
else:
  print("Invalid shape")
  
