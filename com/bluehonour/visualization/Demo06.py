import matplotlib.pyplot as plt
import seaborn as sns

# 直方图
titanic = sns.load_dataset("titanic")
sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic);
plt.show()