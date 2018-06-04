%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

#simple plot
x = np.arange(0,2*np.pi,0.1)
y_cos,y_sin = np.cos(x),np.sin(x)

plt.subplot(2,2,1)
plt.plot(x,y_sin,color = "blue")
plt.plot(x,y_cos,color = "red", linewidth = 3, linestyle = '--')
plt.title('Simple plot')
plt.xticks(())
plt.yticks(())

#scatter plot
n = 1024
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)

plt.subplot(2,2,2)
plt.scatter(x,y, s = 0.5, color = 'brown')
plt.title('Scatter plot')
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.xticks(())
plt.yticks(())

#pie plot
n=20
z=np.random.uniform(0, 1, n)

plt.subplot(2,2,3)
plt.pie(z, colors = ['%f' % (i/float(n)) for i in range(n)])
plt.title('Pie plot')
plt.axis('equal')

#bar plot
n = 12
x = np.arange(n)
y = (1 - x / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.subplot(2,2,4)
plt.bar(x,y, facecolor='purple')
plt.title('Bar plot')
plt.xticks(())
plt.yticks(())

plt.show()