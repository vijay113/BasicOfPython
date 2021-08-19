
def my_first_function():
    print("Hey. this is my first function.")

    print("Bye")

print("start process")
my_first_function()
print("End Process")

##################################
def my_function_with_Param(user,age):
    print("Hello "+ user + ", your age is "+ age)

my_function_with_Param("ravi","23")
my_function_with_Param("Ajay","30")

#################################

def my_multiple_of_num(num1, num2):
    result = num1 * num2
    print("num are: "+ str(num1) +","+ str(num2) )
    return result

num1 = input("first number:")
num2 = input("second number:")
result = my_multiple_of_num(float(num2),float(num1))
print("mulitple is :" + str(result))

########################################


