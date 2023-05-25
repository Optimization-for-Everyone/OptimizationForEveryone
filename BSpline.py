#import numpy as np
#from numpy import sin, cos, tan ,cosh, tanh, sinh, abs, exp, mean, pi, prod, sqrt, sum, floor
import matplotlib.pyplot as plt
#x =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
x = [1]*(15)
#x = np.random.uniform(0,1,(27,))


N=(int)(len(x)/3)
dt=1.0

f=0.36
h=0.0
m=0.02
  
I0=0.4
Y0=0.0
V0=0.1

a0=(0.5+f*(dt/4)-(dt/4)*V0)*I0
b0=(0.5-(dt/4))*Y0+(dt/4)*I0*V0
c0=(0.5-m*(dt/4)*I0-h*(dt/4))*V0+(dt/4)*Y0

# a0=0.226
# b0=0.01
# c0=0.0498
# # print("dt/4:", dt/4)
# # print("f*dt/4:", f*dt/4)
# # print("(f*dt/4-(dt/4)*V0):", (f*dt/4-(dt/4)*V0))
# # print("(f*dt/4-(dt/4)*V0)*I0:", (f*dt/4-(dt/4)*V0)*0.40)
# print("test:", (0.0650*0.40))

print("a0:", a0)
print("b0:", b0)
print("c0:", c0)

aM1=I0-a0
bM1=Y0-b0
cM1=V0-c0

xe=[0.0] * (len(x)+6)
xe[0]=aM1
xe[1]=bM1
xe[2]=cM1

xe[3]=a0
xe[4]=b0
xe[5]=c0

for i in range (len(x)):
    xe[i+6]=x[i]
    
print("xe:", xe)
D=[0.0] * (len(x)+3)
    # #original below
for i in range (0,len(x)+3,3):
    D[i]=(-1.0-f*(dt/2)+(dt/2)*(xe[i+2]+xe[i+5]))*xe[i]+(1.0-f*(dt/2)+(dt/2)*(xe[i+2]+xe[i+5]))*xe[i+3]
    #D[i] = xe[i] * (-1.0 + (dt/2)*(2*xe[i+2]+2*xe[i+5]-2*f)) + xe[i+3] * (1.0 + (dt/2)*(2*xe[i+2]+2*xe[i+5]-2*f)) # simplified emrah
    print("D[",i,"]:", D[i])
    D[i+1]=(-1.0+(dt/2))*xe[i+1]+(1.0+(dt/2))*xe[i+4]-(dt/2)*(xe[i]+xe[i+3])*(xe[i+2]+xe[i+5])
    print("D[",i+1,"]:", D[i+1])
    D[i+2]=(-1.0+m*(dt/2)*(xe[i]+xe[i+3])+h*(dt/2))*xe[i+2]+(1.0+m*(dt/2)*(xe[i]+xe[i+3])+h*(dt/2))*xe[i+5]-(dt/2)*(xe[i+1]+xe[i+4])
    print("D[",i+2,"]:", D[i+2])    
    
fitness=0.0
for i in range(len(x)+3):
    #print("i:",i)
    fitness=fitness+D[i]*D[i]
    #print("fitness:", fitness)

    #fitness=fitness+abs(D[i])
    #fitness=fitness+abs(fit[i])
        
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

print ("fitness:",fitness)