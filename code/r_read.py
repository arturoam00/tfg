import numpy as np
import sys
import pylab as pl
from aux import *

with open("./out/rho_values.npy", "rb") as f:
    constants = np.load(f)
    tau0 = np.load(f)
    regimes_array = np.load(f)

r = float(constants[0])
L = int(constants[1])
size = int(constants[2])
rho = float(constants[3])
gamma = float(constants[4])
dmin = float(constants[5])
dmax = float(constants[6])
rmin = float(constants[7])
rmax = float(constants[8])

dis_values_log = np.linspace(dmin, dmax, size)  
dis_values = 10 ** dis_values_log

rho_values = np.linspace(rmin, rmax, size)

fig, ax = pl.subplots(1,1)

img = ax.imshow(regimes_array, origin = "lower", extent=[dmin, dmax, rmin, rmax], \
	aspect = (dmax - dmin) / (rmax - rmin), cmap= "gnuplot", interpolation= "none")

pl.xlabel("Dispersión, " + r"$\log_{10}$" + "d")
pl.ylabel("Intensidad de la perturbación, " + r"$\rho$")

x1 = np.log10(L ** 2 * r / (2 * .37 * tau0) ** 2)
x2 = np.log10(L ** 2 * r / 11 ** 2 * np.ones(size))

index = find(rho_values, [0.6226], (rmax - rmin) / size / 2)

line, = ax.plot(x1[index[0]:size], rho_values[index[0]:size], "-m", linewidth = 3)
line2, = ax.plot(x2, np.linspace(.6226, rmax, size), "-m", linewidth = 3)
pl.ylim(rmin, rmax)
pl.xlim(dmin, dmax)

# pl.savefig("../images/compara/comparaR_%i" %size, bbox_inches = "tight")

pl.show()
