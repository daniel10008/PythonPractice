from time import time


def generator_function ():
    x =0
    while True:
       x+=1
       yield x
g=generator_function()
# while True:
#     y = input("do you need another ID: ")
#     if y.lower() == "yes":
#         print(next(g))
#     if y.lower() =="no":
#         break
def fibonacci_number(x):
    list_fibonacci =[0,1]
    for i in range(x):
       list_fibonacci.append(list_fibonacci[i]+list_fibonacci[i+1])
    print(list_fibonacci)
# fibonacci_number(20)
def fibonacci_number2(num):
    t1=time()

    y=1
    x=0
    m=0
    for i in range(num):
        print(x)
        m=y
        y+=x
        x=m
    t2=time()
    print(f"fibonacci_number2 took {t2-t1} seconds to exicute")
fibonacci_number2(21)
def fibonacci_number_generator():
    y=1
    x=0
    m=0
    while True:
            yield x
            m=y
            y+=x
            x=m
object_fibonacci =fibonacci_number_generator()
# while True:
#         response=input("do you want to get the next fibonacci number: ")
#         if response.lower()=="yes":
#             print(next(object_fibonacci))
def reading_file():
    file_template_path = "article.txt"
    try:
        with open(file_template_path) as letter_file:
            content = letter_file.read()
            print(content)
    except Exception as e:
        print(e)
# reading_file()
def reading_file_generator():
    file_template_path = "article.txt"
    try:

        with open(file_template_path) as letter_file:
            for line in letter_file:
                yield line.strip()
    except Exception as e:
        print(e)
obj_generator=reading_file_generator()
# while True:
#    user_input= input("do you want to read the next: ")
#    if user_input.lower()=="yes":
#        print(next(obj_generator))

