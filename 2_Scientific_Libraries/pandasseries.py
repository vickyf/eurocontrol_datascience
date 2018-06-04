import pandas as pd
import numpy as np

colours_list = ['Blue', 'Red', 'Green', 'Yellow', 'Black']
colours_dict = {'a':'Blue', 'b':'Red', 'c':'Green', 'd':'Yellow', 'e':'Black', 'f':'Purple'}
num_scal = 5
index = ['a', 'b', 'c', 'd', 'e']
s_list = pd.Series(colours_list, index)
s_dict = pd.Series(colours_dict, index)
s_scal = pd.Series(num_scal, index)
print(s_list[0])
print(s_dict['d'])
print(np.sum(s_scal))