# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 15:34:06 2014

@author: HP
"""

#from numpy import loadtxt, zeros, ones, array, linspace, logspace
#from pylab import scatter, show, title, xlabel, ylabel, plot, contour


import numpy as np
import pylab


data = loadtxt('trainingdata.txt', delimiter=',')

x = data[:, 0]
y = data[:, 1]

#print x
#print y

numx = np.array(x)
numy = np.array(y)

slope, intercept, r_value, p_value, slope_std_error = stats.linregress(numx, numy)

'''
val = float(raw_input("number: "))


predict_y = intercept + slope * val

print predict_y
'''
predict_y = intercept + slope * x
pred_error = y - predict_y
degrees_of_freedom = len(x) - 2
residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)

# Plotting
plot(x, y, 'o')
plot(x, predict_y, 'r')
show()
print predict_y
print slope
print intercept