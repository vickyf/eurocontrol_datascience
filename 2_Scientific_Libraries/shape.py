import numpy as np

A = np.random.randint(0,11,size = (3,4))
B = np.random.randint(0,16,size = (3,4))
print(A)
print()
print(B)
print()
A.resize(2,6)
A = np.hsplit(A,(3,))[0]
B = B.T
B = np.vsplit(B,2)[1]
C = np.vstack((A,B))
print(C)