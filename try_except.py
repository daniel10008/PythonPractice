try:
    age = input("how old are you: ")
    if int(age) <0:
        print("age must be more than 0")
        result =0
    else:
        result = 100/int(age)

except ZeroDivisionError:
    print("age must be greater than 0")
except ValueError:
    print("please enter your age as a number")
else:
    print(f"the result is: {result}")
finally:#else and finally are not mandatory
    print("this block will always execute")