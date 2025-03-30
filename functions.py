x=1
y=100#x and y are global variables
print(f" before function x is equal to {x}")
print(f"before function y is equal to {y}")
def outer_function ():
    print("this is my function")
    x=2
    y=200# x and y are in local scope
    print(f" inside function x is equal to {x}")
    print(f"inside function y is equal to {y}")
    def inner_function():
        x=3
        y=300
        print(f" inner function x is equal to {x}")
        print(f"inner function y is equal to {y}")
    inner_function()
outer_function()
print(f"after function called x is equal to {x}")
print(f"after function called y is equal to {y}")


def greet(salutation):
    print(f"{salutation} daniel")
greet("hello")


def division(x,y):
    return (x/y)
print(division(6,2))


mass =74.54
gravity =9.81
weight = mass*gravity
print(round(weight,2))
print()
