#KDE - Kernel Density Estimate

from __future__ import division
import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

#manually create KDE by summing the gaussian distribution
ds = randn(100)
#sns.rugplot(ds)
#plt.hist(ds, alpha = 0.5)
#plt.ylim(0, 1)
#plt.savefig('image1.png')

#x_axes = np.linspace(ds.min() - 1, ds.max() + 1, 50)

#bandwidth creation
#bandwidth = ((4 * ds.std() ** 5) / (3 * len(ds))) ** 0.2

#kernels = []

#for point in ds:
#     kernel = stats.norm(point,bandwidth).pdf(x_axes)
#     kernels.append(kernel)

#     kernel = kernel / kernel.max()
#     kernel = kernel * 0.6

     #plt.plot(x_axes,kernel,alpha=0.5,color="red")

#plt.ylim(0, 1)
#plt.savefig('image2.png')

#kde = np.sum(kernels, axis = 0)
#kde_fig = plt.plot(x_axes, kde, color = 'green')
#sns.rugplot(ds)
#plt.suptitle('KDE Plot')
#plt.savefig('image3.png')

#Using Seaborn shortcut
kdefig = sns.kdeplot(ds)
fig = kdefig.get_figure()
fig.savefig('image4.png')