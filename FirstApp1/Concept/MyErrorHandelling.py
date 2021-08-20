
try:
    num = int(input("Enter a number"))
    print(num)
except:
    print("Invalid Number")


##########################

try:
    num = 10/0
    print("Number is "+num)
except ZeroDivisionError as err:
    print("divide by zero")
    print(err)
except:
    print("Change into String")

########################




