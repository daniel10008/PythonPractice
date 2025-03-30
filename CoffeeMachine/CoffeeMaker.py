from CoffeeMachine.MenuItem import MenuItem


class CoffeeMaker:
    def __init__(self,water,milk,coffee):
        self.resources={"water":water,"milk":milk,"coffee":coffee}
    def report(self):
        print(f"water: {self.resources["water"]}mL\nmilk: {self.resources["milk"]}mL\ncoffee: {self.resources["coffee"]} grams")
    def is_resources_sufficient(self, menu_item):
        for item in menu_item.ingredients:
            if self.resources[item]<menu_item.ingredients[item]:
                print(f"Sorry there is not enough {item}")
                return False
        return True
    def make_coffee(self,order):
        for item in order.ingredients:
            self.resources[item]-=order.ingredients[item]
        print(f"Here is your coffee {order.name}")


if __name__ =="__main__":
    coffee_maker=CoffeeMaker(30,40,20)
    coffee_maker.report()
    coffee_maker.is_resources_sufficient(MenuItem("Latte", 2.5,20,60,30))
    coffee_maker.make_coffee(MenuItem("Latte", 2.5,20,60,30))
