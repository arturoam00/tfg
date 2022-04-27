import time
import numpy as np
import pylab as pl

def diffusionf(I, a, T, r, Nx = 500, F = .4, L = 80, K = 1):
    
    import time
    t0 = time.time()

    gamma = 0

    x = np.linspace(0, L, Nx + 1)   # mesh points in space
    dx = x[1] - x[0]

    dt = F * dx ** 2 / a
    Nt = int( round(T / float(dt)) )
    t = np.linspace(0, T, Nt + 1)   # mesh points in time

    u   = np.zeros(Nx +1)  
    u_1 = np.zeros(Nx + 1)

    # Set initial condition u(x,0) = I(x)
    for i in range(0, Nx + 1):
        u_1[i] = I(x[i], L, K) 
        u[i] = u_1[i]

    for n in range(0, Nt):
        # Compute u at inner mesh points
        for i in range(1, Nx):
            u[i] = u_1[i] + dt * r * u_1[i] * (1 - u_1[i] / K) * (u_1[i] / K) ** gamma\
             + F * (u_1[i - 1] - 2 * u_1[i] + u_1[i + 1])


        # Switch variables before next step
        u_1, u = u, u_1

    # Insert boundary conditions
    # u[0] = 1;  u[Nx] = 1

    t1 = time.time()
    return u, x, t1 - t0, K



def I(x, L, K):
    if x < .25 * L or x > .75 * L:
        return K 
    else:
        return .2 * K


def draw(a, r, t, I, Nx, F, L, K):
    for i in t:
        u, x, time, K = diffusionf(I, a, i, r, Nx, F, L, K)

        pl.plot(x, u, label = "t = %.3f" %i)
        pl.ylim(0, 1.2 * K)
        pl.xlim(0, x.max())

    pl.ylabel("Biomass")
    pl.title("r = "+str(r)+" d = "+str(a))
    pl.legend()
    pl.show()

fun = I
Nx = 20
F = .4
L = 10
K = 2

a = 8
r = .01
t = [0, .1, 3, 10]

draw(a, r, t, fun, Nx, F, L, K)









