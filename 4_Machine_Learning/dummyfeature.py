from sklearn.preprocessing import add_dummy_feature
import numpy as np

X=np.array([[1.,4.5],[10.4,7.2],[2.4,9.1]])
Y=add_dummy_feature(X,7.5)
print(Y)