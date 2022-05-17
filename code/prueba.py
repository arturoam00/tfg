import numpy as np
import sys
import pylab as pl
from aux import *


size = 10
r = 1

dis_values_log = np.linspace(-4, 4, size)
dis_values = 10 ** dis_values_log


############################# L ##############################################

# tau0, _, _= return_time(0, 1, 500, Nx = "", sigma = .5, rho = .9, I = step_fun, F = .4, K = 1, gamma = 3)

g_values = np.linspace(0,6, size)

regimes_array = np.array([[1 , 1, 1, 2, 2, 3, 3, 3], [1 , 1, 1, 2, 2, 3, 3, 3],[1 , 1, 2, 2, 2, 3, 3, 3], [1 , 2, 2, 2, 3, 3, 3, 3] ])

# for i in range(0, size):
# 	for j in range(0, size):
# 		regimes_array[i, j] = regimes(dis_values[j], r, l_values[i], Nx = "", sigma = .5, rho = .9, I = step_fun, F = .4, K = 1, gamma = 3)

fig, ax = pl.subplots(1,1)
# ax.imshow(regimes_array, origin = "lower", extent = [-4, 4, 0,6], aspect = 8 / 6, zorder = 1)

x1 = - 2 * g_values
x2 =  100 ** 2 * r / 11 ** 2 * np.ones(size)

line, = ax.plot(x1, g_values, zorder = 2)
line, = ax.plot(x2, g_values, zorder = 2)

# line, = ax.plot(np.log10(dis_values), np.log10(y1))
# line2, = ax.plot(np.log10(dis_values), np.log10(y2))
# # pl.xscale("log")
# # pl.yscale("log")
# pl.ylim(1, 4)


pl.show()