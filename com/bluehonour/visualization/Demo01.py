import numpy as np
import matplotlib.pyplot as plt

# 参考该 https://matplotlib.org/2.0.2/contents.html
x = np.linspace(-2*np.pi, 2*np.pi, 256)

# 画画sin和cos线
cos = np.cos(x)
sin = np.sin(x)

plt.plot(x, cos, '--', linewidth=2)
plt.plot(x, sin)

plt.show()