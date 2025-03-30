print("hello world")
x=134.2454
print(type(x))
def add(a,b):
    return a+b
result = add(5,6)
print(result)
def subtract(a,b):
        return a-b
result2 = subtract(10,5)
print(result2)
print(type(result2))
def addition(a,b):
    # print("the sum of", a,"+",b,"is",a+b
    print(f"the sum of {a},{b} is {a+b}")
def multiplication():
    a=input("please enter the first number")
    b=input("please enter the second number")
    print(f"the multiplication of {a}, and {b} is {int(a)*int(b)}")
# multiplication()
def number_check():
    a=input("please enter any number")
    if int(a)>0:
        print(f"{a} is a positive number")
    elif int()==0:
        print(f"{a} is the number 0")
    else:
        print(f"{a} is a negative number")
# number_check()
def weather_check():
    weather=input("what is the current weather, sunny, cloudy, foggy,snowing: ")
    match weather:
        case "sunny":
            print("carry your cap because its a sunny day")
        case "cloudy":
            print("no need for a cap because its cloudy")
        case "foggy":
            print("carry a light with you because its foggy")
        case "snowing":
            print("say inside because its snowing")
        case _:
            print("this weather does not exist")
# weather_check()
def gender_check():
    gender=input("please enter your gender, He or She: ")
    message= "You are a male" if gender=="He" else "you are a female"
    print(message)
gender_check()
# addition(3,5)


