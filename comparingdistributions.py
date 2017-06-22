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
from tempfile import TemporaryFile
           
#Read in the file
url = 'https://raw.githubusercontent.com/capprogram/2017bootcamp-general/master/ECO_dr1_subset.csv'

df = pd.read_csv(url)  #df = dataframe

#Pull out the series of pandas data

Name = df.loc[:,'NAME']
cz = df.loc[:,'CZ']
logmstar = df.loc[:,'LOGMSTAR']
urcolor = df.loc[:,'MODELU_RCORR']


goodur = (urcolor > -99) 

"""
#Here do the cz histogram
plt.figure(1)
plt.title("Cz Histogram")

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



# Here plot the big stars   
plt.figure(2)
goodurbig = (urcolor > -99) & (logmstar > 10)
colorbig = np.asarray(urcolor[goodurbig])

plt.subplot(223)
counts, bins1, patches = hist(colorbig, bins='knuth',histtype='stepfilled', color = 'g')
plt.title('%s:%i bins' % ('knuth', len(counts)))

plt.subplot(222)
counts, bins, patches = hist(colorbig, bins='freedman',histtype='stepfilled', color='b')
plt.title('%s:%i bins' % ('freedman', len(counts)))

plt.subplot(224)
counts, bins, patches = hist(colorbig, bins='scott',histtype='stepfilled', color='r')
plt.title( '%s:%i bins' % ('scott', len(counts)))   

plt.subplot(221)
bw = (bins1[2]-bins1[1])/2. 
colorbigkde= colorbig[:, np.newaxis]
X = (colorbigkde)
X_plot = np.linspace(0, 3, 1000)[:, np.newaxis]
kde = KernelDensity(kernel='gaussian', bandwidth=bw).fit(X)
log_dens = kde.score_samples(X_plot)
plt.plot(X_plot[:, 0], np.exp(log_dens))
plt.title("Gaussian Kernel Density")



#Here plot the small logmstars

plt.figure(3)
goodursmall = (urcolor > -99) & (logmstar < 10)
colorsmall = urcolor[goodursmall]

plt.subplot(222)
counts, bins, patches = hist(colorsmall, bins='freedman',histtype='stepfilled', color='b')
plt.title( '%s:%i bins' % ('freedman', len(counts)))


plt.subplot(223)
counts, bins2, patches = hist(colorsmall, bins='knuth',histtype='stepfilled', color = 'g')
plt.title( '%s:%i bins' % ('knuth', len(counts)))


plt.subplot(224)
counts, bins, patches = hist(colorsmall, bins='scott',histtype='stepfilled', color='r')
plt.title( '%s:%i bins' % ('scott', len(counts)))  



plt.subplot(221)
bw = (bins2[2]-bins2[1])/2.
colorsmallkde= colorsmall[:, np.newaxis]
X = (colorsmallkde)
X_plot = np.linspace(0, 3, 1000)[:, np.newaxis]
kde = KernelDensity(kernel='gaussian', bandwidth=bw).fit(X)
log_dens = kde.score_samples(X_plot)
plt.plot(X_plot[:, 0], np.exp(log_dens))
plt.title( "Gaussian Kernel Density")      






color = np.asarray(urcolor[goodur]) 


#start the stats here
# redshift is a proxy for distance
nearby = (cz[goodurbig] > 5500.) 
faraway = (cz[goodurbig] < 5500.)
near = np.where(nearby)
far = np.where(faraway)


plt.figure(4)
plt.clf()
hist(color[near],bins='knuth',label='near',normed=1,histtype='stepfilled',color='red',alpha=0.25)
plt.xlim(0,3)
xx = np.linspace(-2,16,10000)[:,np.newaxis]
kde = KernelDensity(kernel='gaussian',bandwidth=bw).fit(color[near][:,np.newaxis])
logdens = kde.score_samples(xx)
plt.plot(xx,np.exp(logdens),'r--')
hist(color[far],bins='knuth',label='far',normed=1,histtype='stepfilled',color='blue',alpha=0.25)
kde = KernelDensity(kernel='gaussian',bandwidth=bw).fit(color[far][:,np.newaxis])
logdens = kde.score_samples(xx)
plt.plot(xx,np.exp(logdens),'b--')



DD, pnullks = stats.ks_2samp(color[near],color[far])
UU, pnullmw = stats.mannwhitneyu(color[near],color[far])
plt.text(1.1, 1.2, "K-S pnull = %0.2g" % pnullks, size=14, color='b')
plt.text(1.2, 1.0, "M-W pnull = %0.2g" % pnullmw, size=14, color='b')
plt.xlabel("u-r color (mag)")
plt.legend()        




#now create a random selection
#randomnum = np.asarray(random.sample(xrange(len(2*color)), len(color)))
#savelastrn = randomnum
np.savez('samplesplitting', savelastrn=savelastrn)


#These lines will save "savelastrn" to a file called gooddistribution (currently p=0.995)
#gooddistribution= TemporaryFile()
#np.save(gooddistribution, savelastrn)
#this one will load it in
input = np.load('samplesplitting.npz')
savelastrn = input['savelastrn']


#coloreven = (randomnum%2 == 0)
#colorodd = (randomnum%2 != 0)
coloreven = (savelastrn%2 == 0)
colorodd = (savelastrn%2 != 0)
color1 = color[coloreven]
color2 = color[colorodd]



DDrand, pnullksrand = stats.ks_2samp(color1,color2)

print (DDrand, pnullksrand)

plt.figure(5)
hist(color1, bins = 'knuth', label='color1', normed=1, histtype = 'stepfilled',alpha =0.6, color='green')
hist(color2, bins = 'knuth', label='color2', normed=1, histtype = 'step', hatch = '//', alpha = 0.8, color='blue')
plt.text(1.6, 0.9, "K-S pnull = %0.2g" % pnullksrand, size=14, color='b')
plt.title('Random Sample Color Comparison')
plt.xlabel('u-r color (mag)')
plt.legend()


































