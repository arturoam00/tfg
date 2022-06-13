import numpy as np
import sys
from aux import *

size = int(sys.argv[1])
r = 1 
L = 100
rho = .9
gamma = 3
dmin = -5
dmax = 5

dis_values_log = np.linspace(dmin, dmax, size) 
dis_values = 10 ** dis_values_log

rmin = .2
rmax = .98
constants = np.array([r, L, size, rho, gamma, dmin, dmax, rmin, rmax])

rho_values = np.linspace(rmin, rmax, size)
tau0_array = np.ones(size)

regimes_array = np.empty(shape = (size, size), dtype = float)

for i in range(0, size):
	tau0,_,_ = return_time(a = 0, r = r, L = L, rho = rho_values[i], gamma = gamma)
	tau0_array[i] = tau0
	for j in range(0, size):
		regimes_array[i, j] = regimes(tau0, dis_values[j], r, L = L, rho = rho_values[i], gamma = gamma)

with open("rho_values.npy", "wb") as f:
	np.save(f, constants)
	np.save(f, tau0_array)
	np.save(f, regimes_array)