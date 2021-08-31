my_list = ["Apple","Banana","Grapes","Cherry"]

print(my_list)

if "Banana" in my_list:
    print("Yes")
else:
    print("No")

#########################
# functions of list
############


new_list = sorted(my_list)
my_list.sort()
print(my_list)
print(new_list)

#######################

print(my_list[1:3])

print(my_list)

print(my_list[::-1])
##############################

my_new_list = my_list

my_list.append("JiRa")
print(my_list)

my_copy_list = my_list.copy()
my_list.append("LOve")

print(my_copy_list)

print(my_new_list)

##############################

#my_new_list1 = my_list.copy()
my_new_list1 = my_list[:]

my_list.append("hello")
my_new_list1.append("hi")
print("My List:")
print(my_list)
print("My New List:")
print(my_new_list1)

########################
# Tuple
########################

my_tuple=(1,2,3,5,6,7,8,9,10,11,12,13,14,15)

b = my_tuple[2:5]
print(my_tuple)
print(b)

b = my_tuple[2:14:2]
print(my_tuple)
print(b)

b = my_tuple[::-1]
print(my_tuple)
print(b)




################
tuple1= ("first","second","third")
first,second,third = tuple1
print(first)
print(second)
print(third)

my_new_tuple = (1,2,3,4,5,6,7,8,9,10)
first,*mid,last = my_new_tuple
print(first)
print(mid)
print(last)

#########################

import sys

my_tuple = (1,2,3,4,5,6,7,8,9,10,"Hello",True)
my_list = [1,2,3,4,5,6,7,8,9,10,"Hello",True]
print(sys.getsizeof(my_tuple),"bytes")
print(sys.getsizeof(my_list),"bytes")

if sys.getsizeof(my_tuple) > sys.getsizeof(my_list):
    print("memory occupation is more in tuple as compare to list")
else:
    print("list has more memory than tuple")    

##########################

import timeit

print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=100000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)",number=100000))
print("tuple creation is more fast than list.")

###################

my_tuple = tuple([0,1,2,3,4,5])
print(my_tuple)



###########################
##
# Dictionary
#########################

mydict = {"name":"vijay","age":"30","gender":"Male","phone":"123444"}

print(mydict)
for i in mydict.keys():
    print(i)
    print(mydict[i])

for Key,Value in mydict.items():
    print(Key,Value)

####################

mydict_copy = mydict
print(mydict_copy)

mydict_copy["Phone"] = "3040234"

print(mydict_copy)
print(mydict)

##############

mydict_copy = mydict.copy()
print(mydict_copy)
mydict["Phone"] = "1111134"
mydict_copy["Phone"] = "3040234"

print(mydict_copy)
print(mydict)

#########################
# update dictionary
######################

dic1 = {"first":"1","second":"2","third":"3","forth":"4"}
dic2 = dict(first= "10",second="20")

print(dic1)
dic1.update(dic2)
print(dic1)

#####################

my_dict = {10:0,20:2,40:4}
print(my_dict)
#print(my_dict[0])

my_dict = {"Jan":"January","feb":"february","mar":"march"}
print(my_dict)
print(my_dict["Jan"])
#################
# keys Types: tuple
############

mytuple1 = (0,1)
mytuple2 = (2,3)
mydict = {mytuple1:10, mytuple2:20}

print(mydict)

list1 = [0,1]
list2 = [2,3]
#mydict1 = {list1:10,list2:20}
#print(mydict1)
# List can not be a Key of dictionary.

#########################

### SET - unorder, mutable, no duplicate
#######################

myset = set("Hello")
myset = {1,2,3,4,5}
myset = {1,2,3,0,4,1,2}
print(myset)

####################

newset = set()
newset.add(1)
newset.add(2)
newset.add(3)
newset.add(4)

print(newset)
newset.remove(4)
newset.discard(1)
newset.pop()
print(newset)

########################

# Union, intersection
######################

odds = {1,3,5,7,9}
evens={2,4,6,8}
prime = {1,3,7,11}
odds_list = [1,3,5,7,9]
evens_list=[2,4,6,8]
prime_list = [1,3,7,11]
even_tuple = (2,4,6,8)

number = odds.union(evens)
number = odds.intersection(prime)

number = odds.union(evens_list)
number = odds.union(even_tuple)

number= odds.intersection(prime_list)
number = prime.difference(odds)
number = prime.symmetric_difference(odds)

print(number)

#odds.update(evens)
odds.intersection_update(prime)
print(odds)

print(odds.issubset(evens))
print(odds.issuperset(evens))
print(odds.isdisjoint(evens))
###################

set1 = {1,2,3}
set2 = {1,2}
set3 = set1
set3 = set1.copy()
set3.add(4)
print(set1)
print(set3)

########################
#
# Frozen Set - unmutable
############################

a = frozenset([1,2,3,4,5])
#a.add(7)
print(a)

b = a.copy()
print(b)
a.union(b)
print(a)
print(a.isdisjoint(b))

#####################################
########################################
