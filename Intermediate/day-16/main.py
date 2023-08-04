from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
item = MenuItem('name', 'water', 'milk', 'coffee', 'cost')
coffee = Menu()
resources = CoffeeMaker()
turn_off = False
cost = MoneyMachine()

while not turn_off:
    user_input = input(f"What would you like {(coffee.get_items())}")
    # Secret word to turn off the machine
    if user_input == "off":
        turn_off = True
    #  Prints report of the resources available
    elif user_input == "report":
        resources.report()
        cost.report()
    else:
        if resources.is_resource_sufficient(coffee.find_drink(user_input)) and  cost.make_payment(coffee.find_drink(user_input).cost):
            resources.make_coffee(coffee.find_drink(user_input))





