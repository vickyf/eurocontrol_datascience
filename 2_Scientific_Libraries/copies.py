import numpy as np
A = np.ones((3,4))
B = A
C = A[0:1,:]
D = A.copy()
B.resize(2,6)
C.resize(2,2)
D.resize(1,12)
B[0,0] = 2
C[0,1] = 3
D[0,2] = 4
print('A=', A)
print()
print('B=', B)
print()
print('C=', C)
print()
print('D=', D)