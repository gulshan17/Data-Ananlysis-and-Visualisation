import pandas as pd
from pandas import Series
import numpy as np

#Series object from pandas
object = Series([5, 10, 15, 20])
#print(object)

#print(object.values)
print(object.index)

#use numpy array to create series
data_array = np.array(['a', 'b', 'c'])
s = Series(data_array)
print(s)

#custom indeex
s = Series(data_array, index = [100, 101, 102])
print(s)

s = Series(data_array, ['index1', 'index2', 'index3'])
print(s)


#using real life example

revenue = Series([20, 80, 40, 35], index = ['ola', 'uber', 'grab', 'gojack'])
print(revenue)

print(revenue['ola'])
print(revenue[revenue >= 35])

#use boolean conditions
print('ola' in revenue)
print('electric' in revenue)

#convert series into python dictionary
revenue_dict = revenue.to_dict()
print(revenue_dict)

#Nan value
index2 = ['ola', 'uber', 'grab', 'gojack', 'lyft']
revenue2 = Series(revenue, index2)
print(revenue2)

print(pd.isnull(revenue2))

print(pd.notnull(revenue2))

#addition of series
print(revenue + revenue2)

#assigning names
revenue2.name = 'Company Revenue'
revenue2.index.name = 'Company Name'
print(revenue2)
