import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "money": 0
}

def monetary(quarters, dimes, nickles, pennies):
    total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    return total

def is_report(ask):
    if ask not in MENU:
        return "Invalid input!!"

    for item in MENU[ask]['ingredients']:
        if resources[item] < MENU[ask]['ingredients'][item]:
            return f"Sorry, there is not enough {item}."

    print("Please insert coins.")
    q = int(input("How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickles?: "))
    p = int(input("How many pennies?: "))

    payment = monetary(q, d, n, p)
    cost = MENU[ask]['cost']

    if payment < cost:
        return "Sorry, that's not enough money. Money refunded."

    for item in MENU[ask]['ingredients']:
        resources[item] -= MENU[ask]['ingredients'][item]

    change = round(payment - cost, 2)
    resources['money'] += cost

    return f"Here is your {ask}. Enjoy! Your change: ${change}"


on = True

while on:
    ask = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if ask == "report":
        for key in resources:
            print(f"{key}: {resources[key]}")
    else:
        message = is_report(ask)
        if message:
            print(message)

    run = input("If you want to turn off or on the machine, type 'OFF' or press Enter to continue: ").lower()
    if run == 'off':
        on = False
