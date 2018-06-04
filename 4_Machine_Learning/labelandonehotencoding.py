import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

data = np.array(['cat', 'dog', 'cat', 'cat','guinea pig','dog','elephant','cat'])
labenc = LabelEncoder()
int_encoded = labenc.fit_transform(data)
print(int_encoded)
print()
OHenc = OneHotEncoder()
int_encoded = int_encoded.reshape(len(int_encoded),1)
OH_encoded = OHenc.fit_transform(int_encoded)
print(OH_encoded.toarray())