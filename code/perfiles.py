#!/usr/bin/env python

# import time
import numpy as np
import sys
import pylab as pl
from aux import *
import pickle 

r = float(sys.argv[1])
a = float(sys.argv[2])
L = int(sys.argv[3])

try:
	Nx = int(sys.argv[4])
except:
	Nx = ""
try:
	sigma = float(sys.argv[5])
except:
	sigma = .5
try:
	rho = float(sys.argv[6])
except:
	rho = .85



tau, s, mix= return_time(a, r, L, Nx, sigma = sigma, rho = rho, I = step_fun, F = .4, K = 1, gamma = 3, show = True, saveImage = True, compare = False)
print("Return time is: %.2f for a total perturbance of: %.2f" %(tau, s))
pl.show()






