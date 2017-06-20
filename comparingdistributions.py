#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:22:22 2017

@author: mk3g
"""
import pandas as pd
import astroML
from astroML.plotting import hist
import matplotlib.pyplot as plt

def goodur():
    for x in xrange(len(urcolor)):
        if urcolor[x] < -99:
            del urcolor[x]
            del cz[x]
            del logmstar[x]
            del Name[x]
    return urcolor

def goodlogbig():
    for x in xrange(len(logmstar)):
        if logmstar[x] < 9 :
            del logmstar[x]
        
            
            
"""def goodlogsm():
    for x in xrange(len(logmstar)):
        if logmstar[x] > 10 :
            del logmstar[x]"""
           

url = 'https://raw.githubusercontent.com/capprogram/2017bootcamp-general/master/ECO_dr1_subset.csv'

df = pd.read_csv(url)  #df = dataframe


Name = df.loc[:,'NAME']
cz = df.loc[:,'CZ']
logmstar = df.loc[:,'LOGMSTAR']
urcolor = df.loc[:,'MODELU_RCORR']





#print len(cz)  #beginning number of stars

goodur()

#print len(cz)  #checks how many stars are left


plt.figure(1)
plt.subplot(221)
counts, bins, patches = hist(cz,histtype='stepfilled',color='m')
plt.text(3000, 2000, '%s:\n%i bins' % ('standard', len(counts)))
           

plt.subplot(222)
counts, bins, patches = hist(cz, bins='freedman',histtype='stepfilled', color='b')
plt.text(3800, 600, '%s:\n%i bins' % ('freedman', len(counts)))

plt.subplot(223)
counts, bins, patches = hist(cz, bins='knuth',histtype='stepfilled', color = 'g')
plt.text(3000, 500, '%s:\n%i bins' % ('knuth', len(counts)))

plt.subplot(224)
counts, bins, patches = hist(cz, bins='scott',histtype='stepfilled', color='r')
plt.text(3600,800, '%s:\n%i bins' % ('scott', len(counts)))


#Here do the big logmstars
goodlogsm()
    
plt.figure(2)

plt.subplot(221)
counts, bins, patches = hist(logmstar,histtype='stepfilled',color='m')
plt.text(3000, 600, '%s:\n%i bins' % ('standard', len(counts)))
           

plt.subplot(222)
counts, bins, patches = hist(logmstar, bins='freedman',histtype='stepfilled', color='b')
plt.text(3800, 200, '%s:\n%i bins' % ('freedman', len(counts)))

plt.subplot(223)
counts, bins, patches = hist(logmstar, bins='knuth',histtype='stepfilled', color = 'g')
plt.text(3200, 250, '%s:\n%i bins' % ('knuth', len(counts)))

plt.subplot(224)
counts, bins, patches = hist(logmstar, bins='scott',histtype='stepfilled', color='r')
plt.text(3600,300, '%s:\n%i bins' % ('scott', len(counts)))   


#Here reset to do small logmstars
Name = df.loc[:,'NAME']
cz = df.loc[:,'CZ']
logmstar = df.loc[:,'LOGMSTAR']
urcolor = df.loc[:,'MODELU_RCORR']


goodur()




plt.figure(3)
plt.subplot(221)
counts, bins, patches = hist(logmstar,histtype='stepfilled',color='m')
#plt.text(3000, 600, '%s:\n%i bins' % ('standard', len(counts)))
           

plt.subplot(222)
counts, bins, patches = hist(logmstar, bins='freedman',histtype='stepfilled', color='b')
#plt.text(3800, 200, '%s:\n%i bins' % ('freedman', len(counts)))

plt.subplot(223)
counts, bins, patches = hist(logmstar, bins='knuth',histtype='stepfilled', color = 'g')
#plt.text(3200, 250, '%s:\n%i bins' % ('knuth', len(counts)))

plt.subplot(224)
counts, bins, patches = hist(logmstar, bins='scott',histtype='stepfilled', color='r')
#plt.text(3600,300, '%s:\n%i bins' % ('scott', len(counts)))   

