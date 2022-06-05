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

lmin = 1
lmax = 4

constants = np.array([r, L, size, rho, gamma, dmin, dmax, lmin, lmax])

l_values_log = np.linspace(lmin, lmax, size)
l_values = 10 ** l_values_log

regimes_array = np.empty(shape = (size, size), dtype = float)

tau0, _, _= return_time(0, r, L, rho = rho, gamma = gamma) #no depende de L y puede ir fuera
for i in range(0, size):
	for j in range(0, size):
		regimes_array[i, j] = regimes(tau0, dis_values[j], r, l_values[i], rho = rho, gamma = gamma)

with open("l_values.npy", "wb") as f:
	np.save(f, constants)
	np.save(f, tau0)
	np.save(f, regimes_array)

