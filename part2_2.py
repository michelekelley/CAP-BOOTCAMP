#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 14:43:30 2017

@author: mk3g
"""

# get the equation for a Gaussian from the solutions to part I

# uncomment this line if you need to
from __future__ import division # make division act like python3 even if 2.7
import numpy.random as npr
import numpy as np

sigma=1.
throws=10000 # play with this number -- how many darts are enough?

# throw darts in box circumscribing portion of Gaussian of interest
# width is from -sigma to +sigma
xvals=(npr.random(throws) *2.0 *sigma - 1.*sigma)
# height is from 0 to peak value of Gaussian
yvals=(npr.random(throws) / (sigma*np.sqrt(2.*3.14159)))

# determine boundary of region as a function of x values
gaussfunct= np.exp((-1.*xvals**2)/(2.*sigma**2))/(sigma*np.sqrt(2.*3.14159))

# identify hits
hits=np.size(np.where(yvals <= gaussfunct))

# use equation area = (hits/throws) * rectangle area
rectarea = 2*sigma*max(yvals)
area = (hits/throws)*rectarea  # integer division here, watch out!

print("area is %s" % area)

plt.plot(xvals, yvals, '.')
plt.plot(xvals, gaussfunct, '.')

