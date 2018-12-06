import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = DataFrame(np.arange(25).reshape(5, 5), index = ['UBER', 'OLA', 'GRAB', 'GOJEK', 'Lyft'], columns = ['RE', 'LO', 'QU', 'GR', 'AG'])
print(df)

#way1->using mapping
df.index = df.index.map(str.lower)
print(df)

#way2 -> using rename method
#doesn't change the original data until inplace is used

print(df.rename(index = str.title, columns = str.lower))

#way3 --> using dictionaries
print(df.rename(index = {'uber' : 'The Best Taxi'}, columns = {'RE' : 'Revenue'}))

#to save in original using rename function
print(df.rename(index = {'uber' : 'The Best Taxi'}, columns = {'RE' : 'Revenue'}, inplace = True))
print(df)