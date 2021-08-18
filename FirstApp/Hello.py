# from math import *
# my_num = -5
# print(ceil(3.1))

from student import studentinfo
from student import teacherinfo

teacherinfo1= teacherinfo("teacher1","english")
nm = teacherinfo1.getname()
print(nm)
print("end")

# student1= studentinfo("vijay","001",200)
# student2= studentinfo("ramesh","009",'0')
# print(student1.getname())
# print(student2.name)

# employeefile = open("employee.txt",'r')

# print(employeefile.readlines())

# employeefile.close()




# try:
#     listarr= [
#     ["Ram","shyam","suresh","ravi"]
#     ,["Harish","sandeep"],
#     ["vijay","ajay","sonu"]
#     ,["geeta"]
#     ]

#     count = len(listarr)
#     print(listarr[4])
#     for ls in listarr:
#         for name in ls:
#             for letter in name:
#                 print(letter)
#             print(name)
# except IndexError as ex : 
#     print(ex)




# def raise_power(basenumber,powernumber):
#     result = 1
#     for index in range(powernumber):
#         result = result * basenumber
    
#     return result

# basenumber = input("Base number is: ")
# powernumber = input("power number is: ")

# result = raise_power(int(basenumber),int(powernumber))
# print("result is :"+ str(result))



# arr=["vijay","ajay","raam","shyam"]
# for index in range(len(arr)):
#     print(arr[index])

# print("done")

# i = 0
# while i<10:
#     print(i)
#     i= i+1
# print("DOne")

# months = {
# "JAN":"JANUARY",
# "FEB":"FEBRUARY",
# "MAR":"MARCH"
# }

# print(months.get("JAN"))


# is_student = 8
# is_programmer = 3
# if is_student > 9:
#     print("true")
# else : 
#     print ("false")



# print(5 + 4 * 3 / 3 * 2)

# name = input("ENter your name")
# age = input("enter your age")
# print("Hi %s your age %s" %(name,age))
# print(f"Hi {name} your age {age}")
# print("Hi {} your age {}" .format(name,age))

# msg = "Hello World"
# print(msg.replace('World','Titu'))



# print(msg)

# mystr= "Hello"
# myfloat = 10.0
# mynumber= 20
# if mystr == "Hello":
#     print("Str is %s" % mystr)
#     print('not str')
# if isinstance(myfloat,float) and myfloat == 10.0:
#     print('float : %f'% myfloat)

# if isinstance(mynumber, int) and mynumber == 20:
#     print("Integer: %d" % mynumber)    



# a,b = 3,4
# print(a,b)


# one = '1'
# two = '2'
# three = one + two
# print(three)

# three = one + " " + two
# print(three)


# num= 7.0
# num = float(num)
# print(num)




