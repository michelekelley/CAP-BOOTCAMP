#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:35:18 2017

@author: mk3g
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr
from astropy.stats import biweight_midvariance
from sklearn.metrics import mean_squared_error


narr = 100
xvals = np.linspace(1,10,narr)
yvals = np.linspace(20,40,narr)
xtrue =xvals
ytrue = yvals

#now add errors in y first normal, then random by hand ~10

yvals = yvals + npr.normal(0, 2, 100)

yvals[11] += 4 
yvals[15] += 5 
yvals[22] += 1 
yvals[37] += 5 
yvals[91] += 3 
yvals[55] += 5 
yvals[97] += 2 
yvals[4] += 5 
yvals[2] += 3 
yvals[63] += 4 

plt.figure(1)
plt.clf()
plt.plot(xvals,yvals, '.', color = 'green')
plt.xlabel("x-values")
plt.ylabel("y-values")
plt.title("Linear Fit Methods with Error in Y")
plt.plot(xtrue,ytrue, linestyle='--', color = 'orange', label='true')

###FORWARD FIT - based on y as dependent

alphaestf=(np.mean(xvals)*np.mean(yvals)-np.mean(xvals*yvals)) / \
         (np.mean(xvals)**2 -np.mean(xvals**2)) #  from derivation
betaestf= np.mean(yvals) - alphaestf*np.mean(xvals)

# The MLE values of the slope and y-intercept are equivalent to the "least
# squares" fit results.
print("analytical MLE slope = %0.7f" %alphaestf)
print("analytical MLE y-intercept = %0.7f" %betaestf)

# Overplot the MLE ("best fit") solution
yfitvals=xvals*alphaestf+betaestf
plt.plot(xvals,yfitvals,'r', label = 'forward --- "best"?')

# Compute analytic uncertainties on slope and y-intercept 

alphauncf = np.sqrt(np.sum((yvals - (alphaestf*xvals+betaestf))**2) / ((narr-2.)*(np.sum((xvals-np.mean(xvals))**2))))
betauncf = np.sqrt((np.sum((yvals - (alphaestf*xvals+betaestf))**2) / (narr-2.)) * ((1./narr) + (np.mean(xvals)**2)/np.sum((xvals-np.mean(xvals))**2)) )

print("analytical MLE uncertainty on alpha is %0.7f" % (alphauncf))
print("analytical MLE uncertainty on beta is %0.7f" % (betauncf))

print("fractional uncertainty on alpha is %0.7f" % (alphauncf/alphaestf))
print("fractional uncertainty on beta is %0.7f" % (betauncf/betaestf))
print"\n"

###INVERSE FIT - based on x as dependent  (inverse of the forward fit and switch x and y)

alphaesti = (np.mean(yvals)**2 - np.mean(yvals*yvals)) / \
            (np.mean(xvals)*np.mean(yvals) - np.mean(yvals*xvals))
betaesti = np.mean(yvals) - alphaesti*np.mean(xvals)

# The MLE values of the slope and y-intercept are equivalent to the "least
# squares" fit results.
print("analytical MLE slope = %0.7f" %alphaesti)
print("analytical MLE y-intercept = %0.7f" %betaesti)

# Overplot the MLE ("best fit") solution
yfitvals=xvals*alphaesti+betaesti
plt.plot(xvals,yfitvals,'b', label="inverse")

# Compute analytic uncertainties on slope and y-intercept 

alphaunci = np.sqrt(np.sum((yvals - (alphaesti*xvals+betaesti))**2) / ((narr-2.)*(np.sum((xvals-np.mean(xvals))**2))))
betaunci = np.sqrt((np.sum((yvals - (alphaesti*xvals+betaesti))**2) / (narr-2.)) * ((1./narr) + (np.mean(xvals)**2)/np.sum((xvals-np.mean(xvals))**2)) )

