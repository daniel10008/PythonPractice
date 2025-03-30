make_square= lambda value: value**2
max_lambda = lambda x,y: x if x>y else y
even_lambda = lambda x: "even" if x%2 ==0  else "odd"
print(even_lambda(5))
print(max_lambda(4,7))
print(make_square(5))
