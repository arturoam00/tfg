##############################################
#######Arturo Abril Martínez, June 2022#######
##Trabajo fin de grado Facultad C.C Físicas###
### Macro para las figuras 1 y 2 del texto ###
##############################################

import sys
import pylab as pl
from aux import *

r = float(sys.argv[1])
a = float(sys.argv[2])
L = int(sys.argv[3])
try:
	rho = float(sys.argv[4])
except:
	rho = .9
try:
	sigma = float(sys.argv[5])
except:
	sigma = .5
try:
	Nx = int(sys.argv[6])
except:
	Nx = ""

gamma = 3


tau, s, mix= return_time(a, r, L, Nx, sigma = sigma, rho = rho, K = 1, gamma = gamma, show = True, saveImage = True, compare = False)
print(mix)
print("Return time is: %.2f for a total perturbance of: %.2f" %(tau, s))
pl.show()
