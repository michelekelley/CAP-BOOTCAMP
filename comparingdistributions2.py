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

#Here start the stats



plt.figure(4)
plt.hist(color[selenvnear], normed=1)
plt.hist(color[selenvfar], normed=1, alpha=.3)




"""










































#Here do the cz histogram
plt.figure(1)
plt.subplot(221)
counts, bins, patches = hist(cz,histtype='stepfilled',color='m', alpha=0.3)
plt.text(3000, 2000, '%s:\n%i bins' % ('standard', len(counts)))
           
plt.subplot(222)
counts, bins, patches = hist(cz, bins='freedman',histtype='stepfilled', color='b', alpha=0.3)
plt.text(3800, 600, '%s:\n%i bins' % ('freedman', len(counts)))

plt.subplot(223)
counts, bins, patches = hist(cz, bins='knuth',histtype='stepfilled', color = 'g', alpha=0.3)
plt.text(3000, 500, '%s:\n%i bins' % ('knuth', len(counts)))

plt.subplot(224)
counts, bins, patches = hist(cz, bins='scott',histtype='stepfilled', color='r', alpha=0.3)
plt.text(3600,800, '%s:\n%i bins' % ('scott', len(counts)))

"""
