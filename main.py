"""
Title: Pizza Time
Description: Manage pizza orders, checkout, and inventory for a local pizza store
Author: John Weng
Version: 1.0
"""

import order, checkout, inventory

print("Wekcome to Pizza Time!")

pizza_order = []
while True:
    print("Select an option below.")
    print("1. Order")
    print("2. Checkout")
    print("3. Inventory")
    print("4. Exit")

    selection = input(">> ")
    if selection == "1":
        pizza_order = order.start()
    elif selection == "2":
        if len(pizza_order) > 0:
            checkout.start(pizza_order)
        else:
            print("The cart is empty")
    elif selection == "3":
        inventory.start()
    elif selection == "4":
        print("Goodbye!")
        break
    else:
        print("Please enter a valid selection")