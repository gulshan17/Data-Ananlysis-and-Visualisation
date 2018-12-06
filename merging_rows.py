#merging on indexes
#remember join occurs on index whereas merge occurs on columns
import pandas as pd
import numpy as np
from pandas import DataFrame

df1 = DataFrame({'reference' : ['O','U', 'L', 'O', 'U'], 'data ' : range(5)})
print(df1)

df2 = DataFrame({'profit' : [10, 20]}, index =  ['O', 'U'])
print(df2)

print(pd.merge(df1, df2, left_on = 'reference', right_index = True))

df3 = DataFrame({'ref1' : ['A', 'A', 'O', 'O', 'A'],
                'ref2' : [5, 10, 15, 20, 25],
                'ref3' : [0, 1, 2, 3, 4] })
print(df3)
df4 = DataFrame(np.arange(10).reshape(5, 2), index = [['A', 'A', 'O', 'O', 'O'], [20, 10, 10, 10, 20]], columns = ['col1', 'col2'])
print(df4)

print(pd.merge(df3, df4, left_on = ['ref1', 'ref2'], right_index = True))

#join function instead of merge because it's complex

df4 = DataFrame({'ref1' : ['A', 'A', 'O', 'O', '0'],
                'ref2' : [15, 20, 25, 30, 35],
                'ref3' : [2, 3, 4, 5, 6] })
print(df3.join(df4, lsuffix = 'x', rsuffix = 'y'))