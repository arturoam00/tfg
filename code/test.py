import time
import numpy as np
import pylab as pl
from aux import return_time, step_fun


fun = step_fun
Nx = 500
F = .4
L = 500
K = 1

a = 10
r = 1

size = 10

rho_values = np.linspace(0, .9, size)
sigma_values = np.linspace(0, 1, size)
tau_values = np.ones(shape = (size, size), dtype = float)

tau = 0 

for i in range(0,size):
    for j in range(0, size):
        tau_values[i, j] = return_time(fun, a, r, Nx, F, L, K, sigma_values[j], rho_values[i])
        # print("tau es %.2f para rho = %.2f y sigma = %.2f" %(tau_values[i, j],i,j))

pl.imshow(tau_values, extent = [0, 1, 0, 1], origin = "lower")
pl.colorbar()
pl.show()


