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

my_arr = np.random.randint(100,500,10)
print(my_arr)
my_arr = np.random.randint(100,500,10)
print(my_arr)


# Shape function

my_arr = np.array([[1,2,3,4],[5,6,7,8]])
print(my_arr)

my_arr.shape=(4,2)
print(my_arr)

my_arr.shape = (8,1)
print(my_arr)

my_arr.shape = (1,8)
print(my_arr)

###  VStack , Hstack , colomn_stack

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

arr3 =np.vstack((arr1,arr2))
print(arr3)

arr4 = np.hstack((arr1,arr2))
print(arr4)

arr5 = np.column_stack((arr1,arr2))
print(arr5)

arr6 = np.row_stack((arr1,arr2))
print(arr6)

####
# INtersection and Difference

n1 = np.array([1,2,3,4,5])

n2 = np.array([3,5,8,9,0])

print(np.intersect1d(n1,n2))
print(np.setdiff1d(n1,n2))
print(np.setdiff1d(n2,n1))

### SUM
print(np.sum([n1,n2]))

print(np.sum([n1,n2],axis=0))

print(np.sum([n1,n2],axis=1))

## mathatical operation
print(n1+5)
print(n1 -2)
print(n1 * 2)

# mean operation

print(n1,n2)

print(np.mean(n1))
print(np.mean(n2))

# standard deviation and Median function

print(np.median(n1))

print(np.std(n1))

# Save and Load

n1 = [1,2,3,4,5]
np.save("my_arr_np",n1)

my_arr=np.load("my_arr_np.npy")
print(my_arr)

######################


#print(np.sta)













