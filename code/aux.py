##Auxiliary functions
import numpy as np

## Initial step function
def step_fun(u, L, K, sigma, rho):
    s = sigma * rho
    l = len(u)
    u[0:l] = K
    u[int((.5 - sigma / 2) * l):int((.5 + sigma / 2) * l)] = (1 - rho) * K
    return u, s

## Find nearest element index function
def find(vec, elem):  
    result = []
    vec = np.round(vec, 1)
    for i in range(0, len(vec)):
        for j in elem:
            if vec[i] == j:
                result = np.append(result, i)
                elem.remove(j)
    return result

# Returns time of recovery defined as time to get back to .99 K
def return_time(I, a, r, Nx, F, L, K, sigma, rho):
    
    gamma = 3

    ## Vector espacial
    dx = L / Nx
    x = np.linspace(0, L, Nx)

    ## Vector con valores de la integral para cada t
    integral = []
    suma = 0

    dt = F * dx ** 2 / a
    t = 0.0
    eps = dt / 2

    u_1 = np.empty(Nx, float)
    u   = np.empty(Nx, float)  

    # Set initial condition u(x,0) = I(x)
    u_1, s = I(u_1, L, K, sigma, rho)
    u = u_1


    while suma < .99 * K:

        u[0:Nx] = u_1[0:Nx] + dt * r * u_1[0:Nx] * (1 - u_1[0:Nx] / K) * (u_1[0:Nx] / K) ** gamma\
        + F * (np.append(u_1[Nx-1], u_1[0:Nx-1]) - 2 * u_1[0:Nx] + np.append(u_1[1:Nx], u_1[0]))

        # Integral of u(x, t) 
        suma = np.sum(u * dx) / L
        integral.append(suma)

        u_1, u = u, u_1
        t+=dt

    return np.round(t-dt, 4)