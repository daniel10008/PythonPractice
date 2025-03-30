class Calculator:
    def sum(self,a,b,c=None):
        if c is not None:
            return a+b+c
        return a+b
calculator =Calculator()
print(calculator.sum(5,6))
print(calculator.sum(3,4,5))