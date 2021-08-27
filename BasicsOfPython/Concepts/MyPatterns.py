
import numpy as np

print("Hello, Patterns:")

d1 = np.array(range(10,-1,-1))
print(d1)

#######################
# Triangle
################


def pattern(n):
    k = 2 * n - 2
    for i in range(0,n):
        for j in range(0,k):
            print(end = " ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ",end = " ")
        print("\r")

pattern(10)

#########################################
# reverse triangle
############################

def pattern_reverse(n):
    k = 2 * n - 2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k = k + 1
        for j in range(0,i+1):
            print("* ",end=" ")
        print("\r")

print("Reverse Triangle:\n")
pattern_reverse(10)

####################
# Right Start Pattern
##########

def right_start_pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end=" ")
        print("\r")
    for i in range(n,-1,-1):
        for j in range(0,i+1):
            print("* ",end=" ")
        print("\r")

print("Right Start Pattern:")    
right_start_pattern(10)

##########################
# Left Start Pattern
################

def left_start_pattern(n):
    k = 2*n-2
    for i in range(0,n-1):
        for j in range(0,k):
            print(end= " ")
        k = k - 2 
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
    k = k -1
    for i in range(n-1,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k = k + 2
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
        
print("Left Start Pattern:")
left_start_pattern(10) 

############################
# Hourglass
###############

def half_piramind(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")

print("Half Piramind pattern:")
half_piramind(10)

#####################################
# number pattern
############################

def num_pattern(n):
    x = 0
    for i in range(0,n):
        x = x + 1
        for j in range(0,i+1):
            print(str(x)+" ",end=" ")
        print("\r")

print("Number Pattern:")
num_pattern(9)

#######################################



        


