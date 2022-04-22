import sys, time
import numpy as np
import pylab as pl

def solver_FE_simple(I, a, L, Nx, F, T):
    """
    Simplest expression of the computational algorithm
    using the Forward Euler method and explicit Python loops.
    For this method F <= 0.5 for stability.
    """
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
            u[i] = u_1[i] + F*(u_1[i-1] - 2*u_1[i] + u_1[i+1])

        # Insert boundary conditions
        u[0] = 1;  u[Nx] = 1

        # Switch variables before next step
        u_1, u = u, u_1

    t1 = time.clock()
    return u, x, t, t1-t0

def I(x):
	if x < .25 or x > .75:
		return 1
	else:
		return .3
    # return np.sin(np.pi * x) + .1 * np.sin(100 * np.pi * x)

u, x, t, time = solver_FE_simple(I, 1, 1, 300, .45, 0)

pl.plot(x, u)
pl.ylim(-.1, 1.2)
pl.xlim(0, x.max())
pl.show()





