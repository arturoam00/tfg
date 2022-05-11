# import time
import numpy as np
import sys
import pylab as pl
from aux import *

r = float(sys.argv[1])
a = float(sys.argv[2])
L = int(sys.argv[3])

try:
	sigma = float(sys.argv[4])
except:
	sigma = .5
try:
	rho = float(sys.argv[5])
except:
	rho = .85



tau, s = return_time(a, r, L, sigma = sigma, rho = rho, I = step_fun, F = .4, K = 1, gamma = 3, show = True, saveImage = False)
print("Return time is: %.2f for a total perturbance of: %.2f" %(tau, s))
pl.show()






