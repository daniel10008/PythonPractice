class Example:
    def __new__(cls, *args, **kwargs):
        print("this is an example class")
        return super(Example, cls).__new__(cls)
    def __init__(self):
        print("this is a constructor")

example = Example()
class Person:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
    # def __str__(self):
    #     return self.name
    def __repr__(self):
        return str(self.age)
    def __add__(self, other):
        return self.age+other.age
    def __len__(self):
        return 5
person2 = Person("mason",14)
person=Person("Daniel",14)
# print(person+person2)
print(person)
# print(len(person))
person3 =Person(20,"ryan")
print(person3)
