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
}

def resources_sufficient(order_ingredients):
    """Cheacks if all the resources and sufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item} 😶.")
            return False
    return True


def process_coins():
    """Calculates the payment"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def money_sufficient(payment_received, drink_cost):
    """Checks if the customer has given enough money"""
    if payment_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(payment_received - drink_cost,2)
        print(f"Here is your ${change} 🤓.")
        return True

    else:
        print("Sorry that's not enough money ☹️. Money refunded")
        return False


def deduct_resources(drink_name,order_ingredients):
    """After every transaction deducts the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {user_choice} ☕️. Enjoy!")


get_coffee = True
while get_coffee == True:
    user_choice = input("What would you like? (espresso/latte/cappuccino: ")
    if user_choice == 'off':
        get_coffee = False
    elif user_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        if resources_sufficient(drink['ingredients']):
            payment = process_coins()
            money_sufficient(payment,drink['cost'])
            deduct_resources(drink,drink['ingredients'])


