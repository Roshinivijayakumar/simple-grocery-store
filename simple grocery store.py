
from ast import Break
from operator import truediv
items_available = {"milk": 20, "egg": 5, "rice": 40, "wheat": 35, "sugar": 25, "apple": 60,
                   "orange": 55, "coffee": 30, "greentea": 75, "juice": 30, "cookies": 60, "soap": 30, "toothpaste": 40}
print("# rice, wheat, sugar, apple,oranges prices per kg")
total = 0
while True:
    print("-"*10, "welcome to the shop", '-'*10)
    print("select what you want to do")
    print("type'1' To buy groceries")
    print("type'2' To quit")
    ch = int(input("enter the your choice : "))
    if ch == 1:
        a = ' '
        while a != 'N':

            print("items available in our store")
            print(items_available)
            s = input("enter which you want to buy :").lower()

            if s in items_available:
                d = int(input("enter quantity: "))
                price = (d * items_available[s])
                print("price=", price)
                total += price
                a = input(
                    "enter 'y' if u want to add some more items; enter 'n' if u wanna end shopping :").upper()
                if a == "N":
                    break

            else:
                print("not present in our store '\n' please enter any other prdt")

        print('the total price of your purchase is:', total)

    if total > 0:
        delivery = input(
            "Please Enter Mode of Delivery '1' for in store '2' Door Delivery :").lower()
        if delivery == "2":
            ask_address = input("enter ur address for home delivery:")
            ask_phno = int(input("please enter your contact no: "))
            print("ur address:", ask_address, "; ur phno:", ask_phno)
            print()
            print("***groceries will be delivered soon***")
            break
        else:
            print()
            print("*********Thank you! visit again***********")
            break
    elif ch == 2:
        print("**********")
        break
