# import time
import numpy as np
import sys
import pylab as pl
from aux import *
from scipy.spatial import distance

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

dis_values = np.linspace(-.00001, 10000, size)
l_values = np.linspace(-.00001, 10000, size)
regimes_array = np.empty(shape = (size, size), dtype = float)

for i in range(0, size):
	for i in range(0, size):
		regimes_array[i, j] = funcion !!!!!!!
		tau, _ = return_time(a, r, L, sigma = sigma, rho = rho, I = step_fun, F = .4, K = 1, gamma = 3, show = False, saveImage = False)
		tau0, _ = return_time(0, r, L, sigma = sigma, rho = rho, I = step_fun, F = .4, K = 1, gamma = 3, show = False, saveImage = False)

print(abs(tau-tau0))