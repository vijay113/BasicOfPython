import random

a = random.random()

a = random.uniform(1,10)
a = random.randint(1,10)
a = random.randrange(1,10)
a = random.normalvariate(0,1) # normal deviation number

my_list = list("ABCDEFGH")
print(my_list)
a = random.choice(my_list)
a = random.sample(my_list,2)
a = random.choices(my_list,k=2)

random.shuffle(my_list)
print(my_list)


print(a)

###########################

random.seed(1)
print(random.random())
print(random.randint(1,10))


random.seed(1)
print(random.random())
print(random.randint(1,10))


random.seed(2)
print(random.random())
print(random.randint(1,10))

random.seed(1)
print(random.random())
print(random.randint(1,10))

##################################
# Secrets module
###############

import secrets

a = secrets.randbelow(10)  # below under 10, 10 is not include.
a = secrets.randbits(4)   # 1111,1010,0000,1010,1001..etc
print(a)

my_list = list("ABCDEFGH")
a = secrets.choice(my_list)
print(a)

#############################
# NumPy

######################

import numpy as np

a = np.random.rand(3)

a = np.random.rand(3,3)

a = np.random.randint(0,10)
a = np.random.randint(0,10,(3,4))

print(a)
########################

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)

np.random.shuffle(arr)
print(arr)

np.random.seed(1)
print(np.random.rand(3,3))

np.random.seed(2)
print(np.random.rand(3,3))

np.random.seed(1)
print(np.random.rand(3,3))

############################
####################################







