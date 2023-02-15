import numpy as np
from numpy import sin, cos, tan ,cosh, tanh, sinh, abs, exp, mean, pi, prod, sqrt, sum, floor

from sympy import *
import sympy as sym

import math

t=sym.symbols('t')
#t=1

#x =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
x = np.random.uniform(0,1,(45,))
print(x)
k=len(x)/3
I_t=0
I_t_s=0
U_t_s=0
V_t_s=0
I_t_d=0
U_t_d=0
V_t_d=0

Q_t=1/(1+exp(-t))
print(Q_t)

#t=1
#Q_t=1/(1+pow(math.e,(-t)))
#print("******\n")
#print(Q_t)


for i in range(0,int(len(x)/3),3):
    #I_t_s=I_t_s+x[i]*(1/(1+pow(math.e,-(x[i+2]*t+x[i+1]))))
    I_t_s=I_t_s+x[i]*(1/(1+exp(-(x[i+2]*t+x[i+1]))))
    #print(I_t_s)

for i in range(int(len(x)/3),int(2*len(x)/3),3):
    #U_t_s=U_t_s+x[i]*(1/(1+pow(math.e,-(x[i+2]*t+x[i+1]))))
    U_t_s=U_t_s+x[i]*(1/(1+exp(-(x[i+2]*t+x[i+1]))))
    #print(U_t_s)
    
for i in range(int(2*len(x)/3),len(x),3):
    #V_t_s=V_t_s+x[i]*(1/(1+pow(math.e,-(x[i+2]*t+x[i+1]))))
    V_t_s=V_t_s+x[i]*(1/(1+exp(-(x[i+2]*t+x[i+1]))))
    #print(V_t_s)
    
for i in range(0,int(len(x)/3),3):
    #I_t_d=I_t_d+x[i]*x[i+2]*((pow(math.e,-(x[i+2]*t+x[i+1])))/(1+pow(math.e,-(x[i+2]*t+x[i+1])))**2)
    I_t_d=I_t_d+x[i]*x[i+2]*((exp(-(x[i+2]*t+x[i+1])))/(1+exp(-(x[i+2]*t+x[i+1])))**2)
    #print(I_t_d)
    
for i in range(int(len(x)/3),int(2*len(x)/3),3):
    #U_t_d=U_t_d+x[i]*x[i+2]*((pow(math.e,-(x[i+2]*t+x[i+1])))/(1+pow(math.e,-(x[i+2]*t+x[i+1])))**2)
    U_t_d=U_t_d+x[i]*x[i+2]*((exp(-(x[i+2]*t+x[i+1])))/(1+exp(-(x[i+2]*t+x[i+1])))**2)
    #print(U_t_d)

for i in range(int(2*len(x)/3),len(x),3):
    #V_t_d=V_t_d+x[i]*x[i+2]*((pow(math.e,-(x[i+2]*t+x[i+1])))/(1+pow(math.e,-(x[i+2]*t+x[i+1])))**2)
    V_t_d=V_t_d+x[i]*x[i+2]*((exp(-(x[i+2]*t+x[i+1])))/(1+exp(-(x[i+2]*t+x[i+1])))**2)
    #print(V_t_d)

print("I_t_s: ",I_t_s)
print("U_t_s: ",U_t_s)
print("V_t_s: ",V_t_s)
#print("Derivatives: ")
#print("I_t_d: ",I_t_d)
#print("U_t_d: ",U_t_d)
#print("V_t_d: ",V_t_d)

r=2*pow(10,-2)
delta=0.7*pow(10,-9)
alpha=0.00842
b=50

f=r/delta
h=alpha/delta
g=1/b

N=2

sum_EI=0
for i in range(N):
    sum_EI=sum_EI+(I_t_d-f*I_t_s+I_t_s*V_t_s)**2
EI=sum_EI/N

sum_EU=0
for i in range(N):
    sum_EU=sum_EU+(U_t_d-I_t_s*V_t_s+U_t_s)**2
EU=sum_EU/N

sum_EV=0
for i in range(N):
    sum_EV=sum_EV+(V_t_d-U_t_s+g*I_t_s*V_t_s+h*V_t_s)**2
EV=sum_EV/N

I0=0.6
U0=0
V0=0.5

EC=1/3*((I_t_s-I0)**2-(U_t_s-U0)**2-(V_t_s-V0)**2)

print("EI: ", EI)
print("EU: ", EU)
print("EV: ", EV)


E=EI+EU+EV+EC

print("\n*******")
print("E: ",E)


