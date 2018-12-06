## OBJECTIVE
#importing csv as dataframe
#using readtable of pandas
#reading partial rows of a csv file
#dumping data into a new csv file
#selecting specific columns of a csv file

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df1 = pd.read_csv('D:\\Downloads\\demo.csv')
print(df1)

df1 = pd.read_csv('D:\\Downloads\\demo.csv', header = None)
print(df1)

#readtablle function
df1 = pd.read_table('D:\\Downloads\\demo.csv', sep = ',', header = None)
print(df1)

#partial row importing
print(pd.read_csv('D:\\Downloads\\demo.csv', nrows = 2, header = None))

df1.to_csv('D:\\Downloads\\output.csv', sep = '#')

#select specific columns
df1.to_csv('D:\\Downloads\\output.csv', columns = [0, 1])

