import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from numpy import random

#numpy array
B1 = np.arange(25).reshape(5, 5)
A1 = random.randn(25).reshape(5, 5)
#print(B1)
#print(A1)

print(np.concatenate([A1, B1], axis = 1))
print('concatenate along row')
print(np.concatenate([A1, B1], axis = 0))

#Series
s1 = Series([100, 200, 300], index = ['A', 'B', 'C'])
s2 = Series([400, 500], index = ['D', 'E'])

print(pd.concat([s1, s2]))
print(pd.concat([s1, s2], axis = 1))

#DataFrame

df1 = DataFrame(random.randn(4, 3), columns = ['A', 'B', 'C'])
df2 = DataFrame(random.randn(3, 3), columns = ['B', 'D', 'A'])
print('pd concat dataframes')
print(pd.concat([df1, df2]))
print('pd.concat dataframe - continuous index')
print(pd.concat([df1, df2], ignore_index = True))

print('concat along column')
print(pd.concat([df1, df2], axis = 1))