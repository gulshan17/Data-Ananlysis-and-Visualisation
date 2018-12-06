import pandas as pd
import numpy as np
from pandas import Series, DataFrame

#example - Revenue of companies
revenue_df = pd.read_csv('D:\\Downloads\\countterm.csv')
#print(revenue_df)

#index and columns
print(revenue_df.columns)
#print(revenue_df['10'])

#print(DataFrame(revenue_df, columns = ['10', 'TOP', 'Profit']))
#revenue_df2 = DataFrame(revenue_df, columns = ['10', 'TOP', 'Profit'])
#print(revenue_df2)

#head and tail function
print(revenue_df.head())
print(revenue_df.tail(2))
print(revenue_df.shape)

#access row in df
print(revenue_df.loc[1]) #row

#assign values to dataframe
#numpy
array1 = np.array([1, 2, 3, 4, 5, 6, 1, 1, 2, 3, 4, 5, 6, 1,1, 2, 3, 4, 5, 6, 1,1, 2, 3, 4, 5, 6, 1, 17, 17, 17])
revenue_df['Profits'] = array1
print(revenue_df)

#series
profits = Series([1717, 17], index = [1, 2])
revenue_df['Profits'] = profits
print(revenue_df)

#deletion
print(revenue_df.drop('Profits', 1))

del revenue_df['Profits']
print(revenue_df)

#dictionary and dataframe
Sample = {'Comapny' : ['A', 'B'], 'Profit' : [1000, 5000]}

sample_df = DataFrame(Sample)

print(Sample)

print(sample_df)