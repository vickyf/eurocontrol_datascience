%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

mu1=20
sigma1=10
mu2=5
sigma2=3
mu3=0
sigma3=1

df = pd.DataFrame({'A':np.random.normal(mu1,sigma1,1000),
                   'B':np.random.normal(mu2,sigma2,1000),
                   'C': np.random.normal(mu3,sigma3,1000)})
scaler = MinMaxScaler()
scaled_df = pd.DataFrame(scaler.fit_transform(df),columns=['A','B','C'])

plt.figure(figsize=(12,8))
plt.subplot(1,2,1)
plt.title('Before scaling')
plt.hist(df['A'])
plt.hist(df['B'])
plt.hist(df['C'])
plt.subplot(1,2,2)
plt.title('After scaling')
plt.hist(scaled_df['A'])
plt.hist(scaled_df['B'])
plt.hist(scaled_df['C'])

plt.show()