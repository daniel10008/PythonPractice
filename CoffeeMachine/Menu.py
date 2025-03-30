from CoffeeMachine.MenuItem import MenuItem


class Menu:
    def __init__(self):
        self.menu =[MenuItem("latte", 3,30,50,20),
                    MenuItem("espresso",4,20,0,50),
                    MenuItem("cappuccino",5,30,20,40)]
    def get_item(self):
            for item in self.menu:
                print(item)
    def find_drink(self,order_name:str):
        for item in self.menu:
            if item.name==order_name:
                return item
        return None
if __name__ =="__main__":
    menu=Menu()
    menu.get_item()