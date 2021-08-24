import pandas as pd

s1 = pd.Series([1,2,3,4,5])

print(s1)
print(type(s1))

s1 = pd.Series([1,2,3,4],index=["a","b","c","d"])

print(s1)

s2 = pd.Series({"jan":"january","feb":"february","mar":"march"})

print(s2)

s2 = pd.Series({"jan":"january","feb":"february","mar":"march"},index=["mar","jan","feb"])

print(s2)

s2 = pd.Series({"jan":"january","feb":"february","mar":"march"},index=["1","2","3"])

print(s2)


print(s1[1:])
print(s1[:-1])
print(s1[1:3])

print(s1)
print(s1+5)
print(s1*2)
print(s1/3)

s2  = pd.Series([10,20,30,40],index=["a","b","c","d"])

print(s1,s2)
print(s1+s2)

#################
# Data Frame
###########

my_data = pd.DataFrame({"Name":["Raam","Ravi","Ajay"],"Marks":[100,200,300]})
print(my_data)


sample_data = pd.read_csv('sample_data.csv')

print(sample_data.head()) # first five records
print(sample_data.tail())  #last five records
print(sample_data.shape)  #row coloumn

print(sample_data.describe())

print(sample_data.iloc[:4,:3])

print(sample_data.iloc[:7,3:7])  # (row,column)

print(sample_data.loc[0:3,("STATUS","UNITS")])

print(sample_data)
data1 = sample_data.drop('Period',axis=1)
print(data1.head())

print(sample_data)
data2 = sample_data.drop([1,2,3,4],axis=0)
print(data2.head())

data3 =sample_data.loc[0:3,("Period")]
print(data3.mean())
print(data3.median())
print(data3.std())

### Apply Function

def half_data(data):
    return data * 0.5 

print(sample_data.head())
data4 = sample_data[["Period","Data_value"]].apply(half_data)
print(sample_data.head())
print(data4.head())

#####

print(sample_data["Period"].value_counts())

print(sample_data.sort_values(by="Period"))

##############################










# print(sample_data.head())

# print(sample_data.drop([3,4,5],axis=0))
# print(sample_data.head())








