import numpy as np
A = np.random.randint(0,11,size = (4,4))
print(A)
B = np.random.randint(0,11,size = (4,4))
print(B)
c = np.dot(A.sum(axis=0),np.sqrt(B.max(axis=1)))
print(c)