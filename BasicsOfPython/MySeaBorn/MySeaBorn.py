import seaborn as sns
from matplotlib import pyplot as plt

fmri = sns.load_dataset("fmri")
print(fmri.head())

# sns.lineplot(x = "timepoint",y = "signal",data = fmri)
# plt.show()
##########################
# plt.subplot(2,1,1)
# sns.lineplot(x = "timepoint",y = "signal",data = fmri,hue = "event",style ="event",markers=True)


# plt.subplot(2,1,2)
# sns.lineplot(x = "timepoint",y="signal",data=fmri)
# plt.show()

############################
# Bar Plot
############

# sns.set(style="whitegrid")
# sns.barplot(x="timepoint",y="signal",data = fmri,hue="event")
# plt.show()

###############

# sns.set(style="whitegrid")
# sns.barplot(x="timepoint",y="signal",data = fmri,palette = "Blues_d")   # palette = rocket 
# plt.show()

# sns.set(style="whitegrid")
# sns.barplot(x="timepoint",y="signal",data = fmri,color="green")   # palette = rocket 
# plt.show()

#####################
# Scatter Plot

###################

# plt.subplot(2,2,1)
# sns.scatterplot(x = "timepoint", y = "signal", data = fmri)

# plt.subplot(2,2,2)
# sns.scatterplot(x="timepoint",y = "signal",data = fmri,hue = "event",style="event")
# plt.show()

###############
# Histogram/Distplot

###########

# plt.subplot(3,2,1)
# sns.distplot(fmri["signal"])
# plt.subplot(3,2,2)
# sns.distplot(fmri["signal"],hist = False)

# plt.subplot(3,2,3)
# sns.distplot(fmri["signal"],color="red")

# plt.subplot(3,2,5)
# sns.distplot(fmri["signal"],kde = False,bins=30)

# plt.subplot(3,2,6)
# sns.distplot(fmri["signal"],kde = False,bins=30,vertical=True)
# plt.show()

#######################
## Joint Plot = Scatter + Histogram
###############


# sns.jointplot(x="timepoint",y="signal",data = fmri,kind="reg",color="green")
# plt.show()

###############
# BoxPlot
#############

#sns.boxplot(x="timepoint",y="signal",data=fmri,palette = "Set1",linewidth=2,hue="event")

# plt.subplot(1,2,2)
# sns.boxplot(x="subject", y="event",data= fmri)
#plt.show()

#############
# Pair Ploat
############

sns.pairplot(fmri,hue="event")
plt.show()

####################################











