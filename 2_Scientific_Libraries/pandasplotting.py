%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a=[3,3,2,1,4,4,5,6,7,4,9,7,8,12,19,15,13,10,20,17,21,26,24,27,28,32,31,35,39,37,42]
b=[30,32,26,13,14,16,20,28,36,49,50,50,48,59,35,26,30,23,10,7,2,2,4,7,18,32,39,20,25,17,15]
dat = pd.date_range('2017-01-01', periods = 31, freq = 'D')
s1 = pd.Series(a, index = dat)
s2 = pd.Series(b, index = dat)
df = pd.DataFrame({'A':s1,'B':s2})

df.plot()
plt.show()

df.boxplot()
plt.show()

print(df.describe())