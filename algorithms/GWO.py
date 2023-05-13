# -*- coding: utf-8 -*-
"""
Created on Mon May 16 00:27:50 2016

@author: Hossam Faris
"""

import random
import numpy
import math
from solution import solution
import time
import matplotlib.pyplot as plt


def GWO(objf, lb, ub, dim, SearchAgents_no, Max_iter):

    # Max_iter=1000
    # lb=-100
    # ub=100
    # dim=30
    # SearchAgents_no=5

    # initialize alpha, beta, and delta_pos
    Alpha_pos = numpy.zeros(dim)
    Alpha_score = float("inf")

    Beta_pos = numpy.zeros(dim)
    Beta_score = float("inf")

    Delta_pos = numpy.zeros(dim)
    Delta_score = float("inf")

    if not isinstance(lb, list):
        lb = [lb] * dim
    if not isinstance(ub, list):
        ub = [ub] * dim

    # Initialize the positions of search agents
    Positions = numpy.zeros((SearchAgents_no, dim))
    for i in range(dim):
        Positions[:, i] = (
            numpy.random.uniform(0, 1, SearchAgents_no) * (ub[i] - lb[i]) + lb[i]
        )

    Convergence_curve = numpy.zeros(Max_iter)
    s = solution()

    # Loop counter
    print('GWO is optimizing  "' + objf.__name__ + '"')

    timerStart = time.time()
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    # Main loop
    for l in range(0, Max_iter):
        for i in range(0, SearchAgents_no):

            # Return back the search agents that go beyond the boundaries of the search space
            for j in range(dim):
                Positions[i, j] = numpy.clip(Positions[i, j], lb[j], ub[j])

            # Calculate objective function for each search agent
            fitness = objf(Positions[i, :])

            # Update Alpha, Beta, and Delta
            if fitness < Alpha_score:
                Delta_score = Beta_score  # Update delte
                Delta_pos = Beta_pos.copy()
                Beta_score = Alpha_score  # Update beta
                Beta_pos = Alpha_pos.copy()
                Alpha_score = fitness
                # Update alpha
                Alpha_pos = Positions[i, :].copy()

            if fitness > Alpha_score and fitness < Beta_score:
                Delta_score = Beta_score  # Update delte
                Delta_pos = Beta_pos.copy()
                Beta_score = fitness  # Update beta
                Beta_pos = Positions[i, :].copy()

            if fitness > Alpha_score and fitness > Beta_score and fitness < Delta_score:
                Delta_score = fitness  # Update delta
                Delta_pos = Positions[i, :].copy()

        a = 2 - l * ((2) / Max_iter)
        # a decreases linearly fron 2 to 0

        # Update the Position of search agents including omegas
        for i in range(0, SearchAgents_no):
            for j in range(0, dim):

                r1 = random.random()  # r1 is a random number in [0,1]
                r2 = random.random()  # r2 is a random number in [0,1]

                A1 = 2 * a * r1 - a
                # Equation (3.3)
                C1 = 2 * r2
                # Equation (3.4)

                D_alpha = abs(C1 * Alpha_pos[j] - Positions[i, j])
                # Equation (3.5)-part 1
                X1 = Alpha_pos[j] - A1 * D_alpha
                # Equation (3.6)-part 1

                r1 = random.random()
                r2 = random.random()

                A2 = 2 * a * r1 - a
                # Equation (3.3)
                C2 = 2 * r2
                # Equation (3.4)

                D_beta = abs(C2 * Beta_pos[j] - Positions[i, j])
                # Equation (3.5)-part 2
                X2 = Beta_pos[j] - A2 * D_beta
                # Equation (3.6)-part 2

                r1 = random.random()
                r2 = random.random()

                A3 = 2 * a * r1 - a
                # Equation (3.3)
                C3 = 2 * r2
                # Equation (3.4)

                D_delta = abs(C3 * Delta_pos[j] - Positions[i, j])
                # Equation (3.5)-part 3
                X3 = Delta_pos[j] - A3 * D_delta
                # Equation (3.5)-part 3

                Positions[i, j] = (X1 + X2 + X3) / 3  # Equation (3.7)

        Convergence_curve[l] = Alpha_score

        if l % 1 == 0:
            print(
                ["At iteration " + str(l) + " the best fitness is " + str(Alpha_score)
                 # + " the best ind is " + str(Alpha_pos)
                 ]
            )

    timerEnd = time.time()
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime = timerEnd - timerStart
    s.convergence = Convergence_curve
    s.optimizer = "GWO"
    s.objfname = objf.__name__
    
    
    
    print("Final best fitness: ", Alpha_score)
    print("Final best ind: ", numpy.array2string(Alpha_pos,separator=","))
    #print("Deneme")
    myArr=Alpha_pos
    #print(myArr)
    N=(int)(len(myArr)/3)
    #print("N:", N)
    
    dt=2.0
    f=0.36
    h=0.0
    m=0.02

    I0=0.4
    Y0=0.0
    V0=0.1
    
    a0=(0.5+f*(dt/4)-(dt/4)*V0)*I0
    b0=(0.5-(dt/4))*Y0+(dt/4)*I0*V0
    c0=(0.5-m*(dt/4)*I0-h*(dt/4))*V0+(dt/4)*Y0
    
    aM1=I0-a0
    bM1=Y0-b0
    cM1=V0-c0

    xe=[0.0] * (len(myArr)+6)
    xe[0]=aM1
    xe[1]=bM1
    xe[2]=cM1

    xe[3]=a0
    xe[4]=b0
    xe[5]=c0

    for i in range (len(myArr)):
        xe[i+6]=myArr[i]
    
    plotI=[0.0]*(N+1)
    plotY=[0.0]*(N+1)
    plotV=[0.0]*(N+1)

    for i in range(0,N+1):
        plotI[i]=xe[3*i]+xe[3*i+3]
        plotY[i]=xe[3*i+1]+xe[3*i+4]
        plotV[i]=xe[3*i+2]+xe[3*i+5]

    print("plot_I:",plotI)
    print("plot_Y:",plotY)
    print("plot_V:",plotV)
        
    xpoints=[i for i in range(0, N+1)]
    plt.plot(xpoints,plotI, label="I")
    plt.plot(xpoints,plotY, label="Y")
    plt.plot(xpoints,plotV, label="V")
    plt.legend()
    plt.show() 
    
    return s
