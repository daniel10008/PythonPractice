from conditionals import result


def sum(n):
    x=0
    for i in range(1,n+1):
        x+=i
    return x



def sum_recursion(n):
    print(f"the exicution is happening for the number {n}")
    if n ==1:
        return n
    result = n+ sum_recursion(n-1)
    print(f"the result of the execution for the number {n} is {result}")

    return result

#print(sum_recursion(5))



#print(sum(5))
#factorial 5! = 5*4*3*2*1=120     5*4!
#factorial 4! = 4*3*2*1=24
def factorial(n):
    y=1
    for i in range(1,n+1):
        y*=i
    return  y


def factorial_recursion(n):
    if n==1:
        return n
    result = n* factorial_recursion(n-1)
    return result
print(factorial_recursion(9))

def reverse_recursion(name):
    if len(name)==0:
        return name
    reverse_recursion(name[1:])+name[0]


print(reverse_recursion("daniel"))

name = "daniel"
print(name[2:-1])
def reverse(name):
    reverse_name=""
    for i in range (len(name)-1,-1,-1):

        reverse_name +=  name[i]
    return reverse_name
print(reverse("daniel"))





def factorial_reverse(n):
    y=1
    for i in range(n,0,-1):
        y*=i
    return y
# print(factorial_reverse(5))
# print(factorial(5))