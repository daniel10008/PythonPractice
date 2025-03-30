class Coordinate:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"{self.x}/{self.y}"
    def __add__(self, other):
        result =Coordinate(self.x+other.x,self.y+other.y)
        return result
    def __sub__(self, other):
        result =Coordinate(self.x-other.x,self.y-other.y)
        return result
coordinate1 =Coordinate(13,56)
coordinate2=Coordinate(276,34)

print(coordinate1)
print(coordinate1+coordinate2)
print(coordinate1-coordinate2)