class MenuItem:
    def __init__(self,name,cost,water,milk,coffee):
        self.name=name
        self.cost=cost
        self.ingredients={"water":water,"milk":milk,"coffee":coffee}
    def __repr__(self):
        return f"{self.name} ${self.cost}"
if __name__ =="__main__":
    menu_items=MenuItem("Latte", 2.5,50,60,30)
    print(menu_items)
