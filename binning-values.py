#binning -> process of separating elements into bins or categories

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#list
prime_no = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

number_bins = [0, 10, 20, 30, 40, 50]

category = pd.cut(prime_no, number_bins)

print(category)

print(category.categories)

#value_counts --> count the number values present in the dataframe

print(pd.value_counts(category))

#limits
print(pd.cut(prime_no, 3, precision = 1))

