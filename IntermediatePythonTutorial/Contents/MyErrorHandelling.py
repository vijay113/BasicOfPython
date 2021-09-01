# error and exception

###########
x = -5
#assert (x>0) , "x is not positive"
# if x <0:
#     raise Exception("x should be positive.")


#####################
try:    
    print("Hello")
    #z = 5/0
    #raise Exception("eror is throw.")
except ZeroDivisionError as ex:
    print("Zero devision error:",ex)
except TypeError as a:
    print("type error:",a)
except Exception as ex:
    print("general error:",ex)
else:
    print("all are okay")
finally:
    print("Clean all operation.")

#######################
# 
# ###############################

class CustomErrorHandle(Exception):
    pass

class Valuetoosmall(Exception):
    def __init__(self,message,value, *args: object) -> None:
        super().__init__(*args)
        self.message = message
        self.value = value

def test_value(x):
    if x>100:
        raise CustomErrorHandle("Value is too high")
    if x<10:
        raise Valuetoosmall("value is too short",20)


try:
    test_value(122)
except CustomErrorHandle as ex:
    print("error:",ex)
except Valuetoosmall as ex:
    print("error of small:",ex.message,ex.value)
else:
    print("all working")

##########################

