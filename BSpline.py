import numpy as np
from numpy import sin, cos, tan ,cosh, tanh, sinh, abs, exp, mean, pi, prod, sqrt, sum, floor

#x =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#x =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
x = [1]*(30)
#x = np.random.uniform(0,1,(27,))
N=(int)(len(x)/3)
#print("N: ", N)
dt=1/N
#print("dt: ", dt)
    #alpha=0.00842
    #beta=(7/10) * 10**(-9)
    #delta=1/18
    #b=50

f=0
h=0.15
m=0.02

I=[0] * (N*3)
Y=[0] * (N*3)
V=[0] * (N*3)

D=[0] * (N*3)

I[0]=0.6
Y[0]=0
V[0]=0.5


a0=(1/2+f*(dt/4)-(dt/4)*V[0])*I[0]
b0=(1/2-(dt/4))*Y[0]+(dt/4)*I[0]*V[0]
c0=(1/2-m*(dt/4)*I[0]-h*(dt/4))*V[0]+(dt/4)*Y[0]

# print("a0:", a0)
# print("b0:", b0)
# print("c0:", c0)

aM1=I[0]-a0
bM1=Y[0]-b0
cM1=V[0]-c0

xe=[0] * (len(x)+6)
xe[0]=aM1
xe[1]=bM1
xe[2]=cM1

xe[3]=a0
xe[4]=b0
xe[5]=c0

for i in range (len(x)):
    xe[i+6]=x[i]

for i in range (len(xe)):
    print("xe[",i,"]:",xe[i])

for i in range (0,len(x),3):
    D[i]=(-1-f*(dt/2)+(dt/2)*(xe[i+5]+xe[i+8]))*xe[i+3]+(1-f*(dt/2)+(dt/2)*(xe[i+5]+xe[i+8]))*xe[i+6]
    print("D[",i,"]:", D[i])
    D[i+1]=(-1+(dt/2))*xe[i+4]+(1+(dt/2))*xe[i+7]-(dt/2)*(xe[i+3]+xe[i+6])*(xe[i+5]+xe[i+8])
    print("D[",i+1,"]:", D[i+1])
    D[i+2]=(-1+m*(dt/2)*(xe[i+3]+xe[i+6])+h*(dt/2))*xe[i+5]+(1+m*(dt/2)*(xe[i+3]+xe[i+6])+h*(dt/2))*xe[i+8]-(dt/2)*(xe[i+4]+xe[i+7])
    print("D[",i+2,"]:", D[i+2])

#print("D:", D)
fitness=0
for i in range(len(x)):
    fitness=fitness+D[i]*D[i]
#    print("fitness: ", fitness)

plot_I=[0]*(N+1)
plot_Y=[0]*(N+1)
plot_V=[0]*(N+1)

for i in range(0,N+1):
    plot_I[i]=xe[3*i]+xe[3*i+3]
    plot_Y[i]=xe[3*i+1]+xe[3*i+4]
    plot_V[i]=xe[3*i+2]+xe[3*i+5]

print("plot_I:",plot_I)
print("plot_Y:",plot_Y)
print("plot_V:",plot_V)

print ("fitness:",fitness)