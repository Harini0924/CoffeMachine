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
}


def pick_drink(choose_drink):
    global water
    global milk
    global coffee
    global cost
    global water_left
    global milk_left
    global coffee_left
    #global money
    water = (MENU[choose_drink]["ingredients"]["water"])
    milk = (MENU[choose_drink]["ingredients"]["milk"])
    coffee = (MENU[choose_drink]["ingredients"]["coffee"])
    cost =(MENU[choose_drink]["cost"])
    water_left = (resources["water"])
    milk_left = (resources["milk"])
    coffee_left = (resources["coffee"])
    money = 0



def report():
    global water_left
    global milk_left
    global coffee_left
    #global money
    water_left -= water
    print(water_left)
    milk_left -= milk
    print(water_left)
    coffee_left -= coffee
    print(coffee_left)

    """print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}ml")
    print(f"Money: ${money}")
"""
def check_resources():
    if (water_left < 0):
        return("Sorry there is not enough water.")
    elif (milk_left < 0):
        return("Sorry there is not enough milk.")
    elif (coffee_left < 0):
        return("Sorry there is not enough coffee.")



place_order = True
def game(choose_drink):

    pick_drink(choose_drink)
    while(place_order == True):
        money = cost
        report()
        (check_resources())
        while(check_resources() == "Sorry there is not enough water." or check_resources() == "Sorry there is not enough milk." or check_resources() == "Sorry there is not enough coffee."):
            print(check_resources())
            choose_drink = input("What would you like? (espresso/latte/cappuccino): ")
        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        money_deposited = (quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .25)
        if (money_deposited < money):
            print("Sorry that's not enough money. Money refunded.")
        if(money_deposited>money):
            change = round((money_deposited -cost),2)
            print(f"Here is you {change} in change.")
            print(f"Here is your {choose_drink}. Enjoy!")
        choose_drink = input("What would you like? (espresso/latte/cappuccino): ")
        if(choose_drink =="off"):
            place_order == False
        if(choose_drink =="report"):
            report()



choose_drink = input("What would you like? (espresso/latte/cappuccino): ")
if (choose_drink == "report"):
    report()
    choose_drink = input("What would you like? (espresso/latte/cappuccino): ")
game(choose_drink)
