import numpy as np
import sys
import pylab as pl
from aux import *

with open("./out/l_values.npy", "rb") as f:
    constants = np.load(f)
    tau0 = float(np.load(f))
    regimes_array = np.load(f)

r = float(constants[0])
L = int(constants[1])
size = int(constants[2])
rho = float(constants[3])
gamma = float(constants[4])
dmin = float(constants[5])
dmax = float(constants[6])
lmin = float(constants[7])
lmax = float(constants[8])

dis_values_log = np.linspace(dmin, dmax, size)  
dis_values = 10 ** dis_values_log

l_values_log = np.linspace(lmin, lmax, size)
l_values = 10 ** l_values_log

fig, ax = pl.subplots(1,1)

img = ax.imshow(regimes_array, origin = "lower", extent=[dmin, dmax, lmin, lmax], \
	aspect = (dmax - dmin) / (lmax - lmin), cmap= "gnuplot", interpolation= "none")

pl.xlabel("Dispersión, " + r"$\log_{10}$" + "d")
pl.ylabel("Tamaño del sistema, " + r"$\log_{10}$" + "L")

y1 = 2 * .37 * tau0 * np.sqrt(1 / r) * np.sqrt(dis_values)
y2 = 11 * np.sqrt(1 / r) * np.sqrt(dis_values)

line, = ax.plot(dis_values_log, np.log10(y1), "-m", linewidth = 3)
line2, = ax.plot(dis_values_log, np.log10(y2), "-m", linewidth = 3)
pl.ylim(lmin, lmax)
pl.xlim(dmin, dmax)
line3, = ax.plot(dis_values_log, np.ones(size)*2, linestyle = "dashed", color = "white")

# pl.savefig("../images/compara/comparaL_%i" %size, bbox_inches = "tight")

pl.show()
