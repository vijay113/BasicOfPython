
import functools
# @mydecorator
# def do_something():
#     pass


def start_end_decorator(func):

    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@start_end_decorator
def print_name():
    print("Raam")
#print_name = start_end_decorator(print_name)

print_name()

#########################

def start_add_end(func):

    @functools.wraps(func)    # to fix Identity of this function
    def wrapper(*args,**kwargs):
        print("Start")
        res = func(*args,**kwargs)
        print("End")
        return res
    return wrapper

@start_add_end
def add_two_num(x,y):
    return x+y

print(add_two_num(10,20))

print(help(add_two_num))
print(add_two_num.__name__)

############################

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                result = func(* args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(F"hello {name}")


greet("Raam")

##############################
# nested decorators
################

def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

# def debug(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f'{k}={v!r}' for k,v in kwargs.items]
#         signature = ",".join(args_repr + kwargs_repr)
#         print(f"Calling {func.__name__}({signature})")
#         result = func(*args,**kwargs)
#         print(f"{func.__name__!r} returned {result!r}")
#         return result
#     return wrapper

# @debug
@start_end_decorator
def say_hello(name):
    greeting = f"Hello {name}"
    print(greeting)
    return greeting

#say_hello("AjayKumar")

############################
# Class Decorator
############################

class Count_Calls:

    def __init__(self,func):
        self.func = func
        self.num_calls = 0

    def __call__(self,*args,**kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)


@Count_Calls
def say_hello_1():
    print("Hello")


say_hello_1()
say_hello_1()

###############################
##################################