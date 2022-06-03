import time
import numpy as np
import pylab as pl
import matplotlib.colors as colors
from aux import return_time, step_fun
import sys

r = float(sys.argv[1])
a = float(sys.argv[2])

try:
    L = int(sys.argv[3])
except:
    L = 500

try:
    size = int(sys.argv[4])
except:
    size = 20

rho_values = np.linspace(0.15, .95, size)
sigma_values = np.linspace(0.15, 1, size)

rmax = rho_values.max()
rmin = rho_values.min()
smax = sigma_values.max()
smin = sigma_values.min()

tau_values = np.empty(shape = (size, size), dtype = float)
# tau0_values = np.ones(shape = (size, size), dtype = float)

for i in range(0,size):
    for j in range(0, size):
        # print("sigma: %.3f y rho: %.3f" %(sigma_values[j], rho_values[i]))
        tau_values[i, j], _ , _= return_time(a, r, L, sigma = sigma_values[j], rho = rho_values[i])
        ###if tau0 required
        # tau0_values[i, j], _ , _= return_time(0, r, L, sigma = sigma_values[j], rho = rho_values[i])

contours = pl.contour(sigma_values, rho_values, np.log10(tau_values), 6, colors = "black")
pl.clabel(contours, inline=True, fontsize=8)


#comment lines below if no regime boundaries needed
#####
# diff_matrix = abs(tau_values - tau0_values)
# contour_boundary = pl.contour(rho_values, sigma_values, diff_matrix, [8], colors = "magenta", linewidths = 3, linestyles = "dashed")
####

pl.imshow(np.log10(tau_values), extent = [smin, smax, rmin, rmax], origin = "lower", cmap = "RdGy", alpha = .5, interpolation = "bilinear")

pl.colorbar(label = "Tiempo de recuperación, " + r"$\log_{10}\tau$", drawedges = False)

pl.xlabel("Extension de la perturbación, " + r"$\sigma$")
pl.ylabel("Intensidad de la perturbación, " + r"$\rho$")
pl.title("Dispersión, d = %i" %a)

# pl.savefig("../images/recovery/return_%i" %a, bbox_inches = "tight")

pl.show(block = True)
