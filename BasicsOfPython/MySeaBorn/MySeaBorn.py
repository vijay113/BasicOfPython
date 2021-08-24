import seaborn as sns
from matplotlib import pyplot as plt

fmri = sns.load_dataset("fmri")
print(fmri.head())

# sns.lineplot(x = "timepoint",y = "signal",data = fmri)
# plt.show()
sns.lineplot(x = "timepoint",y = "signal",data = fmri,hue = "event")
plt.show()



