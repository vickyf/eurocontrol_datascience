import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy import stats as s

X = np.random.normal(6,4,(1000000,1))
scaler = StandardScaler()
standardized_X = scaler.fit_transform(X)
print(X[0:10,:])
print()
print(standardized_X[0:10,:])
print()
print(np.isclose(s.describe(standardized_X).mean,0))
print()
print(np.isclose(s.describe(standardized_X).variance,1))