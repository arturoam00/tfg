import numpy as np
from aux import *
import sys
import pylab as pl

with open("./out/values_tau_d0_500.npy", "rb") as file_tau:
    a = np.load(file_tau)
    print(a)
    constants = np.load(file_tau)
    tau_values = np.load(file_tau)
    with open("./out/values_tau0_500.npy", "rb") as file_tau0:
        if all(constants == np.load(file_tau0)):
            # borrar = np.load(file_tau0)
            tau0_values = np.load(file_tau0)
        else:
            raise ValueError("Constants don't match")

r = float(constants[0])
L = int(constants[1])
print(L)
size = int(constants[2])
print(size)
rmin = float(constants[3])
rmax = float(constants[4])
smin = float(constants[5])
smax = float(constants[6])

rho_values = np.linspace(rmin, rmax, size) 
sigma_values = np.linspace(smin, smax, size) 

contours = pl.contour(sigma_values, rho_values, np.log10(tau_values), 6, colors = "black")
pl.clabel(contours, inline=True, fontsize=8)


#comment lines below if no regime boundaries needed
# #####
diff_matrix = abs(tau_values - tau0_values)
contour_boundary = pl.contour(sigma_values, rho_values, diff_matrix, [8], colors = "magenta", linewidths = 3, linestyles = "dashed")
###

pl.imshow(np.log10(tau_values), extent = [smin, smax, rmin, rmax], origin = "lower", cmap = "RdGy", alpha = .5, interpolation = "bilinear")#, vmax = np.log10(tau_values[.95*size,.95*size]))

pl.colorbar(label = "Tiempo de recuperación, " + r"$\log_{10}\tau$", drawedges = False)

pl.xlabel("Extension de la perturbación, " + r"$\sigma$")
pl.ylabel("Intensidad de la perturbación, " + r"$\rho$")
pl.title("Dispersión, d = %i" %a)
pl.xlim(.15,.95)

# pl.savefig("../images/recovery/return_%i" %a, bbox_inches = "tight")

pl.show()
