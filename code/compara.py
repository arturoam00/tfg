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

dis_values_log = np.linspace(-4, 4, size)
dis_values = 10 ** dis_values_log

############################# L ##############################################

# l_values_log = np.linspace(1, 4, size)
# l_values = 10 ** l_values_log

# regimes_array = np.empty(shape = (size, size), dtype = float)

# for i in range(0, size):
# 	for j in range(0, size):
# 		regimes_array[i, j] = regimes(dis_values[j], r, l_values[i], Nx = "", sigma = .5, rho = .9, I = step_fun, F = .4, K = 1, gamma = 3)

# fig, ax = pl.subplots(1,1)

# img = ax.imshow(regimes_array, origin = "lower", extent=[-1,1,-1,1])

# # indices_dis = find(dis_values_log, [-4, -2, 0, 2, 4])
# # indices_l = find()

# x_label_list = [round(dis_values_log[0], 1), round(dis_values_log[int(.25 * size)], 1),round(dis_values_log[int(.5 * size)], 1) ,\
#  round(dis_values_log[int(.75 * size)], 1) ,round(dis_values_log[size-1], 1)]

# y_label_list = [round(l_values_log[0], 1), round(l_values_log[int(.25 * size)], 1),round(l_values_log[int(.5 * size)], 1) ,\
#  round(l_values_log[int(.75 * size)], 1) ,round(l_values_log[size-1], 1)]

# ax.set_xticks([-1,-0.5,0,0.5,1])
# ax.set_yticks([-1,-0.5,0,0.5,1])

# ax.set_xticklabels(x_label_list)
# ax.set_yticklabels(y_label_list)

# pl.xlabel("Dispersión, " + r"$\log_{10}d$")
# pl.ylabel("Tamaño del sistema, " + r"$\log_{10} L$")

# pl.savefig("../images/compara/comparaL_%i" %size, bbox_inches = "tight")


# pl.show()

############################# GAMMA ##############################################

# g_values = np.linspace(0, 6, size)

# regimes_array = np.empty(shape = (size, size), dtype = float)

# for i in range(0, size):
# 	for j in range(0, size):
# 		regimes_array[i, j] = regimes(dis_values[j], r, L = 100, Nx = "", sigma = .5, rho = .9, I = step_fun, F = .4, K = 1, gamma = g_values[i])

# fig, ax = pl.subplots(1,1)

# img = ax.imshow(regimes_array, origin = "lower", extent=[-1,1,-1,1])

# x_label_list = [round(dis_values_log[0], 1), round(dis_values_log[int(.25 * size)], 1),round(dis_values_log[int(.5 * size)], 1) ,\
#  round(dis_values_log[int(.75 * size)], 1) ,round(dis_values_log[size-1], 1)]

# y_label_list = [round(g_values[0], 1), round(g_values[int(.25 * size)], 1),round(g_values[int(.75 * size)], 1) ,round(g_values[size-1], 1)]

# ax.set_xticks([-1,-0.5,0,0.5,1])
# ax.set_yticks([-1,-0.5,0.5,1])

# ax.set_xticklabels(x_label_list)
# ax.set_yticklabels(y_label_list)

# pl.xlabel("Dispersión, " + r"$\log_{10}d$")
# pl.ylabel("No-linealidad, " + r"$\gamma$")

# pl.savefig("../images/compara/comparaG_%i" %size, bbox_inches = "tight")


# pl.show()

############################# RHO ##############################################

rho_values = np.linspace(.01, 1, size)

regimes_array = np.empty(shape = (size, size), dtype = float)

for i in range(0, size):
	for j in range(0, size):
		regimes_array[i, j] = regimes(dis_values[j], r, L = 100, Nx = "", sigma = .5, rho = rho_values[i], I = step_fun, F = .4, K = 1, gamma = 3)
		print(dis_values[j], rho_values[i])

fig, ax = pl.subplots(1,1)

img = ax.imshow(regimes_array, origin = "lower", extent=[-1,1,-1,1])

x_label_list = [round(dis_values_log[0], 1), round(dis_values_log[int(.25 * size)], 1),round(dis_values_log[int(.5 * size)], 1) ,\
 round(dis_values_log[int(.75 * size)], 1) ,round(dis_values_log[size-1], 1)]

y_label_list = [round(rho_values[0], 1), round(rho_values[int(.25 * size)], 1),round(rho_values[int(.75 * size)], 1) ,round(rho_values[size-1], 1)]

ax.set_xticks([-1,-0.5,0,0.5,1])
ax.set_yticks([-1,-0.5,0.5,1])

ax.set_xticklabels(x_label_list)
ax.set_yticklabels(y_label_list)

pl.xlabel("Dispersión, " + r"$\log_{10}d$")
pl.ylabel("Intensidad de la perturbación, " + r"$\rho$")

# pl.savefig("../images/compara/comparaR_%i" %size, bbox_inches = "tight")


pl.show()