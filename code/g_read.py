import numpy as np
import sys
import pylab as pl
from aux import *

with open("g_values.npy", "rb") as f:
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
gmin = float(constants[7])
gmax = float(constants[8])

dis_values_log = np.linspace(dmin, dmax, size)  
dis_values = 10 ** dis_values_log

g_values = np.linspace(gmin, gmax, size)

fig, ax = pl.subplots(1,1)

img = ax.imshow(regimes_array, origin = "lower", extent=[dmin, dmax, gmin, gmax], \
	aspect = (dmax - dmin) / (gmax - gmin), cmap= "gnuplot", interpolation= "none")

pl.xlabel("Dispersión, " + r"$\log_{10}$" + "d")
pl.ylabel("No - linealidad, " + r"$\gamma$")

##Dibujo las curvas de frontera entre regímenes teóricas
x1 = np.log10(L ** 2 * r / (2 * .37 * tau0) ** 2)
x2 = np.log10(L ** 2 * r / 11 ** 2 * np.ones(size))

line, = ax.plot(x1, g_values, "-m", linewidth = 3)
line2, = ax.plot(x2, g_values, "-m", linewidth = 3)
pl.ylim(gmin, gmax)
pl.xlim(dmin, dmax)

# pl.savefig("../images/compara/comparaG_%i" %size, bbox_inches = "tight")

pl.show()
