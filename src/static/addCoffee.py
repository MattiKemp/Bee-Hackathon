from dependencies import db as db
import time


name = input("Name: ")
cups = (input("Cup(s): "))
hour = (time.time() - 1618660800) // 3600

d = db.db(host = '192.168.1.100')
d.addCoffeeData(name.lower(), hour, cups)
