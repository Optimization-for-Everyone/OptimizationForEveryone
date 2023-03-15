import numpy as np
from numpy import sin, cos, tan ,cosh, tanh, sinh, abs, exp, mean, pi, prod, sqrt, sum, floor

from sympy import *
import sympy as sym





function = "sum(x**2)"



def createFunction(f):
    function = f

def custom(x):
    x = np.asarray_chkfinite(x)
    return eval(function)

def selectFunction(cbIndex):
        switcher = {
        0: ackley,
        1: dixonprice,
        2: griewank,
        3: michalewicz,
        4: perm,
        5: powell,
        6: powersum,
        7: rastrigin,
        8: rosenbrock,
        9: schwefel,
        10: sphere,
        11: sum2,
        12: trid,
        13: zakharov,
        14: ellipse,
        15: nesterov,
        16: saddle,
        17: nonlinear,
        18: cvrt,
        19: BSpline,
        20: custom
    }
        return switcher.get(cbIndex, "nothing")

def ackley( x, a=20, b=0.2, c=2*pi ):
    x = np.asarray_chkfinite(x)  # ValueError if any NaN or Inf
    n = len(x)
    s1 = sum( x**2 )
    s2 = sum( cos( c * x ))
    return -a*exp( -b*sqrt( s1 / n )) - exp( s2 / n ) + a + exp(1)

#...............................................................................
def dixonprice( x ):  # dp.m
    x = np.asarray_chkfinite(x)
    n = len(x)
    j = np.arange( 2, n+1 )
    x2 = 2 * x**2
    return sum( j * (x2[1:] - x[:-1]) **2 ) + (x[0] - 1) **2

#...............................................................................
def griewank( x, fr=4000 ):
    x = np.asarray_chkfinite(x)
    n = len(x)
    j = np.arange( 1., n+1 )
    s = sum( x**2 )
    p = prod( cos( x / sqrt(j) ))
    return s/fr - p + 1

#...............................................................................
def levy( x ):
    x = np.asarray_chkfinite(x)
    n = len(x)
    z = 1 + (x - 1) / 4
    return (sin( pi * z[0] )**2
        + sum( (z[:-1] - 1)**2 * (1 + 10 * sin( pi * z[:-1] + 1 )**2 ))
        +       (z[-1] - 1)**2 * (1 + sin( 2 * pi * z[-1] )**2 ))

#...............................................................................
michalewicz_m = .5  # orig 10: ^20 => underflow

def michalewicz( x ):  # mich.m
    x = np.asarray_chkfinite(x)
    n = len(x)
    j = np.arange( 1., n+1 )
    return - sum( sin(x) * sin( j * x**2 / pi ) ** (2 * michalewicz_m) )

#...............................................................................
def perm( x, b=.5 ):
    x = np.asarray_chkfinite(x)
    n = len(x)
    j = np.arange( 1., n+1 )
    xbyj = np.fabs(x) / j
    return mean([ mean( (j**k + b) * (xbyj ** k - 1) ) **2
            for k in j/n ])
    # original overflows at n=100 --
    # return sum([ sum( (j**k + b) * ((x / j) ** k - 1) ) **2
    #       for k in j ])

