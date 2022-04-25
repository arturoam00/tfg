import time
import numpy as np
import pylab as pl
from random import seed, random

def iterator(T, d, r, L = 80, Nx = 500, Nt = 500, K = 1.0):   #(I, a, L, Nx, F, T, r, K):
    
    seed(1)
    t0 = time.time()

    gamma = 1

    x = np.linspace(0, L, Nx + 1)   # mesh points in space
    dx = x[1] - x[0]

    t = np.linspace(0, T, Nt + 1)   # mesh points in time
    dt = t[1] - t[0]

    N = np.ones(Nx + 1) * K       #Aquí puedes multiplicar por K si quieres para K distinta de 1

    # Set initial condition 
    for i in range(0, Nx + 1):
        if .25 * L < x[i] < .75 * L:
            N[i] = .2 * K         #Aquí puedes multiplicar por K si quieres

    for n in range(0, Nt):

        for i in range(0, Nx + 1):
            num = random()
            m = dt * d * N[i]  # <----------------esto lo tienes que pensar mejor

            N[i] += dt * r * N[i] * (1 - N[i] / K) * (N[i] / K) ** gamma

            if num >= .5:
                if N[(i + 1) % (Nx + 1)] < K:
                    N[i] -= m
                    N[(i + 1) % (Nx + 1)] += m  

    t1 = time.time()

    return N, x, t1-t0

r = .01
d = 1
T = float(input("insert time: "))

N, x, time = iterator(T, d, r, L = 80, Nx = 500, Nt = 500, K = 1)

print("time consumed: ", time)

pl.plot(x, N)
pl.ylim(0, 1.2)
pl.xlim(0, x.max())
pl.show()



