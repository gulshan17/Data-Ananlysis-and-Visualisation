import numpy as np
import pandas as pd
from numpy.random import randn
import matplotlib as mlp
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('flights')
df2 = df.pivot('year', 'month', 'passengers')
print(df2)

#sns.clustermap(df2).savefig('cluster1.png')

#sns.clustermap(df2, col_cluster = False).savefig('cluster2.png')

#Standardization
#standard_scale = 0 means standardization by rows
sns.clustermap(df2, standard_scale = 0).savefig('cluster3.png')
sns.clustermap(df2, standard_scale = 1).savefig('cluster4.png')