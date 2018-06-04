%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2*np.pi, 100)
y_sin, y_cos = np.sin(x), np.cos(x)

plt.subplot(1,2,1)
plt.plot(x,y_sin, color = 'blue',label='sine')
plt.title('Sine')
plt.xticks([0, np.pi, 2*np.pi])
plt.yticks([-1,0,1])

plt.subplot(1,2,2)
plt.plot(x,y_cos, color = 'red',label='cosine')
plt.title('Cosine')
plt.xticks([0, np.pi, 2*np.pi])
plt.yticks([-1,0,1])

plt.show()