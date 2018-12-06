import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

mean = [0, 0]
covariance = [[1, 0], [0, 100]]

ds = np.random.multivariate_normal(mean, covariance, 500)
#print(ds)
dframe = pd.DataFrame(ds, columns = ['col1', 'col2'])
print(dframe)
fig = sns.kdeplot(dframe).get_figure()
fig.savefig('kde1.png')

#shape
fig2 = sns.kdeplot(dframe, shade = True).get_figure()
fig2.savefig('kde2.png')

#nadwidth change
fig3 = sns.kdeplot(dframe, bw = 1.1).get_figure()
fig3.savefig('kde3.png')

fig3 = sns.kdeplot(dframe, bw = 'silverman').get_figure()
fig3.savefig('kde3.png')

#kind variable
fig4 = sns.jointplot('col1', 'col2', dframe, kind = 'kde')
fig4.savefig('kde4.png')