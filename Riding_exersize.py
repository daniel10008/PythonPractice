try:
    height = input("please enter how tall you are in cm: ")
    if int(height)>120:
        print("you are tall enough to ride")
        age =input("please enter your age: ")
        price =0
        if int(age)<12:
            price=5
        elif int(age)<=18:
            price = 7
        elif int(age)<45:
            price = 12
        elif 0 > int(age) > 55:
            print("invalid age")
        picture = input("do you want a picture yes or no: ")
        if picture=="yes":
            price+=3
        print(f"your total price is {price}")



    else:
        print(f"{height} cm is not tall enough to ride")
except Exception as e:
    print(e)
else:
    print("thank you visit again")
finally:
    print("this block will always execute")