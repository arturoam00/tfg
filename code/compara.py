# import time
import numpy as np
import sys
import pylab as pl
from aux import *
from scipy.spatial import distance

r = float(sys.argv[1])
a = float(sys.argv[2])

try:
	Nx = int(sys.argv[3])
except:
	Nx = 200
try:
	sigma = float(sys.argv[4])
except:
	sigma = .5
try:
	rho = float(sys.argv[5])
except:
	rho = .85

con, sin = compare(a, r, sigma = sigma, rho = rho, Nx = Nx, I = step_fun, F = .4, L = 80, K = 1, gamma = 3)
# for i in range(0, len(con)):
# 	print("%.5f, %.5f" %(con[i], sin[i]))
print(distance.euclidean(con, sin))
