menu ={"espresso": {"ingredient":{"water": 50,"coffee":25},"cost":2.50},"latte":{"ingredient":{"water": 25,"coffee":50,"milk":50},"cost":3.00},"cappuccino":{"ingredient":{"water":25,"coffee":50},"cost":5.00}}
resources={"water":300,"milk":500,"coffee":100,"money":0.00}

def print_report():
        for key, value in resources.items():
            print(f"{key} : {value}")
def check_resources(drink_name):
    for item in menu[drink_name]["ingredient"]:
        if resources[item]<menu[drink_name]["ingredient"][item]:
            return False
    return True
def process_coins():
    print("please enter coins:")
    quarter=int(input("how many quarters do you want to insert: "))*0.25
    dime=int(input("how many dimes do you want to insert: "))*0.10
    nickle=int(input("how many nickles do you want to insert: "))*0.05
    pennies=int(input("how many pennies do you want to insert"))*0.01
    return quarter+dime+nickle+pennies

def check_transaction_successful(money,drink_name):
    if money<menu[drink_name]["cost"]:
        print(f"sorry that is not enough money\ntake your refund: {round(money,2)}")
        return False
    else:
        change=money-menu[drink_name]["cost"]
        if change>0:
            print(f"your change is {round(change,2)}$")
        resources["money"]+=menu[drink_name]["cost"]
        return True

def make_coffee(coffee_name):
    for item in menu[coffee_name]["ingredient"]:
        resources[item]-=menu[coffee_name]["ingredient"][item]
    print(f"here is your {coffee_name}, Enjoy!")
def coffee_machine():
    is_on =True
    while is_on:
        user_input= input("Enter <report> to generate a report on the resources\nEnter <order> to order coffee\nEnter <off> to turn the coffee machine off.")
        if user_input.lower()=="order":
            print("what would you like to order?")
            for key, value in menu.items():
                print(f"{key.upper()} : cost = {value["cost"]}$")
            coffee_order=input("Please enter the coffee name to order: ")
            if coffee_order in menu:
                if check_resources(coffee_order):
                    payment=process_coins()
                    if check_transaction_successful(payment,coffee_order):
                        make_coffee(coffee_order)
                else:
                    print("Resources unavailable")
            else:
                print("We do not have that kind of coffee")
        elif user_input.lower() == "off":
            print("Thank you for using the coffee machine!")
            is_on=False
        elif user_input.lower() =="report":
            print_report()
        else:
            print("Invalid option, try again")
coffee_machine()


