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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
def monetary(quarters,dimes,nickles,pennies):
    q= 0.25*quarters
    d=0.1*dimes
    n=0.05*nickles
    p=0.01*pennies
    total=q+d+n+p
    return total

on=True
while on:
   ask=input("What would you like? (espresso/latte/cappuccino): ").lower()
   if ask=='report':
     for key in resources:
         print(f"{key}: {resources[key]}")
   elif ask in MENU:
      print("please insert coins.")
      q=int(input("How many quarters?: "))
      d=int(input("How many dimes?: "))
      n=int(input("How many nickles?: "))
      p=int(input("How many pennies?: "))
      profit+=monetary(q,d,n,p)

    
