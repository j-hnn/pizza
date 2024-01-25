import warnings, pandas

class Order:
    def __init__(self, quantity, size, type, price):
        self.quantity = quantity
        self.size = size
        self.type = type
        self.price = price

warnings.simplefilter(action='ignore', category=FutureWarning)

def start():
    print("Which pizza would you like to order?")
    pizza_menu = pandas.read_csv("data/types.csv")
    print(pizza_menu[["Type", "Size", "Price"]])

    selection = int(input(">> "))
    size = pizza_menu.iloc[selection][1]
    ptype = pizza_menu.iloc[selection][0]
    price =  pizza_menu.iloc[selection][2]
    quantity = int(input(f"How many {size} {ptype} pizzas do you want? "))

    order = Order(quantity, size, ptype, price)

    print(order.quantity, order.size, order.type, order.price)