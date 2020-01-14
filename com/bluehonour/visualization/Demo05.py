import matplotlib.pyplot as plt
import seaborn as sns

# 折线图
fmri = sns.load_dataset("fmri")
sns.relplot(x="timepoint", y="signal", hue="event", kind="line", data=fmri);
plt.show()

# 更多关于 seaborn 的可以看看以下链接
# https://seaborn.pydata.org/index.html


