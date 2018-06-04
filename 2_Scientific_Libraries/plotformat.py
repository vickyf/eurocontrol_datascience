%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2*np.pi, 100)
y_sin, y_cos = np.sin(x), np.cos(x)

plt.plot(x,y_sin, color = 'Blue',label='sine')
plt.plot(x,y_cos, color = 'Red', linewidth = 3, linestyle = "--", label='cosine')
plt.title('Cosine and sine')
plt.legend(loc = 'lower left')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.xticks([0,np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
plt.yticks([-1,0,1])
plt.show()