print("analytical MLE uncertainty on alpha is %0.7f" % (alphaunci))
print("analytical MLE uncertainty on beta is %0.7f" % (betaunci))

print("fractional uncertainty on alpha is %0.7f" % (alphaunci/alphaesti))
print("fractional uncertainty on beta is %0.7f" % (betaunci/betaesti))
print "\n"




###BISECTOR FIT

alphaestb = ( alphaestf*alphaesti - 1.0 + np.sqrt((1.0 + alphaestf**2)*(1.0 + alphaesti**2)) ) / (alphaestf+alphaesti)
betaestb = np.mean(yvals) - alphaestb*np.mean(xvals)


# The MLE values of the slope and y-intercept are equivalent to the "least
# squares" fit results.
print("analytical MLE slope = %0.7f" %alphaestb)
print("analytical MLE y-intercept = %0.7f" %betaestb)

# Overplot the MLE ("best fit") solution
yfitvals=xvals*alphaestb+betaestb
plt.plot(xvals,yfitvals,'black', label = 'bisector')
plt.legend()

# Compute analytic uncertainties on slope and y-intercept 

alphauncb = np.sqrt(np.sum((yvals - (alphaestb*xvals+betaestb))**2) / ((narr-2.)*(np.sum((xvals-np.mean(xvals))**2))))
betauncb = np.sqrt((np.sum((yvals - (alphaestb*xvals+betaestb))**2) / (narr-2.)) * ((1./narr) + (np.mean(xvals)**2)/np.sum((xvals-np.mean(xvals))**2)) )

print("analytical MLE uncertainty on alpha is %0.7f" % (alphauncb))
print("analytical MLE uncertainty on beta is %0.7f" % (betauncb))

print("fractional uncertainty on alpha is %0.7f" % (alphauncb/alphaestb))
print("fractional uncertainty on beta is %0.7f" % (betauncb/betaestb))
print "\n"

bmv = biweight_midvariance((yvals-ytrue))
rms = np.sqrt(mean_squared_error(ytrue, yvals))

print "The biweight scatter:", bmv
print "The rms scatter:", rms
print "\n"



###HERE BEGINS HAVING ERROR IN X AND Y
###When you have error in x and y, the best fit will be centered about the variable with the dominant scatter.
###For instance, with sigma = 1 for y and and sigma = 3 for x, the error is much more dominant in x.Thus an 
###inverse fit is the closest fit. With a more even error distribution, bisector fit is closer. 
###Selection bias will effect the fits. For a selection in x, the forward line won't change much. For a selection
###in y, the inverse line will not be altered.


xvals = xvals + npr.normal(0,2,100)


#add in selection bias for X > 3
yvals = yvals[np.where( xvals >3)]
xvals = xvals[np.where( xvals >3)]



plt.figure(2)
plt.clf()
plt.plot(xtrue,ytrue, linestyle="--", color='orange', label='true')
plt.plot(xvals,yvals, '.', color = 'green')
plt.xlabel("x-values")
plt.ylabel("y-values")
plt.title("Linear Fit Methods with Error in X & Y")





###FORWARD FIT - based on y as dependent

alphaestf=(np.mean(xvals)*np.mean(yvals)-np.mean(xvals*yvals)) / \
         (np.mean(xvals)**2 -np.mean(xvals**2)) #  from derivation
betaestf= np.mean(yvals) - alphaestf*np.mean(xvals)

# The MLE values of the slope and y-intercept are equivalent to the "least
# squares" fit results.
print("analytical MLE slope = %0.7f" %alphaestf)
print("analytical MLE y-intercept = %0.7f" %betaestf)

# Overplot the MLE ("best fit") solution
yfitvals=xvals*alphaestf+betaestf
plt.plot(xvals,yfitvals,'r', label = 'forward')

# Compute analytic uncertainties on slope and y-intercept 

