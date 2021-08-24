
import numpy as np
from matplotlib import  colors, pyplot as plt
from numpy.lib.function_base import median


# x = np.arange(1,11)
# print(x)

# y = x *2
# plt.plot(x,y)
# plt.title("my_graph")
# plt.xlabel("x_values")
# plt.ylabel("y_values")
# plt.show()


# x = np.arange(1,11)
# print(x)
# y = x *3
# plt.plot(x,y,color = "g",linestyle = ":",linewidth = 2)
# plt.title("my_graph_1")
# plt.xlabel("x_values")
# plt.ylabel("y_values")
# plt.show()

########################################

# x = np.arange(1,11)
# print(x)

# y1 = x *2
# y2 = x *3

# plt.plot(x,y1,color = "g",linestyle = ":", linewidth = 2)
# plt.plot(x,y2,color="r",linewidth = 5)
# plt.title("x_y1_y2 graph")
# plt.xlabel("x values")
# plt.ylabel("y values")
# plt.grid(True)
# plt.show()

###############################
# x = np.arange(1,11)
# print(x)

# y1 = x *2
# y2 = x *3

# plt.subplot(1,2,1)
# plt.plot(x,y1,color = "g",linestyle = ":", linewidth = 2)
# plt.title("x_y1 graph")
# plt.xlabel("x values")
# plt.ylabel("y values")
# plt.grid(True)

# plt.subplot(1,2,2)
# plt.plot(x,y2,color="r",linewidth = 5)
# plt.title("x_y2 graph")
# plt.xlabel("x values")
# plt.ylabel("y values")
# plt.grid(True)
# plt.show()

###################

# Bar plot
################

# data = {"ravi":100,"ajay":200,"rahul":400}

# print(data)
# x = list(data.keys())
# y = list(data.values())

# #plt.bar(x,y)
# plt.barh(x,y,color ="g")
# plt.title("score bar graph")
# plt.xlabel("name")
# plt.ylabel("value")
# plt.grid(True)
# plt.show()

##########################
#Scatter plot
################

# x = [1,2,3,4,5]
# y= [10,12,23,10,20]
# z=[15,21,31,9,17]
# plt.scatter(x,y,marker="*",c="g",s=100)
# plt.scatter(x,z,marker=".",c="r",s=200)
# plt.show()

###########

# x = [1,2,3,4,5]
# y= [10,12,23,10,20]
# z=[15,21,31,9,17]

# plt.subplot(1,2,1)
# plt.scatter(x,y,marker="*",c="g",s=100)

# plt.subplot(1,2,2)
# plt.scatter(x,z,marker=".",c="r",s=200)
# plt.show()

###########################
# Histogram
#############################

# my_data = [1,1,2,2,2,3,3,4,5,6,6,6,7]

# plt.hist(my_data, color="r",bins=10)
# plt.show()

##########
import pandas as pd

# sample_data = pd.read_csv("sample_data.csv")

# print( sample_data.head())

# plt.hist(sample_data["Period"],bins = 30,color = "r")
# plt.title("data histogram")
# plt.xlabel("Period")
# plt.ylabel("frequency")
# plt.grid(True)
# plt.show()

#####################
# Box Plot
#########

# x1 = [1,2,3,4,5,6,7,8]
# x2 = [4,5,3,7,8]
# x3 = [5,6,8,9,3,0]
# d1= list([x1,x2,x3])
# print(d1)

#plt.boxplot(d1)
#plt.show()

###########
# Vielin Box 
######

#plt.violinplot(d1,showmedians = True)
#plt.show()

##############
# Pie Chart
######

# fruit = ["orange","mango","apple","banana"]
# quantity = [100,200,300,200]
# plt.pie(quantity,labels=fruit)
# plt.show()

# fruit = ["orange","mango","apple","banana"]
# quantity = [100,200,300,200]
# plt.pie(quantity,labels=fruit,autopct='%0.2f%%',colors=["Yellow","Red","Green","Blue"])
# plt.show()

##############
# DoughNut Chart

fruit = ["orange","mango","apple","banana"]
quantity = [100,200,300,200]
plt.pie(quantity,labels=fruit,autopct='%0.2f%%',colors=["Yellow","Red","Green","Blue"],radius=1)
plt.pie([10],colors=["White"],radius=0.3)
plt.show()

##################################















