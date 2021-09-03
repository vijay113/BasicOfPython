
# multiplication

print(5 * 7)

# power operation

print(2 ** 4)

# list/tuple with repeat elements

print([1,2,3] * 10)

print((0,1) * 10)

print("AB "*5)

######################
#
def sample(a,b,*args,**kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in  kwargs:
        print(key, kwargs[key])

sample(1,2,4,5,6,seven = 7,eight=8) 

#####################

def sample_1(a,b,*,c):
    print(a,b,c)

sample_1(1,2,c=3)

my_dic = {"a":1,"b":2,"c":3}
sample_1(**my_dic)

################################

numbers = [1,2,3,4,5]

*first,last = numbers
print(first)
print(last)

first,*last = numbers
print(first)
print(last)

first,*middle,last = numbers
print(first)
print(middle)
print(last)


first,*middle,second_last,last = numbers
print(first)
print(middle)
print(second_last)
print(last)

###########################

my_tuple = (1,2,3,4)
my_list = [1,2,3,4,5,6]

my_set = {7,8,9}

new_list = [*my_tuple,*my_list,*my_set]
print(new_list)

###########################

dict_a = {"a":1,"b":2}
dict_b = {"c":3,"d":4}

new_dict = {*dict_a,*dict_b}
print(new_dict)

new_dict = {**dict_a,**dict_b}
print(new_dict)

#############################
###########################


