import math


class Shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, breadth, name):
        super().__init__(name)
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
class Circle(Shape):
    def __init__(self, radius, name):
        super().__init__(name)
        self.radius=radius
    def area(self):
        return (self.radius**2)*math.pi
circle=Circle(4,"Daniel")
rectangle=Rectangle(4,6,"Daniel")
print(circle.area())
print(rectangle.area())