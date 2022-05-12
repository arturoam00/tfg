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
# try:
# 	rho = float(sys.argv[5])
# except:
# 	rho = .85

dis_values_log = np.linspace(-4, 4, size)
dis_values = 10 ** dis_values_log
l_values_log = np.linspace(1, 4, size)
l_values = 10 ** l_values_log
regimes_array = np.empty(shape = (size, size), dtype = float)

for i in range(0, size):
	for j in range(0, size):
		regimes_array[i, j] = regimes(dis_values[j], r, l_values[i], Nx = "", sigma = .5, rho = .85, I = step_fun, F = .4, K = 1, gamma = 3)
		# print("For d = %.2f, L = %.2f, regime is %i" %(dis_values[i], l_values[j], regimes_array[i, j]))

fig, ax = pl.subplots(1,1)

img = ax.imshow(regimes_array, origin = "lower", extent=[-1,1,-1,1])

x_label_list = [round(dis_values_log[0], 1), round(dis_values_log[.25 * size], 1),round(dis_values_log[.5 * size], 1) ,\
 round(dis_values_log[.75 * size], 1) ,round(dis_values_log[size-1], 1)]

y_label_list = [round(l_values_log[0], 1), round(l_values_log[.25 * size], 1),round(l_values_log[.5 * size], 1) ,\
 round(l_values_log[.75 * size], 1) ,round(l_values_log[size-1], 1)]

ax.set_xticks([-1,-0.5,0,0.5,1])
ax.set_yticks([-1,-0.5,0,0.5,1])

ax.set_xticklabels(x_label_list)
ax.set_yticklabels(y_label_list)

pl.show()