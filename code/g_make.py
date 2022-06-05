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

gmin = 0
gmax = 6
constants = np.array([r, L, size, rho, gamma, dmin, dmax, gmin, gmax])

g_values = np.linspace(gmin, gmax, size)
tau0_array = np.empty(size)

regimes_array = np.empty(shape = (size, size), dtype = float)

for i in range(0, size):
	# print("next tau0 is for gamma = %.3f"%(g_values[i]))
	tau0,_,_ = return_time(a = 0, r = r, L = L, rho = rho, gamma = g_values[i])
	tau0_array[i] = tau0
	for j in range(0, size):
		# print("next is gamma = %.3f, d = %.5f"%(g_values[i], dis_values[j]))
		regimes_array[i, j] = regimes(tau0, a = dis_values[j], r = r, L = L, rho = rho, gamma = g_values[i])

with open("g_values.npy", "wb") as f:
	np.save(f, constants)
	np.save(f, tau0_array)
	np.save(f, regimes_array)