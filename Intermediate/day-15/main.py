MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
turn_off = False
money = 0


def check_resources(resource_available, coffee):
    if resources[resource_available] < MENU[coffee]['ingredients'][resource_available]:
        print(f"Sorry there is not enough {resource}")
        return (0)
    else:
        resources[resource_available] -= MENU[coffee]['ingredients'][resource_available]


def calculate_coins():
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickels = float(input("How many nickels? "))
    pennies = float(input("How many pennies? "))
    total = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    return total


def process_coins(coffee):
    coins_req = MENU[coffee]['cost']
    print("Please insert coins:")
    user_coins = calculate_coins()
    if coins_req > user_coins:
        print("Sorry that's not enough money, Money refunded")
    elif user_coins > coins_req:
        change = round((user_coins - coins_req), 2)
        print(f"Here is ${change} dollars in change")
        print(f"Here is your {coffee} enjoy !")
    elif user_coins == coins_req:
        print(f"Here is your {coffee} enjoy !")


while not turn_off:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    # Secret word to turn off the machine
    if user_input == "off":
        turn_off = True

    # Prints Report of the resources available
    elif user_input == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {money}")

    # Ask the user what he/she would like
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        for resource in resources:
            check_resources(resource, user_input)
        process_coins(user_input)
        money += MENU[user_input]['cost']
