# import time
import numpy as np
import sys
import pylab as pl
from aux import *

r = float(sys.argv[1])
a = float(sys.argv[2])

try:
	Nx = int(sys.argv[3])
except:
	Nx = 500
try:
	sigma = float(sys.argv[4])
except:
	sigma = .5
try:
	rho = float(sys.argv[5])
except:
	rho = .85

tau, s = return_time(a, r, sigma = sigma, rho = rho, Nx = Nx, I = step_fun, F = .4, L = 80, K = 1, gamma = 3, show = True)

print("Return time is: %.2f for a total perturbance of: %.2f" %(tau, s))
pl.show()




