
#leave this line commented out until the end of the exercise:
from __future__ import division # make division act like python3 even if 2.7

import random
import matplotlib.pyplot as plt
import numpy as np


#create a list of random numbers from the gaussian distribution with a mean of 0 and a sigma of 1
uu=np.asarray([random.gauss(0,1) for r in xrange(10000)]) # variable named uu to avoid single-letter variable name




#3: plot histogram
# histogram plotting methods taken from http://matplotlib.org
n1, bins1, patches1 = plt.hist(uu,bins=50,normed=1,histtype='stepfilled')
plt.setp(patches1,'facecolor','g','alpha',0.75)

#overplot expected Gaussian distribution on histogram - note sigma=1
#must uncomment "import numpy as np" above to be able to use np.exp and np.sqrt
y = np.exp(-1.*(((bins1)**2) / (2.)))
norm = 1./(np.sqrt(2.* np.pi))
y = norm * y

plt.plot(bins1,y,'k--',linewidth=1.5)




#4: compute fraction in confidence interval
uarray=np.array(uu) # "np.array" turns a list into an array
limval= 1 # set to value of interest
fractinrange=np.size(np.where(abs(uarray) <= limval))/np.size(uarray)
# above line is integer division so import python3 division to get real number
print(fractinrange)
