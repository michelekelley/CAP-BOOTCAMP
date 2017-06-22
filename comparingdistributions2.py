#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:22:22 2017

@author: mk3g
"""

import pandas as pd
from astroML.plotting import hist
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KernelDensity
import scipy.stats as stats
import random 
#from tempfile import TemporaryFile

           
#Read in the file
url = 'https://raw.githubusercontent.com/capprogram/2017bootcamp-general/master/ECO_dr1_subset.csv'

df = pd.read_csv(url)  #df = dataframe

#Pull out the series of pandas data

Name = df.loc[:,'NAME']
cz = df.loc[:,'CZ']
logmstar = df.loc[:,'LOGMSTAR']
urcolor = df.loc[:,'MODELU_RCORR']


goodur = (urcolor > -99) & (logmstar > 10)
color = np.asarray(urcolor[goodur]) 

#plot the distribution of colors with different histogram bin widths
plt.figure(1)
plt.clf()
hist(color,bins='freedman',label='freedman',normed=1,histtype='stepfilled',color='green',alpha=0.5)
hist(color,bins='scott',label='scott',normed=1,histtype='step',color='purple',alpha=0.3,hatch='///')
# note the different format used below so as to save the bin info for Knuth's rule
n0, bins0, patches0 = hist(color,bins='knuth',label='knuth',normed=1,histtype='stepfilled',color='blue',alpha=0.3)
plt.xlim(0,3)
plt.xlabel("u-r color (mag)")
plt.title("Galaxy Color Distribution")
plt.legend(loc='best')





#add in the kde  
bw = (bins0[2]-bins0[1])/2 
colorkde= color[:, np.newaxis]
X = (colorkde)
X_plot = np.linspace(0, 3, 1000)[:, np.newaxis]
kde = KernelDensity(kernel='gaussian', bandwidth=bw).fit(X)
log_dens = kde.score_samples(X_plot)
plt.figure(1)
plt.plot(X_plot[:, 0], np.exp(log_dens), label='kde', color='m')
plt.legend(loc='best')








# this yields the index of the galaxies
nearby = (cz[goodur] > 5500.) # redshift is a proxy for distance
selenvnear = np.where(nearby)
selenvfar = np.where(~nearby)


plt.figure(2)
plt.clf()
hist(color[selenvnear],bins='knuth',label='near',normed=1,histtype='stepfilled',color='red',alpha=0.25)
plt.xlim(0,3)
xx = np.linspace(-2,16,10000)[:,np.newaxis]
kde = KernelDensity(kernel='gaussian',bandwidth=bw).fit(color[selenvnear][:,np.newaxis])
logdens = kde.score_samples(xx)
plt.plot(xx,np.exp(logdens),'r--')
hist(color[selenvfar],bins='knuth',label='far',normed=1,histtype='stepfilled',color='blue',alpha=0.25)
kde = KernelDensity(kernel='gaussian',bandwidth=bw).fit(color[selenvfar][:,np.newaxis])
logdens = kde.score_samples(xx)
plt.plot(xx,np.exp(logdens),'b--')






# Use the Kolmogorov-Smirnov and Mann-Whitney U tests to compare distributions
DD, pnullks = stats.ks_2samp(color[selenvnear],color[selenvfar])
UU, pnullmw = stats.mannwhitneyu(color[selenvnear],color[selenvfar])
plt.text(1.1, 1.7, "K-S pnull = %0.2g" % pnullks, size=14, color='b')
plt.text(1.1, 1.5, "M-W pnull = %0.2g" % pnullmw, size=14, color='b')
plt.xlabel("u-r color (mag)")
plt.legend()


print (DD, pnullks)
print (UU, pnullmw)


#now create a random selection
randomnum = np.asarray(random.sample(xrange(len(2*color)), len(color)))
savelastrn = randomnum




#coloreven = (randomnum%2 == 0)
#colorodd = (randomnum%2 != 0)
coloreven = (savelastrn%2 == 0)
colorodd = (savelastrn%2 != 0)
color1 = color[coloreven]
color2 = color[colorodd]



DDrand, pnullksrand = stats.ks_2samp(color1,color2)

print (DDrand, pnullksrand)

plt.figure(3)
hist(color1, bins = 'knuth', label='color1', normed=1, histtype = 'stepfilled',alpha =0.6, color='green')
hist(color2, bins = 'knuth', label='color2', normed=1, histtype = 'step', hatch = '//', alpha = 0.8, color='blue')
plt.title('Random Sample Color Comparison')
plt.xlabel('u-r color (mag)')
plt.legend()
