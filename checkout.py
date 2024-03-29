def start(order):
    # Accept payment
    # Give change

    subtotal = 0
    tax_rate = 0.095

    print("Customer Order: ")
    for i in order:
        print(i.quantity, i.size, i.type, i.price)
        subtotal += i.quantity * i.price

    subtotal = round(subtotal, 2)
    tax = round(subtotal * tax_rate, 2)
    total = round(subtotal + tax, 2)
    print("Subtotal: $" + str(subtotal))
    print("Tax: $" + str(tax))
    print("Total: $" + str(total))

    payment(total)
    save(order, total)

def payment(total):
    while True:
        payment_type = input("Cash, Credit, or Chuck E. Cheese Tokens? ")
        if payment_type.lower() == "cash":
            print(f"The total is ${total}.")
            cash = int(input("Enter cash received: "))
            change = round(cash - total, 2)
            print(f"Your change is ${change}.")
            input("Press ENTER to continue")
            break
        elif payment_type.lower() == "credit":
            print(f"The total is ${total}.")
            print("Please swipe, insert, or tap.")
            print("Transaction Complete")
            input("Press ENTER to continue")
            break
        elif payment_type.lower() == "chuck e. cheese tokens":
            chuck_total = round(total / 2)
            print(f"The total is {chuck_total} tokens.")
            tokens = int(input("Tokens received: "))
            change = chuck_total - tokens
            print(f"Your change is {change} tokens.")
            input("Press ENTER to continue")
            break
        else:
            print("Please input Cash, Credit, or Chuck E. Cheese Tokens only")
            input("Press ENTER to continue")

def save(order, total):
    with open("pizza.dat", "a") as orders:
        for pizza in order:
            orders.write(f"{pizza.quantity}, {pizza.size}, {pizza.type}, {pizza.price}, ")
            orders.write(f"{total}")
        orders.write("\n")
    