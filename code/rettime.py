import time
import numpy as np
import pylab as pl
import matplotlib.colors as colors
from aux import return_time, step_fun
import sys

r = float(sys.argv[1])
a = float(sys.argv[2])
L = int(sys.argv[3])

try:
    size = int(sys.argv[4])
except:
    size = 20

rho_values = np.linspace(0.15, 1, size)
sigma_values = np.linspace(0.15, .98, size)
tau_values = np.empty(shape = (size, size), dtype = float)

for i in range(0,size):
    for j in range(0, size):
        tau_values[i, j], _ = return_time(a, r, L, sigma_values[j], rho_values[i], I = step_fun, F = .4, K = 1, gamma = 3)


contours = pl.contour(rho_values, sigma_values, np.log10(tau_values), 5, colors = "black")
pl.clabel(contours, inline=True, fontsize=8)
pl.imshow(np.log10(tau_values), extent = [0.15, 1, 0.15, .95], origin = "lower", cmap = "RdGy", alpha = .5)# norm = colors.LogNorm(), )

pl.colorbar(label = "Tiempo de recuperación, " + r"$\log_{10}\tau$", drawedges = False)#, ticks = ticks)

pl.xlabel("Intensidad de la perturbación, " + r"$\rho$")
pl.ylabel("Extension de la perturbación, " + r"$\sigma$")
pl.title("Dispersión, d = %.4f" %a)

pl.savefig("../images/recovery/return_%i" %a, bbox_inches = "tight")

pl.show()


