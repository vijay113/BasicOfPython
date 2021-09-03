import copy

a = 5
b = a
b = b+1
print(a,b)


my_list = [1,2,3]
copy_list = my_list
copy_list[0]=100

print(my_list)
print(copy_list)
# both are changed.


##############################
# Shallow copy
######################

new_copy_list = my_list.copy()
#new_copy_list = list(my_list)
#new_copy_list = my_list[:]

new_copy_list[0]=-200




print(my_list)
print(new_copy_list)
# both not changed

##############################

# shallow copy - only one level

my_2d_list = [[1,2,3],[4,5,6]]
new_list = copy.copy(my_2d_list)
new_list[0][1]=-10

print(my_2d_list)
print(new_list)


# deep copy - for all level
my_2d_list = [[1,2,3],[4,5,6]]
new_list = copy.deepcopy(my_2d_list)
new_list[0][1]=-10

print(my_2d_list)
print(new_list)

##############################

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


p1 = Person("Ajay",30)
#p2 = p1
p2= copy.copy(p1)

p2.age = 50

print(p1.age)
print(p2.age)

##############################
################################









