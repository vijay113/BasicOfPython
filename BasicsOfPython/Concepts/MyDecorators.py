# def function1(function):
#     def wrapper(*arg,**warg):
#         print("Hello")
#         function()
#         print("Thank you.")
#     return wrapper

# def function2():
#     print("Welcome")

# function2 = function1(function2)

# print(function2())


################################

def function1(function):
    def wrapper(*arg,**warg):
        print("Hello")
        function()
        print("Thank you.")
    return wrapper

# decorator
@function1
def function2():
    print("Welcome")


print(function2())

########################################
# Fancy Decorator :- Class - static method
########################

class Square:
    def __init__(self,side):
        self._side = side

    @property
    def side(self):
        return self._side
   
    @side.setter
    def side(self,value):
        if value > 0:
            self._side = value
        else:
            print("error")

    @property
    def area(self):
        return self._side **2

    @classmethod
    def unit_square(cls):
        return cls(1)


s = Square(5)
print(s.area)
print(s.side)



    
    







