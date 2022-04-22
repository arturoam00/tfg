import sys, time
import numpy as np
import pylab as pl

def solver_FE_simple(I, a, L, Nx, F, T, r, K):
    
    import time
    t0 = time.clock()

    x = np.linspace(0, L, Nx+1)   # mesh points in space
    dx = x[1] - x[0]

    dt = F*dx**2/a
    Nt = int(round(T/float(dt)))
    t = np.linspace(0, T, Nt+1)   # mesh points in time

    u   = np.zeros(Nx+1)  
    u_1 = np.zeros(Nx+1)

    # Set initial condition u(x,0) = I(x)
    for i in range(0, Nx+1):
        u_1[i] = I(x[i]) 
        u[i] = u_1[i]

    for n in range(0, Nt):
        # Compute u at inner mesh points
        for i in range(1, Nx):
            u[i] = u_1[i] + dt * r * u_1[i] * (1 - u_1[i] / K) + F*(u_1[i-1] - 2*u_1[i] + u_1[i+1])

        # Insert boundary conditions
        # u[0] = 1;  u[Nx] = 1

        # Switch variables before next step
        u_1, u = u, u_1

    t1 = time.clock()
    return u, x, t, t1-t0

def I(x):
    if x < .25 * L or x > .75 * L:
        return 1
    else:
        return .2

r = .1
K = 1
a = 8
L = 80
u, x, t, time = solver_FE_simple(I, 1, L, 500, .2, 12, r, K)

pl.plot(x, u)
pl.ylim(0, 1.2)
pl.xlim(0, x.max())
pl.show()




