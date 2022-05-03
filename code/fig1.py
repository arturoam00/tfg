import time
import numpy as np
import pylab as pl
import time

def main(I, a, T, tsteps, r, Nx = 500, F = .4, L = 80, K = 1):
    
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
    u_1, u = I(u_1, L, K), I(u, L, K)
    pl.plot(x, u, label = "t0")

    while t < T:
        u[0:Nx] = u_1[0:Nx] + dt * r * u_1[0:Nx] * (1 - u_1[0:Nx] / K) * (u_1[0:Nx] / K) ** gamma\
        + F * (np.append(u_1[Nx-1], u_1[0:Nx-1]) - 2 * u_1[0:Nx] + np.append(u_1[1:Nx], u_1[0]))

        u_1, u = u, u_1
        t+=dt

        for i in tsteps:
            if abs(t - i)<eps:
                pl.plot(x, u, label = "t%i" %tsteps.index(i))

    t1 = time.time()
    print("Time consumed: %.3f" %(t1 - t0))

    pl.xlim(0, x.max() )
    pl.ylim(0, 1.2 * K)
    pl.ylabel("Biomasa")
    pl.xlabel("x")
    pl.title("r = "+str(r)+" d = "+str(a))
    pl.legend(loc = 4)
    pl.show()



def I(u, L, K):
    l = len(u)
    sigma, rho = .4, 1
    u[0:l] = K
    u[int((.5 - sigma / 2) * l):int((.5 + sigma / 2) * l)] = (1 - rho) * K
    return u

fun = I
Nx = 200
F = .4
L = 80
K = 1

a = 1
r = 1
T = float(input("Insert time: "))
tsteps = [0, 5, 15, 25, 35, 45, T]

main(I, a, T, tsteps, r, Nx, F, L, K)


## [0, 15, 25, 28, 31, 32, T] con nx = 5000 para IR T = 35
## [0, 5, 15, 25, 35, 45, T] con nx = 200 para RR T = 55
## [0, 3, 15, 50, 400, T] con nx = 200 para MR T = 700






