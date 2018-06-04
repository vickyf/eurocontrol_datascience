import numpy as np
from sklearn.preprocessing import Normalizer

X=np.array([[1.,4.5],[10.4,7.2],[2.4,9.1]])
scaler = Normalizer()
normalized_X = scaler.fit_transform(X)
print(X)
print()
print(normalized_X)
print()
print(np.isclose(np.linalg.norm(normalized_X,axis=1), 1.0))