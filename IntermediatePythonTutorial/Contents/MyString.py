##
## string :- immutable, ordered, text 
##

my_string = "Hello \
    world"

print(my_string)    

print(my_string[1:5])
print(my_string[:])
print(my_string[::])
print(my_string[::-1])
print(my_string[::2])
print(my_string[1:9:3])

#######################

my_string = "        Hello      world"
print(my_string)
print(my_string.strip())

print(my_string.endswith("ld"))

print(my_string.find("ld"))

print(my_string.count("l"))

print(my_string.replace("world","universe"))
print(my_string)

###############################

string1 ="Hows are you"
my_list = string1.split(" ")
print(string1)
print(my_list)

new_string = " ".join(my_list)
new_string = " ".join("This is you")
print(new_string)
#########################

my_list = ['Hello'] * 6
print(my_list)

########################
# formats:
# %, .formart(), f-string
###################
var = "Tom"
my_string = "the variable is %s" % var
print(my_string)

var = 100
my_string = "the variable is %d" % var
print(my_string)

var = 100
my_string = "the variable is %.2f" % var
print(my_string)

var = False
my_string = "the variable is %u" % var
print(my_string)

var = 2.343434
my_string = "the variable is {:.2f} and {}".format(var,var)
print(my_string)

var = 2.343434
var1 = 323.233
my_string = f"the variable is {var+2} and {var1}"
print(my_string)






