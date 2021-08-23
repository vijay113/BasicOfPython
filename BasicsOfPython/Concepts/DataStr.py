
# Tuple -- emmutable means can not change value .

tuple1 = ('my hero', 20.3 ,[3.2,1,2])

print(tuple1[0])

print(tuple1[-1])

## Not Possible
# tuple1[0]= "hello"

print(tuple1)

print(tuple1[1:3])

tuple2 = (10,11,12)

print(tuple1 + tuple2)  # append into tuple1

print(tuple2 and tuple1)  

print(tuple2 * 10)

print(tuple1 * 2 )    # multiple elements of tuple

print(min(tuple2))

print(max(tuple2))

#print(min(tuple1))

#print(max(tuple1))

##############

# List

###########


my_list = [1,2,3,"hello",(1,2)]
print(my_list)

print(my_list[3:])

print(my_list[-1])

#print(max(my_list))

my_list[0]= 100

print(my_list)
my_list.append("Last")

print(my_list)

print(my_list.pop())

print(my_list.append(my_list.pop()))
my_list.reverse()

print(my_list)

my_list.insert(0,'start')

print(my_list)


#print(my_list.sort())

print(my_list *3)

my_list1 = [11,43,21,56]
print(my_list + my_list1)

########################

# Dictionary
##################

my_dictionary = {"jan":"january",
"feb":"february",
"mar":"march"
}

print(my_dictionary.get("jan"))

my_dictionary["apr"]="april"

print(my_dictionary.keys())

print(my_dictionary.values())

my_dictionary["jan"]="new year month"
print(my_dictionary.values())

my_dictionary1 = {"sun":"sunday",
"mon":"monday",
"tue":"tuesday"
}

my_dictionary.update(my_dictionary1)

print(my_dictionary)
print(my_dictionary1)

my_dictionary.pop('jan')
print(my_dictionary)

############################

# Set

# no index here
###############

my_set = {1,2,3,"hello",3,1}  # no duplicate possible

print(my_set)
my_set.add("5")
print(my_set)

my_set.remove(3)

print(my_set)

my_set.update([7,8,9])
print(my_set)

my_set1 = {1,2,3,8,10,11,12}

my_set.union(my_set1)

print(my_set.union(my_set1))

print(my_set.intersection(my_set1))

###############










