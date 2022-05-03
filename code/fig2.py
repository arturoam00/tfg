import time
import numpy as np
import pylab as pl
import time

def main(I, a, T, r, Nx = 500, F = .4, L = 80, K = 1):
    
    t0 = time.time()
    
    gamma = 3

    dx = L / Nx
    x = np.linspace(0, L, Nx)

    dt = F * dx ** 2 / a
    t = 0.0
    eps = dt / 2

    u_1 = np.empty(Nx, float)
    u   = np.empty(Nx, float)  

    # Set initial condition u(x,0) = I(x)
    u_1, s = I(u_1, L, K)
    u = u_1

    time_vec = np.linspace(-.05 * T , 0, 100)
    integral = np.array([np.repeat(K, 100)])

    while t < T:
        u[0:Nx] = u_1[0:Nx] + dt * r * u_1[0:Nx] * (1 - u_1[0:Nx] / K) * (u_1[0:Nx] / K) ** gamma\
        + F * (np.append(u_1[Nx-1], u_1[0:Nx-1]) - 2 * u_1[0:Nx] + np.append(u_1[1:Nx], u_1[0]))

        # Integral of u(x, t) 
        suma = np.sum(u * dx) / L
        integral = np.append(integral, suma)
        time_vec = np.append(time_vec, t)

        u_1, u = u, u_1
        t+=dt


    t1 = time.time()
    print("Time consumed: %.3f" %(t1 - t0))

    pl.plot(time_vec, integral)    
    pl.ylim(.95 - s, 1.02 * K)
    pl.xlim(time_vec.min(), time_vec.max())
    pl.ylabel("Biomasa / K")
    pl.xlabel("Tiempo")
    pl.show()




def I(u, L, K):
    l = len(u)
    sigma, rho = .4, 1
    s = sigma * rho
    u[0:l] = K
    u[int((.5 - sigma / 2) * l):int((.5 + sigma / 2) * l)] = (1 - rho) * K
    return u, s


fun = I
Nx = 200
F = .4
L = 80
K = 1

a = 1
r = 1
T = float(input("Insert time: "))

main(I, a, T, r, Nx, F, L, K)

## T = 55 !!
## [0, 5, 15, 25, 35, 45, T] con nx = 200 para RR T = 55







