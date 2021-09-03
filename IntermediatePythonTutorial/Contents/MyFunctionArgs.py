
def print_name(name):
    print(name)


print_name("vijay Kumar")

# arguments = values of parameters
# parameter = variable inside () of function.

def foo(a,b,c):
    print(a,b,c)

foo(a=1,b=2,c=3)
foo(c=3,a=1,b=2)
foo(1,b=2,c=3)
foo(1,2,c=3)
############################
def sample(a,b,c=7,d=4):
    print(a,b,c,d)

sample(1,2,3)
sample(c=3,b=2,a=1)
sample(a=1,b=3)

#############################

def sample_1(a,b,*args,**kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


sample_1(1,2,3,4,5,six = 6, seven = 7)
sample_1(1,2)
sample_1(1,2,six = 6,seven=7,eight= 8)
sample_1(1,2,3,4,5)

####################################

def sample_2(a,b,*,c,d):
    print(a,b,c,d)

sample_2(1,2,c=3,d=4)

############################
# keyword only args

def sample_3(*args,c ,d):
    for arg in args:
        print(arg)
    print(c,d)

sample_3(1,2,3,c=6,d=7)

#########################
# unpacked args

def sample_4(a,b,c,d):
    print(a,b,c,d)

my_list = [1,2,3,4]
sample_4(*my_list)

my_dictionary = {"a":1,"b":2,"c":3,"d":4}
sample_4(*my_dictionary)
sample_4(**my_dictionary)

my_dictionary = {"a":1,"b":3}
sample_4(**my_dictionary,c=5,d=2)

#######################################
# local n global args

def sample():
    global number
    x = number +1
    number = x +1
    print("number inside function:",x)

number = 0
sample()
print("Outside:",number)

################################
# value by reference Args

def sample_5(x):
    x=5

var = 10
sample_5(var)  # not change immutable type-int
print(var)

############################

def sample_6(my_list):
    # change the list
    my_list.append(4)
    my_list[0]=-100

def sample_7(my_list):
    # not change global list
    my_list = [100,200,300]
    my_list.append(4)
    my_list[0]=-100


def sample_8(my_list):
    # not change the globle list
    my_list = my_list + [100,200,300]
    my_list.append(4)
    my_list[0]=-100

def sample_9(my_list):
    # change the globle list
    my_list += [100,200,300]
    my_list.append(4)
    my_list[0]=-100


my_list = [1,2,3]
sample_6(my_list)  # change the list 
print(my_list)

my_list = [1,2,3]
sample_7(my_list) # not change the list
print(my_list)

my_list = [1,2,3]
sample_8(my_list) # not change the list
print(my_list)

my_list = [1,2,3]
sample_9(my_list) # change the list
print(my_list)


##########################
############################
