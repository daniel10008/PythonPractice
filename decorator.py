import time

def time_logger(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time=time.time()
        print(f"the execution time is {end_time-start_time:.6f} seconds")
        return result
    return wrapper


def type_check(func):
    def wrapper(*args,**kwargs):
        for arg in args:
            if type(arg)!=int:
                raise TypeError("unexpected type")
        return func(*args,**kwargs)
    return wrapper


@time_logger
def slow_function():
    time.sleep(5)
    print("function execution completed")
#slow_function()

@type_check
@time_logger
def add_function(a,b):
    return a+b
print(add_function(5,6))
print(add_function('j',6))