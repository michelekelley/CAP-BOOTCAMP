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


"""def goodur():
    for x in xrange(len(urcolor)):
        if urcolor[x] < -99:
            del urcolor[x]
            del cz[x]
            del logmstar[x]
            del Name[x]
    return urcolor  """      

           
#Read in the file
url = 'https://raw.githubusercontent.com/capprogram/2017bootcamp-general/master/ECO_dr1_subset.csv'

df = pd.read_csv(url)  #df = dataframe

#Pull out the series of pandas data

Name = df.loc[:,'NAME']
cz = df.loc[:,'CZ']
logmstar = df.loc[:,'LOGMSTAR']
urcolor = df.loc[:,'MODELU_RCORR']


goodur = (urcolor > -99) & (logmstar > 10)
color = urcolor[goodur] 

plt.figure(1)
plt.clf()
hist(color,bins='freedman',label='freedman',normed=1,histtype='stepfilled',color='green',alpha=0.5)
hist(color,bins='scott',label='scott',normed=1,histtype='step',color='purple',alpha=0.5,hatch='///')
# note the different format used below so as to save the bin info for Knuth's rule
n0, bins0, patches0 = hist(color,bins='knuth',label='knuth',normed=1,histtype='stepfilled',color='blue',alpha=0.25)
plt.xlim(0,3)




"""hist(color,bins='freedman',label='freedman',normed=1,histtype='stepfilled',color='green',alpha=0.5)
hist(color,bins='scott',label='scott',normed=1,histtype='step',color='purple', hatch="///")
hist(color, bins='knuth',histtype='stepfilled', color = 'blue', hatch="///", alpha=0.3)"""
plt.xlim(0,3)
plt.xlabel("u-r color (mag)")
plt.title("Galaxy Color Distribution")
plt.legend(loc='best')

"""#Here create the arrays for the big and small stars 
logbig=[]
logsmall=[]
for x in xrange(len(logmstar)):
    if logmstar[x] < 9 :
        logsmall=np.append(logsmall, logmstar[x])
    else:
        logbig=np.append(logbig, logmstar[x])

logbigkde= logbig.reshape(-1,1)

#Here plot the big stars   
plt.figure(2)

plt.subplot(223)
counts, bins, patches = hist(logbig, bins='knuth',histtype='stepfilled', color = 'g')
plt.text(10.5, 530, '%s:\n%i bins' % ('knuth', len(counts)))


bw = (bins[2]-bins[1])/2 

plt.subplot(221)
X = (logbigkde)
X_plot = np.linspace(9, 13, 1000)[:, np.newaxis]
kde = KernelDensity(kernel='gaussian', bandwidth=bw).fit(X)
log_dens = kde.score_samples(X_plot)
plt.plot(X_plot[:, 0], np.exp(log_dens))
plt.text(9, 0.1, "Gaussian Kernel Density")


           

plt.subplot(222)
counts, bins, patches = hist(logbig, bins='freedman',histtype='stepfilled', color='b')
plt.text(10, 550, '%s:\n%i bins' % ('freedman', len(counts)))



plt.subplot(224)
counts, bins, patches = hist(logbig, bins='scott',histtype='stepfilled', color='r')
plt.text(10.2,530, '%s:\n%i bins' % ('scott', len(counts)))   


#Here plot the small logmstars


plt.figure(3)



#lt.subplot(221)
#counts, bins, patches = hist(logsmall,histtype='stepfilled',color='m')
#plt.text(7, 1400, '%s:\n%i bins' % ('standard', len(counts)))

logsmallkde = logsmall.reshape(-1,1)
X = (logsmallkde)





plt.subplot(223)
counts, bins, patches = hist(logsmall, bins='knuth',histtype='stepfilled', color = 'g')
plt.text(7.5, 200, '%s:\n%i bins' % ('knuth', len(counts)))

bw = (bins[2]-bins[1])/2 

plt.subplot(221)
X_plot = np.linspace(6, 9, 1000)[:, np.newaxis]
kde = KernelDensity(kernel='gaussian', bandwidth=bw).fit(X)
log_dens = kde.score_samples(X_plot)
plt.plot(X_plot[:, 0], np.exp(log_dens))
plt.text(6, 0.5, "Gaussian Kernel Density")      

plt.subplot(222)
counts, bins, patches = hist(logsmall, bins='freedman',histtype='stepfilled', color='b')
plt.text(7.5, 200, '%s:\n%i bins' % ('freedman', len(counts)))



plt.subplot(224)
counts, bins, patches = hist(logsmall, bins='scott',histtype='stepfilled', color='r')
plt.text(7,350, '%s:\n%i bins' % ('scott', len(counts)))  



goodur()
nearby = (cz[])
urcolornear=[]
urcolorfar=[]


            

#Here start the stats

ks = stats.ks_2samp(urcolornear, urcolorfar)
print  ks


mwu = stats.mannwhitneyu(urcolornear,urcolorfar)
print  mwu


plt.figure(4)
plt.hist(urcolornear, normed=1)
plt.hist(urcolorfar, normed=1, alpha=.3)




"""










































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
plt.text(3600,800, '%s:\n%i bins' % ('scott', len(counts)))"""


