import time
import numpy as np
import pylab as pl

def diffusionf(I, a, T, r, Nx = 500, F = .4, L = 80, K = 1):
    
    import time
    t0 = time.time()

    gamma = 4

    x = np.linspace(0, L, Nx + 1)   # mesh points in space
    dx = x[1] - x[0]

    dt = F *dx ** 2 / a
    Nt = int( round(T / float(dt)) )
    t = np.linspace(0, T, Nt + 1)   # mesh points in time

    u   = np.zeros(Nx +1)  
    u_1 = np.zeros(Nx + 1)

    # Set initial condition u(x,0) = I(x)
    for i in range(0, Nx + 1):
        u_1[i] = I(x[i]) 
        u[i] = u_1[i]

    for n in range(0, Nt):
        # Compute u at inner mesh points
        for i in range(1, Nx):
            u[i] = u_1[i] + dt * r * u_1[i] * (1 - u_1[i] / K) * (u_1[i] / K) ** gamma\
             + F*(u_1[i - 1] - 2*u_1[i] + u_1[i + 1])


        # Switch variables before next step
        u_1, u = u, u_1

    # Insert boundary conditions
    # u[0] = 1;  u[Nx] = 1

    t1 = time.time()
    return u, x, t1 - t0

def I(x):
    L = 80
    if x < .25 * L or x > .75 * L:
        return 1
    else:
        return .2

def draw(t = [0, 20, 50, 52, 60], I = I):
    r = 4
    a = 0.01
    for i in t:
        u, x, time = diffusionf(I, a, i, r, Nx = 5000, F = .4, L = 80, K = 1)

        pl.plot(x, u, label = "t = %i" %i)
        pl.ylim(0, 1.2)
        pl.xlim(0, x.max())
    pl.ylabel("Biomass")
    pl.title("r = "+str(r)+" d = "+str(a))
    pl.legend()
    pl.show()

draw()








