import time
import numpy as np
import pylab as pl
from aux import find, step_fun

def main(I, a, T, tsteps, r, Nx, F, L, K, sigma, rho):
    
    # t0 = time.time()
    p = []  ## Vector que contiene los plots para los colores
    
    gamma = 3

    ## Vector espacial
    dx = L / Nx
    x = np.linspace(0, L, Nx)

    ## Vector temporal y vector con los valores de la integral para cada t
    time_vec = np.linspace(-.05 * T , 0, 100)
    integral = np.array([np.repeat(K, 100)])

    dt = F * dx ** 2 / a
    t = 0.0
    eps = dt / 2

    u_1 = np.empty(Nx, float)
    u   = np.empty(Nx, float)  

    # Set initial condition u(x,0) = I(x)
    u_1, s = I(u_1, L, K, sigma, rho)
    u = u_1

    ## Plot para los diferentes perfiles
    plot1 = pl.figure(1)
    p.append(pl.plot(x, u, label = "t0"))

    while t < T:
        u[0:Nx] = u_1[0:Nx] + dt * r * u_1[0:Nx] * (1 - u_1[0:Nx] / K) * (u_1[0:Nx] / K) ** gamma\
        + F * (np.append(u_1[Nx-1], u_1[0:Nx-1]) - 2 * u_1[0:Nx] + np.append(u_1[1:Nx], u_1[0]))

        # Integral of u(x, t) 
        suma = np.sum(u * dx) / L
        integral = np.append(integral, suma)
        time_vec = np.append(time_vec, t)

        u_1, u = u, u_1
        t+=dt

        for i in tsteps:
            if abs(t - i)<eps:
                p.append(pl.plot(x, u, label = "t%i" %tsteps.index(i)))

    # t1 = time.time()
    # print("Time consumed: %.3f" %(t1 - t0))


    pl.xlim(0, x.max() )
    pl.ylim(0, 1.2 * K)
    pl.ylabel("Biomasa")
    pl.xlabel("x")
    pl.title("r = "+str(r)+" d = "+str(a))
    pl.legend(loc = 4)

    ## Plot para la integral de la biomasa en funcion de t
    plot2 = pl.figure(2)

    pl.plot(time_vec, integral)    
    pl.ylim(.95 - s, 1.02 * K)
    pl.xlim(time_vec.min(), time_vec.max()+.005 * T)
    pl.ylabel("Biomasa / K")
    pl.xlabel("Tiempo")

    time_vec = time_vec[99:]
    integral = integral[99:]
    markers = find(time_vec, tsteps)
    c = 0
    for i in markers:
        pl.plot(time_vec[i], integral[i], color = p[c][0].get_color(), marker = "o")    
        c+=1


    ## Plot para el parameter space de las disturbances
    plot3 = pl.figure(3)
    x_vec = np.linspace(0.01, 1, 100)
    y_vec = s / x_vec
    pl.plot(x_vec, y_vec, "k--")
    pl.plot(rho, sigma, "ro")
    pl.xlabel("Intensidad de la perturbacion, " + r"$\rho$")
    pl.ylabel("Extension de la perturbacion, "+ r"$\sigma$")
    pl.text(.6, s / .6 + .05, "s = %.2f" %s)
    pl.ylim(0, 1)

    pl.show()

    ## Save figures




fun = step_fun
Nx = 500
F = .4
L = 80
K = 1

a = 1
r = 1
T = float(input("Insert time: "))
tsteps = [0, 5, 15, 25, 35, 45, T]

sigma = .4
rho = .85

main(fun, a, T, tsteps, r, Nx, F, L, K, sigma, rho)


## [0, 15, 25, 28, 31, 32, T] con nx = 5000 para IR (r = 4, d = .01) T = 35
## [0, 5, 15, 25, 35, 45, T] con nx = 200 para RR (r = 1, d = 1) T = 55
## [0, 3, 15, 50, 400, T] con nx = 200 para MR (r = .01, d = 8) T = 700
## Siempre con gamma = 3, L = 80, K = 1






