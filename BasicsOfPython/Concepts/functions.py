def hello_world():
    print("Hello world.")

hello_world()


#########
# Lambda function

y = lambda x: print("hello Mr.",x)

y("vijay")

a = lambda x,y: (x+y)

result = a(10,20)
print(result)

##########
# filter function
############
my_list= [1,2,4,3,5,6,7]
result_list = list(filter(lambda x: (x%2 != 0),my_list))
print(result_list)

#############
# Map function

res_list = list(map(lambda x: x*2,my_list))
print(res_list)

################
# reduce function
from functools import reduce
re_list = reduce(lambda x,y: (x*y),my_list)

print(re_list)

#######################