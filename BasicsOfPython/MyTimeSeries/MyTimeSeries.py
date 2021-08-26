
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.seasonal import seasonal_decompose

from pylab import rcParams

my_data = pd.read_csv("AirPassengers.csv")

print(my_data.shape)
print(my_data)

my_data = pd.read_csv("AirPassengers.csv",parse_dates=["Month"],index_col="Month")

print(my_data.head())
print(my_data["1949-01-01":"1951-01-01"])


rcParams["figure.figsize"]=10,8
# my_data.plot()
# plt.show()

#####################
# If Seasonal is constant then use additive model
# otherwise if Seasoanl Is Not Constant then use Multiplicative model

# my_data_decompose = seasonal_decompose(my_data,model = "multiplicative")

# my_data_decompose.plot()
# plt.show()

###############
# we can change Multiplicative model into Additive model
#########################

my_data_log = my_data.copy()
my_data_log["#Passengers"] = np.log(my_data)
print(my_data_log.head)

plt.subplot(2,1,1)
plt.title("Data With Logs")
plt.plot(my_data_log)

plt.subplot(2,1,2)
plt.title("Original Data")
plt.plot(my_data)
plt.show()

##############################
###########################