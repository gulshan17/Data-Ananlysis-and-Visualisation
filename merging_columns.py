import pandas as pd
import numpy as np
from pandas import Series, DataFrame

df1 = DataFrame({'reference' : ['ola', 'uber', 'lyft', 'gojak', 'grab'], 'revenue' : [17, 2, 3, 4, 5]})
df2 = DataFrame({'reference' : ['ola', 'uber', 'uber', 'ola'], 'revenue' : [17, 2, 3, 4]})

print(df1)
print(df2)

print(pd.merge(df1, df2))
df3 = pd.merge(df1, df2, on = 'reference')
print(df3)

df4 = pd.merge(df1, df2, on = 'reference', how = 'left')
print(df4)

df5 = pd.merge(df1, df2, on = 'reference', how = 'outer')
print(df5)

#many to many merging

df6 = DataFrame({'reference' : ['ola', 'ola', 'lyft', 'lyft', 'uber', 'uber', 'ola'], 'revenue' : [17, 2, 3, 4, 5, 6, 7]})
df7 = DataFrame({'reference' : ['uber', 'uber', 'lyft', 'ola', 'ola'], 'revenue' : [17, 2, 3, 4, 5]})
print(df6)
print(df7)

print(pd.merge(df6, df7))

#multiple references
df8 = DataFrame({'reference' : ['ola', 'ola', 'lyft'], 'revenue' : ['one', 'two', 'three'], 'profit' : [1, 2, 3]})

df9 = DataFrame({'reference' : ['ola', 'ola', 'lyft', 'lyft'], 'revenue' : ['one', 'one', 'one', 'three'], 'profit' : [4, 5, 6, 7]})

print(pd.merge(df8, df9, on = ['reference', 'revenue'], how = 'outer'))
print(pd.merge(df8, df9, on = ['reference', 'revenue'], how = 'outer', suffixes = ['_first', '_second']))
print(pd.merge(df8, df9, on = ['reference', 'revenue'], how = 'outer', suffixes = ('_first', '_second')))