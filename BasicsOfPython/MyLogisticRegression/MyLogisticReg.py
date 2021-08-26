######
# f(x) = exp(x)/(1+exp(x))
#######

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
color = sns.color_palette()
import sklearn.metrics as metrics
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import confusion_matrix, classification_report

from imblearn.over_sampling import SMOTE


import warnings

warnings.filterwarnings("ignore")

sample_data = pd.read_csv("sample_data.csv")

print(sample_data.head())

print(sample_data.shape)

print(sample_data.isnull().sum())

#################
# CountPlot
##############

# plt.figure(figsize=(10,5))
# plt.subplot(1,2,1)
# sns.countplot(sample_data["UNITS"])

# plt.subplot(1,2,2)
# sns.countplot(sample_data["STATUS"])
# plt.show()

####################
# Box Plot
#############

# print(sample_data["STATUS"].value_counts(normalize=True))

# sns.boxplot(sample_data["STATUS"],sample_data["Data_value"])
# plt.show()

#########################

# to change Catagory with number
# sample_data = pd.get_dummies(sample_data,drop_first=True)
# print(sample_data.head())

x= np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#y= np.array([0,0,1,0,0,1,0,0,1,0,0,1])
y= np.array([0,1,0,1,0,1,0,1,0,1,0,1])

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=21,stratify=y)

print("x_train:")
print(x_train)
print("x_test:")
print(x_test)

print("y_train:")
print(y_train)
print("y_test:")
print(y_test)

# # to extend sample data
# sm = SMOTE(random_state = 33,sampling_strategy=0.75)
# X_res,Y_res = sm.fit_sample(x_train,y_train)

# print("x_res:")
# print(X_res)
# print("y_res:")
# print(Y_res)

lr = LogisticRegression()

lr.fit(x_train.reshape(-1,1),y_train.reshape(-1,1))
y_predict = lr.predict(x_test.reshape(-1,1))

print("y_predict:")
print(y_predict)

mt = confusion_matrix(y_test,y_predict)
print(mt)
# mt = [[3 0][1 0]]
# accuracy_percentage = > (sum of right-diagnal)/(Sum of all)==>  (3+0)/(3+0+1+0) = 3/4 = 0.75 ==> 75 %

########################################









