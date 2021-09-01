from functools import reduce

# lambda args: expression

add10 = lambda x: x+10

print(add10(9))

def add10_1(x):
    return x+10

print(add10_1(9))

######################

mult = lambda x,y: x*y
print(mult(3,5))
#######################

a2D = [(1,2),(15,1),(5,-1),(10,4)]

point_2d_sorted = sorted(a2D)

print(a2D)
print(point_2d_sorted)

list_sortby_y = sorted(a2D,key= lambda x : x[1])

print(list_sortby_y)

list_sortby_sumofeach = sorted(a2D,key= lambda x: x[0]+x[1])

print(list_sortby_sumofeach)

##########################
# map(func,seq)

a =[1,2,3,4,5]
b = map(lambda x: x*2,a)
print(list(b))

print(2*a)

c = [x*2 for x in a]
print(c)

##################
# filter(func, seq)

filter_list = filter(lambda x: x%2==0,a)
print(list(filter_list))

c = [x for x in a if x%2==0]
print(c)

##################
# reduce(func,seq)

a = [1,2,3,4]

product_a = reduce(lambda x,y:x*y,a)
print(product_a)

########################
########################


