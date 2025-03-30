from locale import currency


class MoneyMachine:
    currency = "$"
    coin_values ={"quarter":0.25,"dime":0.10,"nickel":0.05,"pennie":0.01}

    def __init__(self):
        self.profit=0

    def report(self):
        print(f"Money: {self.currency}{self.profit}")
    def make_payments(self,cost):
        print("Please insert coins")
        total_coin=0
        for item in self.coin_values:
            coin=int(input(f"Please insert {item}"))
            total_coin+=coin*self.coin_values[item]
        if total_coin<cost:
            print(f"Sorry, not enough money, money is refunded: {self.currency}{total_coin}")
            return False
        else:
            change =total_coin-cost
            if change>0:
                print(f"Here is you change: {self.currency}{change}")
            self.profit+=cost
            return True

if __name__=="__main__":
    money=MoneyMachine()
    money.make_payments(20)
    money.report()

