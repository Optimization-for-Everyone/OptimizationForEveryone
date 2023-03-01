import numpy as np
from numpy import sin, cos, tan ,cosh, tanh, sinh, abs, exp, mean, pi, prod, sqrt, sum, floor

from sympy import *
import sympy as sym

t=sym.symbols('t')
#t=1

x =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
#x = np.random.uniform(0,1,(27,))
print(x)
#k=len(x)/3
I_t=0
U_t=0
V_t=0
I_t_d=0
U_t_d=0
V_t_d=0

#print('I am exactly here')

for i in range(0,int(len(x)/3),3):
    #I_t=I_t+x[i]*(1/(1+pow(math.e,-(x[i+2]*t+x[i+1]))))
    I_t=I_t+x[i]*(1/(1+exp(-(x[i+2]*t+x[i+1]))))
    #print(I_t)

for i in range(int(len(x)/3),int(2*len(x)/3),3):
    #U_t=U_t+x[i]*(1/(1+pow(math.e,-(x[i+2]*t+x[i+1]))))
    U_t=U_t+x[i]*(1/(1+exp(-(x[i+2]*t+x[i+1]))))
    #print(U_t)
    
for i in range(int(2*len(x)/3),len(x),3):
    #V_t=V_t+x[i]*(1/(1+pow(math.e,-(x[i+2]*t+x[i+1]))))
    V_t=V_t+x[i]*(1/(1+exp(-(x[i+2]*t+x[i+1]))))
    #print(V_t)
    
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
    
print("I_t: ",I_t)
print("U_t: ",U_t)
print("V_t: ",V_t)
print("Derivatives: ")
print("I_t_d: ",I_t_d)
print("U_t_d: ",U_t_d)
print("V_t_d: ",V_t_d)

# tekrar
I_t=0
U_t=0
V_t=0
I_t_d=0
U_t_d=0
V_t_d=0
t=1
for i in range(0,int(len(x)/3),3):
    #I_t=I_t+x[i]*(1/(1+pow(math.e,-(x[i+2]*t+x[i+1]))))
    I_t=I_t+x[i]*(1/(1+exp(-(x[i+2]*t+x[i+1]))))
    #print(I_t)

for i in range(int(len(x)/3),int(2*len(x)/3),3):
    #U_t=U_t+x[i]*(1/(1+pow(math.e,-(x[i+2]*t+x[i+1]))))
    U_t=U_t+x[i]*(1/(1+exp(-(x[i+2]*t+x[i+1]))))
    #print(U_t)
  
for i in range(int(2*len(x)/3),len(x),3):
    #V_t=V_t+x[i]*(1/(1+pow(math.e,-(x[i+2]*t+x[i+1]))))
    V_t=V_t+x[i]*(1/(1+exp(-(x[i+2]*t+x[i+1]))))
    #print(V_t)
    
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
    
#print("I_t: ",I_t)
#print("U_t: ",U_t)
#print("V_t: ",V_t)
#print("Derivatives: ")
#print("I_t_d: ",I_t_d)
#print("U_t_d: ",U_t_d)
#print("V_t_d: ",V_t_d)
    
# end tekrar

#general parameters
#r=2*pow(10,-2)
#delta=0.7*pow(10,-9)
#alpha=0.00842
#b=50

#f=r/delta
#h=alpha/delta
#g=1/b
# end general parameters

#problem 1
f=0
h=0.15
g=0.02
#end problem 1
N=1

sum_EI=0
for i in range(N):
    sum_EI=sum_EI+(I_t_d-f*I_t+I_t*V_t)**2
EI=sum_EI/N

sum_EU=0
for i in range(N):
    sum_EU=sum_EU+(U_t_d-I_t*V_t+U_t)**2
EU=sum_EU/N

sum_EV=0
for i in range(N):
    sum_EV=sum_EV+(V_t_d-U_t+g*I_t*V_t+h*V_t)**2
EV=sum_EV/N

I0=0.6
U0=0
V0=0.5

EC=(1/3)*((I_t-I0)**2+(U_t-U0)**2+(V_t-V0)**2)

print("EI: ", EI)
print("EU: ", EU)
print("EV: ", EV)

E=EI+EU+EV+EC

print("E: ", E)