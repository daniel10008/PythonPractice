def reverse_recursion(name):
    print(name)
    if len(name)==0:
        return name
    return reverse_recursion(name[1:])+name[0]



print(reverse_recursion("daniel"))
