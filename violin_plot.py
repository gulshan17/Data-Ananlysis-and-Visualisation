import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

#violin plots are combination of box plot and kde plot

ds = randn(80)
#sns.violinplot(ds).get_figure().savefig('violin1.png')

#sns.violinplot(ds, bw = 0.2).get_figure().savefig('violin2.png')

sns.violinplot(ds, inner = 'stick').get_figure().savefig('violin3.png')

