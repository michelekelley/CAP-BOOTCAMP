#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 15:00:05 2017

@author: mk3g
"""

# uncomment this line if you need to
#from __future__ import division # make division act like python3 even if 2.7

import numpy.random as npr
import numpy as np
import matplotlib.pyplot as plt

# notes: probability distribution, its integral, and its reverse lookup
#### next 3 lines are pseudo-code, do not uncomment but use for reference
#### p_r=2.*3.14159*r / (3.14159*R**2)
#### intp_r=3.14159*r**2 / (3.14159*R**2)  =  r**2 for R=1
#### r_at_given_intp_r= ??? solve analytically on paper  ---> sqrt(intp_r)

# choose nran random numbers in uniform interval 0-1
nran = 1000
xrand = npr.random(nran)

# the integral of a uniform distribution p_u*dx (=1*dx) from 0 to x is just x
intp_uniform = xrand # rename variable for clarity

#the integrated areas must be the same across the transform
intp_r = intp_uniform  # rename variable for clarity
# solve for radius that gives the same integrated area under p_r
radvals = np.sqrt(intp_r) # use analytic solution you found above

# make a histogram
n1, bins1, patches1 = plt.hist(radvals,bins=50,normed=1,histtype='stepfilled')
plt.setp(patches1,'facecolor','g','alpha',0.75)

# insert code below stolen/modified from other codes

import random

DARTS=1000 # how many darts to you need to get a good, consistent estimate
radii=[]
for i in range (0, DARTS):
    x = random.uniform(-1,1) # square box circumscribes circle with radius 1
    y = random.uniform(-1,1)
    distsquared = x**2 + y**2 # taking the square root here would slow the code
    if distsquared <= 1.0:
        radii.append(np.sqrt(distsquared))
        
n1, bins1, patches1 = plt.hist(radii,bins=50,normed=1,histtype='stepfilled')
plt.setp(patches1,'facecolor','y','alpha',0.75)

