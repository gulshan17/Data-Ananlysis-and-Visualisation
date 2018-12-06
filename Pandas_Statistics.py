from pandas import Series, DataFrame
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt

array1 = np.array([[10, np.nan, 20], [30, 40, np.nan]])
print(array1)

df1 = DataFrame(array1, index = [1, 2], columns = list('ABC'))
print(df1)

print(df1.sum())
print(df1.sum(axis = 1))

print(df1.min())
print(df1.max())

print(df1.idxmax())
print(df1.cumsum())
print(df1.describe())

df2 = DataFrame(randn(9).reshape(3, 3), index = [1, 2, 3], columns = list('ABC'))
print(df2)

plt.plot(df2)
plt.legend(df2.columns, loc = 'lower right')
plt.savefig('samplegraph.png')
plt.show()

ser1 = Series(list('aabbccaabd'))
print(ser1.unique())

print(ser1.value_counts())

#Additional learn covariance and correlations