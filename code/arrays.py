import time
import numpy as np
import pylab as pl
import time

def diffusionf(I, a, T, tsteps, r, Nx = 500, F = .4, L = 80, K = 1):
    
    t0 = time.time()
    
    gamma = 0

    dx = L / Nx
    x = np.linspace(0, L, Nx)

    dt = F * dx ** 2 / a
    t = 0.0
    eps = dt / 1000

    u_1 = np.empty(Nx, float)
    u   = np.empty(Nx, float)  

    # Set initial condition u(x,0) = I(x)
    u_1, u = I(u_1, L, K), I(u, L, K)
    pl.plot(x, u, label = "t = %.3f" %t)

    while t < T:
        u[0:Nx] = u_1[0:Nx] + dt * r * u_1[0:Nx] * (1 - u_1[0:Nx] / K) * (u_1[0:Nx] / K) ** gamma\
        + F * (np.append(u_1[Nx-1], u_1[0:Nx-1]) - 2 * u_1[0:Nx] + np.append(u_1[1:Nx], u_1[0]))

        u_1, u = u, u_1
        t+=dt

        for i in tsteps:
            if abs(t - i)<eps:
                pl.plot(x, u, label = "t = %.3f" %i)

    t1 = time.time()
    print("Time consumed: %.3f" %(t1 - t0))

    pl.xlim(0, x.max() )
    pl.ylim(0, 1.2 * K)
    pl.ylabel("Biomass")
    pl.title("r = "+str(r)+" d = "+str(a))
    pl.legend()
    pl.show()



def I(u, L, K):
    l = len(u)
    u[0:l] = K
    u[int(.25 * l):int(.75 * l)] = .2 * K
    return u

fun = I
Nx = 300
F = .4
L = 1
K = 1

a = 8
r = .01
T = float(input("Insert time: "))
tsteps = [.01, .02, .9, 2, T]

diffusionf(I, a, T, tsteps, r, Nx, F, L, K)








