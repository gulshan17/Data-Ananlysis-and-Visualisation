import numpy as np
import pandas as pd
from pandas import Series
from numpy.random import randn

series1 = Series([500, 1000, 1500], index = ['a', 'c', 'b'])
#sorting by index
print(series1.sort_index())

#sort by values
print(series1.sort_values())

print(series1.rank())

#ranking of series
series2 = Series(randn(10))
print(series2)

print(series2.rank())
print(series2.sort_values())

print(series2.rank())