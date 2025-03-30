from CoffeeMachine.CoffeeMaker import CoffeeMaker
from CoffeeMachine.Menu import Menu
from CoffeeMachine.MoneyMachine import MoneyMachine


def main():
    is_on =True
    coffee_maker=CoffeeMaker(100,100,100)
    money_machine=MoneyMachine()
    menu=Menu()

    while is_on:

        user_input = input("Enter <report> to generate a report on the resources\nEnter <order> to order coffee\nEnter <off> to turn the coffee machine off.")
        match(user_input.lower()):
            case "off":
                print("Thank you for using coffee machine")
                is_on=False
            case "report":
                coffee_maker.report()
                money_machine.report()
            case "order":
                menu.get_item()
                order=input("What would you like to order: ")
                menu_item=menu.find_drink(order)
                if menu_item is None:
                    print(f"Sorry we dont support {menu_item}")
                else:
                    if coffee_maker.is_resources_sufficient(menu_item) and money_machine.make_payments(menu_item.cost):
                        coffee_maker.make_coffee(menu_item)





if __name__=="__main__":
    main()