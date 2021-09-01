
# Itertools : Product, Permutation, combinations, accumulate, group by

from itertools import accumulate, combinations, combinations_with_replacement, count, cycle, groupby, product, repeat

from itertools import permutations
import operator

a = [1,2,3]
b = [5,6]
prod = product(a,b)
print(list(prod))

prod1 = product(a,b, repeat=2)
print(list(prod1))

#######################
# Permutation
###################

a = [1,2,3]

perm = permutations(a,2)
print(list(perm))

perm = permutations(a)
print(list(perm))

#########################
# Combination
#################
a = [1,2,3]
comb = combinations(a,2)
print(list(comb))

com_wr = combinations_with_replacement(a,2)
print(list(com_wr))


###########################
# accumulate
##########################

a = [1,2,3,4]
acc = accumulate(a)
print(a)
print(list(acc))  # by default compute the SUM

acc_mul = accumulate(a,func=operator.mul)
print(list(acc_mul))

a = [1,2,4,3,10,7]
acc1 = accumulate(a,func=max)
print(list(acc1))

##################
# Group By
#######################

a = [1,2,3,4,5,6]
gr = groupby(a,key= lambda x: x<3)
for key,value in gr:
    print(key,list(value))

persons = [{"Name":"vijay","age":20},{"Name":"ajay","age":18},{"Name":"raam","age":20},{"Name":"Rajesh","age":18}]

gr1 = groupby(persons,key= lambda x: x["age"]<20)
for Key,Value in gr1:
    print(Key,list(Value))

##########################
# Count
##########################

for i in count(2):
    print(i)
    if i ==10:
        break;
#######################
a = [1,2,3]

for i in repeat(1,4):
    print(i)
########################
for i in cycle(a):
    print(i)
    if i == 3:
        break;

#############################