#...............................................................................
def powell( x ):
    x = np.asarray_chkfinite(x)
    n = len(x)
    n4 = ((n + 3) // 4) * 4
    if n < n4:
        x = np.append( x, np.zeros( n4 - n ))
    x = x.reshape(( 4, -1 ))  # 4 rows: x[4i-3] [4i-2] [4i-1] [4i]
    f = np.empty_like( x )
    f[0] = x[0] + 10 * x[1]
    f[1] = sqrt(5) * (x[2] - x[3])
    f[2] = (x[1] - 2 * x[2]) **2
    f[3] = sqrt(10) * (x[0] - x[3]) **2
    return sum( f**2 )

#...............................................................................
def powersum( x, b=[8,18,44,114] ):  # power.m
    x = np.asarray_chkfinite(x)
    n = len(x)
    s = 0
    for k in range( 1, n+1 ):
        bk = b[ min( k - 1, len(b) - 1 )]  # ?
        s += (sum( x**k ) - bk) **2  # dim 10 huge, 100 overflows
    return s

#...............................................................................
def rastrigin( x ):  # rast.m
    x = np.asarray_chkfinite(x)
    n = len(x)
    return 10*n + sum( x**2 - 10 * cos( 2 * pi * x ))

#...............................................................................
def rosenbrock( x ):  # rosen.m
    """ http://en.wikipedia.org/wiki/Rosenbrock_function """
        # a sum of squares, so LevMar (scipy.optimize.leastsq) is pretty good
    x = np.asarray_chkfinite(x)
    x0 = x[:-1]
    x1 = x[1:]
    return (sum( (1 - x0) **2 )
        + 100 * sum( (x1 - x0**2) **2 ))

#...............................................................................
def schwefel( x ):  # schw.m
    x = np.asarray_chkfinite(x)
    n = len(x)
    return 418.9829*n - sum( x * sin( sqrt( abs( x ))))

#...............................................................................
def sphere( x ):
    x = np.asarray_chkfinite(x)
    return sum( x**2 )

#...............................................................................
def sum2( x ):
    x = np.asarray_chkfinite(x)
    n = len(x)
    j = np.arange( 1., n+1 )
    return sum( j * x**2 )

#...............................................................................
def trid( x ):
    x = np.asarray_chkfinite(x)
    return sum( (x - 1) **2 ) - sum( x[:-1] * x[1:] )

#...............................................................................
def zakharov( x ):  # zakh.m
    x = np.asarray_chkfinite(x)
    n = len(x)
    j = np.arange( 1., n+1 )
    s2 = sum( j * x ) / 2
    return sum( x**2 ) + s2**2 + s2**4

#...............................................................................
    # not in Hedar --

def ellipse( x ):
    x = np.asarray_chkfinite(x)
    return mean( (1 - x) **2 )  + 100 * mean( np.diff(x) **2 )

#...............................................................................
def nesterov( x ):
    """ Nesterov's nonsmooth Chebyshev-Rosenbrock function, Overton 2011 variant 2 """
    x = np.asarray_chkfinite(x)
    x0 = x[:-1]
    x1 = x[1:]
    return abs( 1 - x[0] ) / 4 \
        + sum( abs( x1 - 2*abs(x0) + 1 ))

#...............................................................................
def saddle( x ):
    x = np.asarray_chkfinite(x) - 1
    return np.mean( np.diff( x **2 )) \
        + .5 * np.mean( x **4 )
        
def nonlinear( x ):
    x = np.asarray_chkfinite(x) - 1
    f = 0.36
    h = 0.15
    m = 0.02
    x_t=f*x[0]-x[0]*x[2]
    y_t=x[0]*x[2]-x[1]
    v_t=x[1]-m*x[0]*x[2]-h*x[2]    
    return x_t **2 + y_t **2 + v_t **2

def cvrt( x ):
    
    x = np.asarray_chkfinite(x) - 1
    #t=sym.symbols('t')
    #t=1
    # x=[a1,b1,w1,a2,b2,w2,...]

    #x =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
    #x = np.random.uniform(0,1,(27,))
    #print(x)

    # I_t=0
    # U_t=0
    # V_t=0
    # I_t_d=0
    # U_t_d=0
    # V_t_d=0

    # #print('I am exactly here')

    # for i in range(0,int(len(x)/3),3):
    #     #I_t=I_t+x[i]*(1/(1+pow(math.e,-(x[i+2]*t+x[i+1]))))
    #     I_t=I_t+x[i]*(1/(1+exp(-(x[i+2]*t+x[i+1]))))
    #     #print(I_t)

    # for i in range(int(len(x)/3),int(2*len(x)/3),3):
    #     #U_t=U_t+x[i]*(1/(1+pow(math.e,-(x[i+2]*t+x[i+1]))))
    #     U_t=U_t+x[i]*(1/(1+exp(-(x[i+2]*t+x[i+1]))))
    #     #print(U_t)
    
    # for i in range(int(2*len(x)/3),len(x),3):
    #     #V_t=V_t+x[i]*(1/(1+pow(math.e,-(x[i+2]*t+x[i+1]))))
    #     V_t=V_t+x[i]*(1/(1+exp(-(x[i+2]*t+x[i+1]))))
    #     #print(V_t)
    
    # for i in range(0,int(len(x)/3),3):
    #     #I_t_d=I_t_d+x[i]*x[i+2]*((pow(math.e,-(x[i+2]*t+x[i+1])))/(1+pow(math.e,-(x[i+2]*t+x[i+1])))**2)
    #     I_t_d=I_t_d+x[i]*x[i+2]*((exp(-(x[i+2]*t+x[i+1])))/(1+exp(-(x[i+2]*t+x[i+1])))**2)
    #     #print(I_t_d)
    
    # for i in range(int(len(x)/3),int(2*len(x)/3),3):
    #     #U_t_d=U_t_d+x[i]*x[i+2]*((pow(math.e,-(x[i+2]*t+x[i+1])))/(1+pow(math.e,-(x[i+2]*t+x[i+1])))**2)
    #     U_t_d=U_t_d+x[i]*x[i+2]*((exp(-(x[i+2]*t+x[i+1])))/(1+exp(-(x[i+2]*t+x[i+1])))**2)
    #     #print(U_t_d)

    # for i in range(int(2*len(x)/3),len(x),3):
    #     #V_t_d=V_t_d+x[i]*x[i+2]*((pow(math.e,-(x[i+2]*t+x[i+1])))/(1+pow(math.e,-(x[i+2]*t+x[i+1])))**2)
    #     V_t_d=V_t_d+x[i]*x[i+2]*((exp(-(x[i+2]*t+x[i+1])))/(1+exp(-(x[i+2]*t+x[i+1])))**2)
    #     #print(V_t_d)
    
    #print("I_t: ",I_t)
    #print("U_t: ",U_t)
    #print("V_t: ",V_t)
    #print("Derivatives: ")
    #print("I_t_d: ",I_t_d)
    #print("U_t_d: ",U_t_d)
    #print("V_t_d: ",V_t_d)

    # tekrar
    I_t=0
    U_t=0
    V_t=0
    I_t_d=0
    U_t_d=0
    V_t_d=0
    t=0
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
    # N=1

    # sum_EI=0
    # for i in range(N):
    #     sum_EI=sum_EI+(I_t_d-f*I_t+I_t*V_t)**2
    # EI=sum_EI/N

    # sum_EU=0
    # for i in range(N):
    #     sum_EU=sum_EU+(U_t_d-I_t*V_t+U_t)**2
    # EU=sum_EU/N

    # sum_EV=0
    # for i in range(N):
    #     sum_EV=sum_EV+(V_t_d-U_t+g*I_t*V_t+h*V_t)**2
    # EV=sum_EV/N
    
    EI=(I_t_d-f*I_t+I_t*V_t)**2
    EU=(U_t_d-I_t*V_t+U_t)**2
    EV=(V_t_d-U_t+g*I_t*V_t+h*V_t)**2

    I0=0.6
    U0=0
    V0=0.5

    EC=(1/3)*((I_t-I0)**2+(U_t-U0)**2+(V_t-V0)**2)

    # print("EI: ", EI)
    # print("EU: ", EU)
    # print("EV: ", EV)

    E=EI+EU+EV+EC

    # print("E: ", E)

    return E

def BSpline( x ):

    x = np.asarray_chkfinite(x) - 1

    #x = np.random.uniform(0,1,(27,))
    #print(x)
    #print("length: ", len(x))

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

    # for i in range (len(xe)):
    #     print("xe[",i,"]:",xe[i])

    for i in range (0,len(x),3):
        D[i]=(-1-f*(dt/2)+(dt/2)*(xe[i+5]+xe[i+8]))*xe[i+3]+(1-f*(dt/2)+(dt/2)*(xe[i+5]+xe[i+8]))*xe[i+6]
    #    print("D[",i,"]:", D[i])
        D[i+1]=(-1+(dt/2))*xe[i+4]+(1+(dt/2))*xe[i+7]-(dt/2)*(xe[i+3]+xe[i+6])*(xe[i+5]+xe[i+8])
    #    print("D[",i+1,"]:", D[i+1])
        D[i+2]=(-1+m*(dt/2)*(xe[i+3]+xe[i+6])+h*(dt/2))*xe[i+5]+(1+m*(dt/2)*(xe[i+3]+xe[i+6])+h*(dt/2))*xe[i+8]-(dt/2)*(xe[i+4]+xe[i+7])
    #    print("D[",i+2,"]:", D[i+2])

    print("D:", D)
    fitness=0
    for i in range(len(x)):
        fitness=fitness+D[i]*D[i]
    #    print("fitness: ", fitness)

    # plot_I=[0]*(N+1)
    # plot_Y=[0]*(N+1)
    # plot_V=[0]*(N+1)

    # plot_I[0]=I[0]
    # plot_Y[0]=Y[0]
    # plot_V[0]=V[0]

    # for i in range(0,N+1):
    #     plot_I[i]=xe[3*i]+xe[3*i+3]
    #     plot_Y[i]=xe[3*i+1]+xe[3*i+4]
    #     plot_V[i]=xe[3*i+2]+xe[3*i+5]

    # print("plot_I:",plot_I)
    # print("plot_Y:",plot_Y)
    # print("plot_V:",plot_V)
    return fitness