alphauncf = np.sqrt(np.sum((yvals - (alphaestf*xvals+betaestf))**2) / ((narr-2.)*(np.sum((xvals-np.mean(xvals))**2))))
betauncf = np.sqrt((np.sum((yvals - (alphaestf*xvals+betaestf))**2) / (narr-2.)) * ((1./narr) + (np.mean(xvals)**2)/np.sum((xvals-np.mean(xvals))**2)) )

print("analytical MLE uncertainty on alpha is %0.7f" % (alphauncf))
print("analytical MLE uncertainty on beta is %0.7f" % (betauncf))

print("fractional uncertainty on alpha is %0.7f" % (alphauncf/alphaestf))
print("fractional uncertainty on beta is %0.7f" % (betauncf/betaestf))
print"\n"

###INVERSE FIT - based on x as dependent  (inverse of the forward fit and switch x and y)

alphaesti = (np.mean(yvals)**2 - np.mean(yvals*yvals)) / \
            (np.mean(xvals)*np.mean(yvals) - np.mean(yvals*xvals))
betaesti = np.mean(yvals) - alphaesti*np.mean(xvals)

# The MLE values of the slope and y-intercept are equivalent to the "least
# squares" fit results.
print("analytical MLE slope = %0.7f" %alphaesti)
print("analytical MLE y-intercept = %0.7f" %betaesti)

# Overplot the MLE ("best fit") solution
yfitvals=xvals*alphaesti+betaesti
plt.plot(xvals,yfitvals,'b', label="inverse --- best(for sigma=3)")

# Compute analytic uncertainties on slope and y-intercept 

alphaunci = np.sqrt(np.sum((yvals - (alphaesti*xvals+betaesti))**2) / ((narr-2.)*(np.sum((xvals-np.mean(xvals))**2))))
betaunci = np.sqrt((np.sum((yvals - (alphaesti*xvals+betaesti))**2) / (narr-2.)) * ((1./narr) + (np.mean(xvals)**2)/np.sum((xvals-np.mean(xvals))**2)) )

print("analytical MLE uncertainty on alpha is %0.7f" % (alphaunci))
print("analytical MLE uncertainty on beta is %0.7f" % (betaunci))

print("fractional uncertainty on alpha is %0.7f" % (alphaunci/alphaesti))
print("fractional uncertainty on beta is %0.7f" % (betaunci/betaesti))
print "\n"




###BISECTOR FIT

alphaestb = ( alphaestf*alphaesti - 1.0 + np.sqrt((1.0 + alphaestf**2)*(1.0 + alphaesti**2)) ) / (alphaestf+alphaesti)
betaestb = np.mean(yvals) - alphaestb*np.mean(xvals)


# The MLE values of the slope and y-intercept are equivalent to the "least
# squares" fit results.
print("analytical MLE slope = %0.7f" %alphaestb)
print("analytical MLE y-intercept = %0.7f" %betaestb)

# Overplot the MLE ("best fit") solution
yfitvals=xvals*alphaestb+betaestb
plt.plot(xvals,yfitvals,'black', label = 'bisector --- "best"?')
plt.legend()

# Compute analytic uncertainties on slope and y-intercept 

alphauncb = np.sqrt(np.sum((yvals - (alphaestb*xvals+betaestb))**2) / ((narr-2.)*(np.sum((xvals-np.mean(xvals))**2))))
betauncb = np.sqrt((np.sum((yvals - (alphaestb*xvals+betaestb))**2) / (narr-2.)) * ((1./narr) + (np.mean(xvals)**2)/np.sum((xvals-np.mean(xvals))**2)) )

print("analytical MLE uncertainty on alpha is %0.7f" % (alphauncb))
print("analytical MLE uncertainty on beta is %0.7f" % (betauncb))

print("fractional uncertainty on alpha is %0.7f" % (alphauncb/alphaestb))
print("fractional uncertainty on beta is %0.7f" % (betauncb/betaestb))
print "\n"





#