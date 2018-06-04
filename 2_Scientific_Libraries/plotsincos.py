%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2*np.pi, 100)
y_sin, y_cos = np.sin(x), np.cos(x)

plt.plot(x,y_sin)
plt.plot(x,y_cos)
plt.show()