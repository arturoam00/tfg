import time
import numpy as np
import pylab as pl
import matplotlib.colors as colors
from aux import return_time, step_fun
import sys

r = float(sys.argv[1])
a = float(sys.argv[2])
size = int(sys.argv[3])

try:
    Nx = int(sys.argv[4])
except:
    Nx = 200

rho_values = np.linspace(0.15, 1, size)
sigma_values = np.linspace(0.15, .98, size)
tau_values = np.empty(shape = (size, size), dtype = float)

for i in range(0,size):
    for j in range(0, size):
        tau_values[i, j], s = return_time(a, r, sigma_values[j], rho_values[i], Nx, I = step_fun, F = .4, L = 500, K = 1, gamma = 3)

# log_values = np.log(tau_values)
# ticks = list((np.linspace(tau_values.min(), tau_values.max(), 5)))

pl.imshow(tau_values, extent = [0.15, 1, 0.15, 1], origin = "lower", norm = colors.LogNorm())
pl.colorbar(label = "Tiempo de recuperación " + r"$\tau$")#, ticks = ticks)
pl.xlabel("Intensidad de la perturbacion, " + r"$\rho$")
pl.ylabel("Extension de la perturbacion, " + r"$\sigma$")
pl.title("Dispersion, d = %.2f" %a)

pl.savefig("../images/recovery/return_%i" %a, bbox_inches = "tight")

pl.show()


