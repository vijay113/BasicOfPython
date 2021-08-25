

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

matches = pd.read_csv("matches.csv")
#print(matches.head())

print(matches["season"].value_counts())
######################
for col in matches.columns:
    print(col)

###################  

print(matches["city"].value_counts()[0:5])

#plt.bar(list(matches["city"].value_counts()[0:5].keys()),list(matches["city"].value_counts()[0:5]))
#plt.show()  

############

# Top 10 teams those are won the toss as well as match

toss_match_winner = matches[matches["toss_winner"]==matches["winner"]]


print(toss_match_winner["toss_winner"].value_counts()[0:10])

plt.subplot(1,2,1)
plt.pie(list(toss_match_winner["toss_winner"].value_counts()[0:10]),labels=list(toss_match_winner["toss_winner"].value_counts()[0:10].keys()),autopct="%0.1f%%")

plt.subplot(1,2,2)
plt.bar(list(toss_match_winner["toss_winner"].value_counts()[0:10].keys()),list(toss_match_winner["toss_winner"].value_counts()[0:10]))
plt.show()

#####################################






