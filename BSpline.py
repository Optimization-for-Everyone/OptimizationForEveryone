import numpy as np
from numpy import sin, cos, tan ,cosh, tanh, sinh, abs, exp, mean, pi, prod, sqrt, sum, floor

x =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#x =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#x = [1]*(15)
#x = np.random.uniform(0,1,(27,))


N=(int)(len(x)/3)
dt=1

f=0.36
h=0
m=0.02
    # I=[0] * (N*3)
    # Y=[0] * (N*3)
    # V=[0] * (N*3)

D=[0] * (N*3)

I0=0.4
Y0=0
V0=0.1

a0=(1/2+f*(dt/4)-(dt/4)*V0)*I0
b0=(1/2-(dt/4))*Y0+(dt/4)*I0*V0
c0=(1/2-m*(dt/4)*I0-h*(dt/4))*V0+(dt/4)*Y0

    # print("a0:", a0)
    # print("b0:", b0)
    # print("c0:", c0)

aM1=I0-a0
bM1=Y0-b0
cM1=V0-c0

xe=[0] * (len(x)+6)
xe[0]=aM1
xe[1]=bM1
xe[2]=cM1

xe[3]=a0
xe[4]=b0
xe[5]=c0

for i in range (len(x)):
    xe[i+6]=x[i]

print("xe:", xe)
    #fitness=0
for i in range (0,len(x),3):
    print("i: ", i)
    D[i]=(-1-f*(dt/2)+(dt/2)*(xe[i+5]+xe[i+8]))*xe[i+3]+(1-f*(dt/2)+(dt/2)*(xe[i+5]+xe[i+8]))*xe[i+6]
    print("D[",i,"]:", D[i])
    D[i+1]=(-1+(dt/2))*xe[i+4]+(1+(dt/2))*xe[i+7]-(dt/2)*(xe[i+3]+xe[i+6])*(xe[i+5]+xe[i+8])
    print("D[",i+1,"]:", D[i+1])
    D[i+2]=(-1+m*(dt/2)*(xe[i+3]+xe[i+6])+h*(dt/2))*xe[i+5]+(1+m*(dt/2)*(xe[i+3]+xe[i+6])+h*(dt/2))*xe[i+8]-(dt/2)*(xe[i+4]+xe[i+7])
    print("D[",i+2,"]:", D[i+2])
    #fitness=fitness+(1/(len(x)/3))*(D[i]**2+D[i+1]**2+D[i+2]**2)+(1/3)*((D[i]-I[0])**2+(D[i+1]-Y[0])**2+(D[i+2]-V[0])**2)


fitness=0
EI=0
EY=0
EV=0
#EC=0
#I0=xe[3]+xe[6]
#Y0=xe[4]+xe[7]
#V0=xe[5]+xe[8]
for i in range (0,len(x),3):
    EI=EI+D[i]**2
    EY=EY+D[i+1]**2
    EV=EV+D[i+2]**2

EI=(1/N)*EI
EY=(1/N)*EY
EV=(1/N)*EV
    
    #EC=(1/3)*((I0-I[0])**2+(Y0-Y[0])**2+(V0-V[0])**2)        

    # print("EI: ", EI)
    # print("EY: ", EY)
    # print("EV: ", EV)
    # print("EC: ", EC)
fitness=EI+EY+EV
    #fitness=EI+EY+EV+EC


    
    #print("D:", D)

    # fitness=0
    # for i in range(len(x)):
    #     fitness=fitness+D[i]*D[i]
    #     #fitness=fitness+abs(D[i])


plot_I=[0]*(N+1)
plot_Y=[0]*(N+1)
plot_V=[0]*(N+1)

    # plot_I[0]=I[0]
    # plot_Y[0]=Y[0]
    # plot_V[0]=V[0]

for i in range(0,N+1):
    print(xe[3*i])
    plot_I[i]=xe[3*i]+xe[3*i+3]
    plot_Y[i]=xe[3*i+1]+xe[3*i+4]
    plot_V[i]=xe[3*i+2]+xe[3*i+5]

print("plot_I:",plot_I)
print("plot_Y:",plot_Y)
print("plot_V:",plot_V)
#return fitness

print ("fitness:",fitness)