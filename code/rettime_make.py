import numpy as np
from aux import *
import sys

r = float(sys.argv[1])
a = float(sys.argv[2])
L = int(sys.argv[3])
size = int(sys.argv[4])

rmin = .15 
rmax = .97 #when working with tau0 rho can't reach 1 (.95)
smin = .15
smax = .97 #when working with r / d <<< sigma = 1 means dispersal does nothing and it's very slow

constants = np.array([r, L, size, rmin, rmax, smin, smax])

rho_values = np.linspace(rmin, rmax, size) 
sigma_values = np.linspace(smin, smax, size) 

tau_values = np.empty(shape = (size, size), dtype = float)
tau0_values = np.ones(shape = (size, size), dtype = float)

for i in range(0,size):
    for j in range(0, size):
        # print("Next is rho = %.3f and sigma = %.3f" %(rho_values[i], sigma_values[j]))
        tau_values[i, j], _ , _= return_time(a, r, L, sigma = sigma_values[j], rho = rho_values[i])
        # if rho_values[i] < .96:
        #     tau0_values[i, j], _ , _= return_time(0, r, L, sigma = sigma_values[j], rho = rho_values[i])
        # else:
        #     tau0_values[i, j] = -9999.999

with open("values_tau_d%i.npy"%(a), "wb") as f:
    np.save(f, a)
    np.save(f, constants)
    np.save(f, tau_values)

# with open("values_tau0.npy", "wb") as f:
#     np.save(f, constants)
#     np.save(f, tau0_values)