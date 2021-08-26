from numpy import NaN
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


sample_data = pd.read_csv("sample_data.csv")

print(sample_data.head())
print(sample_data.columns)

# values of One perticular column of a dataset
my_data1 = sample_data["Period"]
print(my_data1.head())


# filter a Dataset from existing dataset with all columns
my_data = sample_data[["Period","Data_value","STATUS","UNITS","Magnitude","Subject","Group"]]
print(my_data.head())

my_filter_data = my_data[my_data["Period"] > 2017]
print(my_filter_data.head())
print(my_filter_data.shape)

###############
# plot scatter plot
################

# plt.subplot(1,2,1)
# sns.scatterplot(x="Period",y="Data_value",data=my_data)

# plt.subplot(1,2,2)
# sns.scatterplot(x="Data_value", y="Period",data=my_filter_data)
# plt.show()

#################################
# Plot Bar
############

# plt.subplot(1,2,1)
# sns.barplot(x="Period",y="Data_value",data=my_data)

# plt.subplot(1,2,2)
# sns.barplot(x="Data_value", y="Period",data=my_filter_data)
# plt.show()


#########################
# Linear Regression using SciKit-Learn 
###########################
# to know relationship between Period & Data_value in My_Data
# Dependent variable = Data_value
# independent variable = Period
# Data_value_y = Fn(Period_x)
############

# y = my_data[["Data_value"]]
# x = my_data[["Period"]]
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)  # Output-sequence is important

# print(x.head())
# print(y.head())
# print(x_train.head())
# print(x_test.head())
# print(y_train.head())
# print(y_test.head())

# my_model_lr = LinearRegression()

# my_model_lr.fit(x_train,y_train)

# y_predict = my_model_lr.predict(x_test)

# print(y_test.head())
# print(y_predict.hea())

# error = mean_squared_error(y_test,y_predict)
# print(error)


############################
# Model 2
#################

# y = my_data[["Data_value"]]
# x = my_data[["Period"]]

y = np.array([1,2,3,4,5,6,7])
x = np.array([10,20,30,40,50,60,70])

print(y)
print(x)

x_train,x_test,y_train,y_test = train_test_split(x.reshape(-1,1),y.reshape(-1,1),test_size=0.3)


print("X_Train:")
print(x_train)
print("X_Test:")
print(x_test)
print("Y_Train:")
print(y_train)
print("Y_Test:")
print(y_test)

lr2 = LinearRegression()
lr2.fit(x_train,y_train)
y_predict = lr2.predict(x_test)

print("y_predict:")
print(y_predict)
y1_error = mean_squared_error(y_test,y_predict)

print("Error :")
print(str(y1_error))

####################################







