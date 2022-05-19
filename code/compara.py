# import time
import numpy as np
import sys
import pylab as pl
from aux import *

r = 1 

try:
	size = int(sys.argv[1])
except:
	size = 20

dis_values_log = np.linspace(-2, 2, size)
dis_values = 10 ** dis_values_log

dmax = dis_values_log.max()
dmin = dis_values_log.min()

############################# L ##############################################

tau0, _, _= return_time(0, 1, 500, Nx = "", sigma = .5, rho = .9, I = step_fun, F = .4, K = 1, gamma = 3)

l_values_log = np.linspace(1, 4, size)
l_values = 10 ** l_values_log

regimes_array = np.empty(shape = (size, size), dtype = float)

for i in range(0, size):
	for j in range(0, size):
		regimes_array[i, j], _ = regimes(dis_values[j], r, l_values[i], Nx = "", sigma = .5, rho = .9, I = step_fun, F = .4, K = 1, gamma = 3)

fig, ax = pl.subplots(1,1)

lmax = l_values_log.max()
lmin = l_values_log.min()

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

pl.savefig("../images/compara/comparaL_%i" %size, bbox_inches = "tight")

pl.show(block = False)
pl.close()

############################# GAMMA ##############################################

# g_values = np.linspace(0, 6, size)
# tau0 = np.empty(size)
# L = 100

# regimes_array = np.empty(shape = (size, size), dtype = float)

# for i in range(0, size):
# 	for j in range(0, size):
# 		regimes_array[i, j], t = regimes(dis_values[j], r, L = L, Nx = "", sigma = .5, rho = .9, I = step_fun, F = .4, K = 1, \
# 			gamma = g_values[i])
# 		if t != -99:
# 			tau0[i] = t

# fig, ax = pl.subplots(1,1)

# gmax = g_values.max()
# gmin = g_values.min()

# img = ax.imshow(regimes_array, origin = "lower", extent=[dmin, dmax, gmin, gmax], \
# 	aspect = (dmax - dmin) / (gmax - gmin), cmap= "gnuplot", interpolation= "none")

# pl.xlabel("Dispersión, " + r"$\log_{10}$" + "d")
# pl.ylabel("No - linealidad, " + r"$\gamma$")

# x1 = np.log10(L ** 2 * r / (2 * .37 * tau0) ** 2)
# x2 = np.log10(L ** 2 * r / 11 ** 2 * np.ones(size))

# line, = ax.plot(x1, g_values, "-m", linewidth = 3)
# line2, = ax.plot(x2, g_values, "-m", linewidth = 3)
# pl.ylim(gmin, gmax)
# pl.xlim(dmin, dmax)

# # pl.savefig("../images/compara/comparaG_%i" %size, bbox_inches = "tight")

# pl.show()
############################# RHO ##############################################

# rho_values = np.linspace(.01, .8 , size)
# tau0 = np.ones(size)
# L = 100

# regimes_array = np.empty(shape = (size, size), dtype = float)

# for i in range(0, size):
# 	for j in range(0, size):
# 		regimes_array[i, j], t = regimes(dis_values[j], r, L = L, Nx = "", sigma = .5, rho = rho_values[i], I = step_fun, F = .4, K = 1\
# 			, gamma = 3)
# 		if t != -99 and t != 0:
# 			tau0[i] = t

# fig, ax = pl.subplots(1,1)

# rmax = rho_values.max()
# rmin = rho_values.min()

# img = ax.imshow(regimes_array, origin = "lower", extent=[dmin, dmax, rmin, rmax], \
# 	aspect = (dmax - dmin) / (rmax - rmin), cmap= "gnuplot", interpolation= "none")

# pl.xlabel("Dispersión, " + r"$\log_{10}$" + "d")
# pl.ylabel("Intensidad de la perturbacion, " + r"$\rho$")

# x1 = np.log10(L ** 2 * r / (2 * .37 * tau0) ** 2)
# x2 = np.log10(L ** 2 * r / 11 ** 2 * np.ones(size))

# line, = ax.plot(x1, rho_values, "-m", linewidth = 3)
# line2, = ax.plot(x2, rho_values, "-m", linewidth = 3)
# pl.ylim(rmin, rmax )
# pl.xlim(dmin, dmax)

# # pl.savefig("../images/compara/comparaR_%i" %size, bbox_inches = "tight")

# pl.show()