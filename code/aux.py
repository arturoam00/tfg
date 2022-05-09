##Auxiliary functions

import numpy as np
import pylab as pl
import copy

## Initial step function
def step_fun(u, L, K, sigma, rho):
    s = sigma * rho
    l = len(u)
    u[0:l] = K
    u[int((.5 - sigma / 2) * l):int((.5 + sigma / 2) * l)] = (1 - rho) * K
    return u, s

## Find nearest element index function which is equal to a certain value in a list within some threshold
def find(vec, elem):  
    result = []
    eps = .01
    for i in range(0, len(vec)):
        for j in range(0, len(elem)):
            if abs(vec[i] - elem[j])<eps:
                result.append(i)
                elem[j] = 9999.99999
    return result

def return_time(a, r, sigma = .5, rho = .85, Nx = 200, I = step_fun, F = .4, L = 80, K = 1, gamma = 3, show = False, saveImage = False):
    
    #Añade una condición en función de l_eff para ajustar el Nx 
    
    col_list = []                                             

    ## Vector espacial
    dx = L / Nx
    x = np.linspace(0, L, Nx)

    time_vec = np.array([])   
    integral = np.array([])

    if a != 0:
        dt = F * dx ** 2 / a
    else: 
        F = 0
        dt = .01

    t = 0.0
    eps = .01
    suma = 0

    u_1 = np.empty(Nx, float)
    u   = np.empty(Nx, float)  

    # Set initial condition u(x,0) = I(x)
    u_1, s = I(u_1, L, K, sigma, rho)
    u = u_1

    values = K * (1 - np.array([1, .97, .9, .5, .2,  .025]) * s)
    values_copy = copy.copy(values)

    if show:
        plot1 = pl.figure(1)

    while suma < .99 * K:
        u[0:Nx] = u_1[0:Nx] + dt * r * u_1[0:Nx] * (1 - u_1[0:Nx] / K) * (u_1[0:Nx] / K) ** gamma\
        + F * (np.append(u_1[Nx-1], u_1[0:Nx-1]) - 2 * u_1[0:Nx] + np.append(u_1[1:Nx], u_1[0]))

        # Integral of u(x, t) 
        suma = np.sum(u * dx) / L
        integral = np.append(integral, suma)
        time_vec = np.append(time_vec, t)

        u_1, u = u, u_1
        t+=dt

        if show:
            for i in range(0, len(values)):
                if abs(suma - values[i])<eps:
                    col_list.append(pl.plot(x, u, label = "t%i" %i))
                    values[i] = 9999.9999

    if show:

        pl.xlim(0, x.max() )
        pl.ylim(0, 1.2 * K)
        pl.ylabel("Biomasa")
        pl.xlabel("x")
        pl.title("r = "+str(r)+" d = "+str(a))
        pl.legend(loc = 4)
        if saveImage:
            pl.savefig("../images/perfiles/perfiles_%i_%i" %(r, a), bbox_inches = "tight")

        ## Plot para la integral de la biomasa en funcion de t
        plot2 = pl.figure(2)

        time_vec_help = np.append(np.linspace(-.05 * time_vec.max(), 0, 100), time_vec)
        integral_help = np.append(np.repeat(K, 100), integral)

        pl.plot(time_vec_help, integral_help)    
        pl.ylim(.95 - s, 1.02 * K)
        pl.xlim(time_vec_help.min(), time_vec_help.max()+.003 * time_vec_help.max())
        pl.ylabel("Biomasa / K")
        pl.xlabel("Tiempo")

        markers = find(integral, values_copy)
        c = 0
        for i in markers:  
            pl.plot(time_vec[i], integral[i], color = col_list[c][0].get_color(), marker = "o")    
            c+=1
        if saveImage:
            pl.savefig("../images/perfiles/integral_%i_%i" %(r, a), bbox_inches = "tight")


        ## Plot para el parameter space de las disturbances
        plot3 = pl.figure(3)
        x_vec = np.linspace(0.01, 1, 100)
        y_vec = s / x_vec
        pl.plot(x_vec, y_vec, "k--")
        pl.plot(rho, sigma, "ro")
        pl.xlabel("Intensidad de la perturbacion, " + r"$\rho$")
        pl.ylabel("Extension de la perturbacion, "+ r"$\sigma$")
        pl.title(r"$s = \sigma\rho$" + " = %.2f" %s)
        pl.text(.6, s / .6 + .05, "s = %.2f" %s)
        pl.ylim(0, 1)
        pl.xlim(0, 1)

        if saveImage:
            pl.savefig("../images/perfiles/parametros_%i_%i" %(r, a), bbox_inches = "tight")


    return r * (t-dt), s


def compare(a, r, sigma = .5, rho = .85, Nx = 200, I = step_fun, F = .4, L = 80, K = 1, gamma = 3):
    
    #Añade una condición en función de l_eff para ajustar el Nx 
    
    ## Vector espacial
    dx = L / Nx
    x = np.linspace(0, L, Nx)

    time_vec = np.array([])   
    integral = np.array([])
    integral_ir = np.array([])

    dt = F * dx ** 2 / a
    t = 0.0
    eps = .01
    suma = 0
    suma_ir = 0 

    u_1 = np.empty(Nx, float)
    u   = np.empty(Nx, float)
    u_1_ir = np.empty(Nx, float)
    u_ir = np.empty(Nx, float)  

    # Set initial condition u(x,0) = I(x)
    u_1, s = I(u_1, L, K, sigma, rho)
    u = u_1

    u_1_ir, _ = I(u_1_ir, L, K, sigma, rho)
    u_ir = u_1_ir

    while suma < .99 * K:
        u[0:Nx] = u_1[0:Nx] + dt * r * u_1[0:Nx] * (1 - u_1[0:Nx] / K) * (u_1[0:Nx] / K) ** gamma\
        + F * (np.append(u_1[Nx-1], u_1[0:Nx-1]) - 2 * u_1[0:Nx] + np.append(u_1[1:Nx], u_1[0]))

        u_ir[0:Nx] = u_1_ir[0:Nx] + dt * r * u_1_ir[0:Nx] * (1 - u_1_ir[0:Nx] / K) * (u_1_ir[0:Nx] / K) ** gamma

        # Integral of u(x, t) 
        suma = np.sum(u * dx) / L
        suma_ir = np.sum(u_ir * dx) / L

        integral = np.append(integral, suma)
        integral_ir = np.append(integral_ir, suma_ir)
        time_vec = np.append(time_vec, t)

        u_1, u = u, u_1
        u_1_ir, u_ir = u_ir, u_1_ir

        t+=dt

    return integral, integral_ir

