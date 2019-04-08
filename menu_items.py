#Droid Restaranut menu items

import os
import time

def cart():

    cart = 0

#Drink Prices
    coke = 3
    water = 1
    orange_pop = 3
    coffee = 5
#Drink Prices

#Food Prices
    chips = 1
    salad = 6
    pizza = 10
    hot_dog = 5
    pasta = 25
#Food Prices

    print_order = [] #Holds the full order when complete

    continueOn = "yes"

    while continueOn == "yes":
        order = input("\nWhat would you like to order?\n").lower()
#----------------------Drinks-------------------------
        if order == "coke":
            cartTemp = int(input("\nHow many orders of Coke would you like?\n"))
            cart = cart + cartTemp * coke
            print_order.append(str(cartTemp) + " order(s) of Coke")
        if order == "water":
            cartTemp = int(input("\nHow many orders of Water would you like?\n"))
            cart = cart + cartTemp * water
            print_order.append(str(cartTemp) + " order(s) of Water")
        if order == "orange pop":
            cartTemp = int(input("\nHow many orders of Orange Pop would you like?\n"))
            cart = cart + cartTemp * orange_pop
            print_order.append(str(cartTemp) + " order(s) of Orange Pop")
        if order == "coffee":
            cartTemp = int(input("\nHow many orders of Coffee would you like?\n"))
            cart = cart + cartTemp * coffee
            print_order.append(str(cartTemp) + " order(s) of Coffee")
#----------------------Drinks-------------------------

#----------------------Food-------------------------
        if order == "chips":
            cartTemp = int(input("\nHow many orders of Chips would you like?\n"))
            cart = cart + cartTemp * chips
            print_order.append(str(cartTemp) + " order(s) of Chips")
        if order == "salad":
            cartTemp = int(input("\nHow many orders of Salad would you like?\n"))
            cart = cart + cartTemp * salad
            print_order.append(str(cartTemp) + " order(s) of Salad")
        if order == "pizza":
            cartTemp = int(input("\nHow many orders of Pizza would you like?\n"))
            cart = cart + cartTemp * pizza
            print_order.append(str(cartTemp) + " order(s) of Pizza")
        if order == "hot dog":
            cartTemp = int(input("\nHow many orders of Hot Dog would you like?\n"))
            cart = cart + cartTemp * hot_dog
            print_order.append(str(cartTemp) + " order(s) of Hot Dog")
        if order == "pasta":
            cartTemp = int(input("\nHow many orders of Pasta would you like?\n"))
            cart = cart + cartTemp * pasta
            print_order.append(str(cartTemp) + " order(s) of Pasta")
#----------------------Food-------------------------

        continueOn = input("\nAnything else?\n").lower()
            
    os.system('cls')

    print("Your order:")

    for i in range(0, len(print_order)):
        print(print_order[i])

    print("\nTotal cost: $" + str(cart))

    answer = input("\nHow would you like to pay?\n")

    if answer == "cash":
        cash = int(input("\nHow much are you giving the cashier?\n$"))
        
        if cash == cart:
            print("\nPayment successful\n")
            time.sleep(2)
            print("No change due")
            time.sleep(2)
            print("Thank you for your purchase!")
        if cash > cart:
            change = cash - cart
            print("\nPayment successful\n")
            time.sleep(2)
            print("Change due is $" + str(change))
            time.sleep(2)
            print("\nThank you for your purchase!")

    if answer == "credit card":
        print("\nPayment successful\n")
        time.sleep(2)
        print("Thank you for your purchase!")