import numpy as np

my_list = [1,2,3,4]
my_np_arr = np.array(my_list)
print(my_np_arr)

print(type(my_np_arr))

my_arr=np.array([[1,2,3,4],[3,4,5,6]])

print(my_arr)

## Zeros function
my_arr = np.zeros((2,5))
print(my_arr)

## Full function
my_arr = np.full((2,5),10)
print(my_arr)

## arange function
my_arr = np.arange(20,50)
print(my_arr)


my_arr = np.arange(20,50,3)  # with gap of 3 
print(my_arr)





