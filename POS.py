#Droid POS System

import os
import time
import menu_items

os.system('cls')

print("Welcome to the Droid Restaraunt!\n")
answer = input("What would you like to do?\n1. See Menu\n2. Place Order\n\n")

if answer == "1":
    os.system('cls')

#Access menu text file
    fr = open('menu.txt', 'r')
    menu = fr.read()
    fr.close()
    print(menu)
    time.sleep(2.5)
    menu_items.cart()
#Access menu text file

if answer == "2":
    os.system('cls')
    menu_items.cart()