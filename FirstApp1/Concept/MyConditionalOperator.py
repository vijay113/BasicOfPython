

is_male = False

if is_male:
 print("User is male")
else:
    print("User is Female") 

###########################

is_Tall = True

if is_male or (is_Tall):
    print("user is male or tall or tall male.")
else:
    print("User is not tall male")    

########################
if is_male and not(is_Tall):
    print("user is sort male")
elif not(is_male):
    print("User is Female")
else:
    print("User is Tall Male")    


##################################


def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3 :
        return num1
    elif num2 >= num1 and  num2 >= num3:
        return num2
    else:
        return num3

print(max_num(1,2,0)) 

######################################



          




