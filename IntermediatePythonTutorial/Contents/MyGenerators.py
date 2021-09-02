 

def my_generator():
     yield 1
     yield 2
     yield 3

g = my_generator()

# print(g)
# value = next(g)
# print(value)

# value = next(g)
# print(value) 

#print(sum(g))

print(sorted(g))

##################################


def count_down(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1

cd = count_down(4)

value = next(cd)

print(value)

print(next(cd))
print(next(cd))

#################################

def first(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n :
        yield num
        num += 1
        

print(list(firstn_generator(10)))
print(sum(firstn_generator(10)))

print(first(10))
print(sum(first(10)))

import sys

print(sys.getsizeof(first(100000)))
print(sys.getsizeof(firstn_generator(100000)))
# size of generator is more less than a list


####################################

def fibonacci(limit):
     # 0 1 1 2 3 5 8 13 ....
     a,b = 0,1
     while a < limit:
         yield a
         a,b = b, a+b

fb = fibonacci(30)
print(list(fb))

########################

my_generator_1 = (i for i in range(100000) if i%2 == 0)
my_list = [i for i in range(100000) if i%2 == 0]
#print(list(my_generator_1))
#print(my_list)

print(sys.getsizeof(my_generator_1))
print(sys.getsizeof(my_list))
# see the difference of memory-size

##################################
# ############################## 



