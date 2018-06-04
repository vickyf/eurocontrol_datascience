import numpy as np
a = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]])
b = a[0:2,0:2]
c = a[1,:]
d = a[np.arange(4),[2,0,1,0]]
e = a[[[0,0],[3,3]],[[0,2],[0,2]]]
f = a[a%2==0]

print(a)
print()
print(b)
print()
print(c)
print()
print(d)
print()
print(e)
print()
print(f)