from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
my_menu = Menu()
turn_off = False
while not turn_off:
    options = my_menu.get_items()
    order = input(f"What would you like to drink? {options}: ")
    drink = my_menu.find_drink(order)
    if order == "off":
        turn_off = True
    elif order == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    elif my_coffee_maker.is_resource_sufficient(drink):
        if my_money_machine.make_payment(drink.cost):
            my_coffee_maker.make_coffee(drink)

