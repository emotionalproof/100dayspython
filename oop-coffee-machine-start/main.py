from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


power = True
current_menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()


def process_order(order):
    """checks resources, asks user for payment, checks payment, and makes coffee"""
    if maker.is_resource_sufficient(order):
        print(f"{order.name} is {order.cost}")
        money.make_payment(order.cost) and maker.make_coffee(order)


def init():
    """initializes main coffee machine operations and starts a while loop that checks power variable"""
    global power
    while power:
        new_order = input(f"What would you like? ({current_menu.get_items()}): ")
        if new_order.lower() == "off":
            power = False
        elif new_order.lower() == "report":
            maker.report()
            money.report()
        else:
            order = current_menu.find_drink(new_order)
            order and process_order(order)


init()
