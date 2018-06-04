import pandas as pd
import numpy as np

index = ['a','b','c','d','e']
s = pd.Series(np.random.randint(0,100,5),index, name='integers')
l = ['Blue','Red','Yellow','Green','Black']

df1 = pd.DataFrame({'A': s, 'B':l})
print(df1)