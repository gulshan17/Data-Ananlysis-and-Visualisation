import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn

series1 = Series([1, 2,3 ,4], index = ['e', 'f', 'g', 'h'])
print(series1)

#creating new indexex using reindex because we cannot reassign indexes directly
series2 = series1.reindex(['e', 'f', 'g', 'h', 'i', 'j'])
print(series2)

series2 = series2.reindex(['e', 'f', 'g', 'h', 'i', 'j', 'k'], fill_value = 10)
print(series2)

cars = Series(['BMW', 'Jaguar', 'Audi', 'Mercedes'], index = [0, 4, 8, 17])
print(cars)

ranger = range(21)
print(ranger)

cars = cars.reindex(ranger, method = "ffill") #forward fill
print(cars)

#dataframe using randn
df_1 = DataFrame(randn(25).reshape(5,5), index = ['a', 'b', 'c', 'd', 'e'], columns = ['c1', 'c2', 'c3', 'c4', 'c5'])
print(df_1)
#reindex row
df_2 = df_1.reindex(['a', 'b', 'c', 'd', 'e', 'f'])
print(df_2)

#reindex column
df_3 = df_2.reindex(columns = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6'])
print(df_3)

df_4 = df_1.loc[['a', 'b', 'c', 'd', 'e', 'f'], ['c1', 'c2', 'c3', 'c4', 'c5', 'c6']]
print(df_4)

print(df_1.ix[['a', 'b', 'c', 'd', 'e', 'f'], ['c1', 'c2', 'c3', 'c4', 'c5', 'c6']])