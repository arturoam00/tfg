from aux import *

size = 50
rho_values = np.linspace(.2, .98, size)
rmax = rho_values.max()
rmin = rho_values.min()

index = find(rho_values, [0.6226], (rmax - rmin) / size / 2)
print(index)