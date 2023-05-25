# -*- coding: utf-8 -*-
from GWO import GWO
import functions
from enumFunctions import Functions
import numpy
import matplotlib.pyplot as plt

def GreyWolf():
    _lb = 0
    _ub = 1
    dim = 450
    pop_size = 1000 # pop size
    maxiter = 250
    obj_func = functions.selectFunction(Functions.BSpline)
    sol = GWO(obj_func, _lb, _ub, dim, pop_size, maxiter)
    return sol

def main():
    result = GreyWolf()
    print("Final best fitness: ", result.best)
    print("Final best ind: ", numpy.array2string(result.bestIndividual,separator=","))
    
    myArr=result.bestIndividual
    #print(myArr)
    N=(int)(len(myArr)/3)
    #xarray=
    #print("N:", N)
    I0=0.4
    Y0=0.0
    V0=0.1

    I = [0.0] * (N+1)
    Y = [0.0] * (N+1)
    V = [0.0] * (N+1)
    
    I[0] = I0
    Y[0] = Y0
    V[0] = V0
    
    I[1:(N+1)] = myArr[:N]
    Y[1:(N+1)] = myArr[N:2*N]
    V[1:(N+1)] = myArr[2*N:]

    print("plot_I:",I)
    print("plot_Y:",Y)
    print("plot_V:",V)
        
    xpoints=[i for i in range(0, N+1)]
    plt.plot(xpoints,I, label="I")
    plt.plot(xpoints,Y, label="Y")
    plt.plot(xpoints,V, label="V")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()