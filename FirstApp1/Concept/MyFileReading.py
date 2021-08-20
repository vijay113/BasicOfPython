
# try:
#     employee_file = open("Contents/Employees.txt","r")
#     #print(employee_file.read())    
#     #print(employee_file.readlines()[1])
#     for employee in employee_file.readlines():
#         print(employee)    
#     employee_file.close()
# except FileNotFoundError as err:
#     print(err)
# except:
#     print("Error occured.")

# #################################################
# # write a file
# ##############
# try:
#     employee_file = open("Contents/Employees1.txt","a")
#     print(employee_file.write("\nNew employee append."))    
#     employee_file.close()
# except FileNotFoundError as err:
#     print(err)
# except:
#     print("Error occured.")


#################################################
# Over-write a file
##############
try:
    employee_file = open("Contents/Employees1.txt","w")
    print(employee_file.write("\n<Html><head></head><p>This is new files</p></Html>."))    
    employee_file.close()
except FileNotFoundError as err:
    print(err)
except:
    print("Error occured.")



