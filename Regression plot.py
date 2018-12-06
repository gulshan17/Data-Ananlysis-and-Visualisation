import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import statsmodels
import seaborn as sns

df  = sns.load_dataset('diamonds').sample(frac = 1).head(100)
print(df)

sns.lmplot('price', 'carat', df).savefig('1.png')

#using dictionary to edit  customize the plot
sns.lmplot('price', 'carat', df, scatter_kws = {'marker' : 'x', 'color' : 'green'}, line_kws = {'color' : 'red', 'linewidth' : 1}).savefig('2.png')

#higher order trend line
sns.lmplot('price', 'carat', df, order = 4, scatter_kws = {'marker' : 'x', 'color' : 'green'}, line_kws = {'color' : 'red', 'linewidth' : 1}).savefig('4.png')

#scatter plot without a trend line
sns.lmplot('price', 'carat', df, fit_reg = False).savefig('5.png')

#hue argument
sns.lmplot('price', 'carat', df, hue = 'cut', markers = ['^', 'v', '*', '.', 's']).savefig('6.png')

sns.lmplot('price', 'carat', df, hue = 'cut').savefig('7.png')

#local regression
sns.lmplot('price', 'carat', df, lowess = True).savefig('8.png')

#regplot
sns.regplot('price', 'carat', df).get_figure().savefig('9.png')

#sub plots
image, (plt1, plt2) = plt.subplots(1, 2, sharey = True)
sns.regplot('price', 'carat', df, ax = plt1).get_figure().savefig('10.png')
sns.boxplot(df['carat'], df['depth'], color = 'green', ax = plt2).get_figure().savefig('10.png')

