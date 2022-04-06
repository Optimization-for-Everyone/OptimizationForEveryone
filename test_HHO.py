import numpy
from HHO import HHO, Levy
from numpy import sum, pi, exp, sqrt, cos
import matplotlib.pyplot as plt
import GA 


## You can create whatever function you want here
def func_sum(solution):
    return sum(solution ** 2)


def func_ackley(solution):
    a, b, c = 20, 0.2, 2 * pi
    d = len(solution)
    sum_1 = -a * exp(-b * sqrt(sum(solution ** 2) / d))
    sum_2 = exp(sum(cos(c * solution)) / d)
    return sum_1 - sum_2 + a + exp(1)

""""
lb = [-32768]
ub = [32768]

obj_func = func_sum
dim = 30
SearchAgents_no = 1000
Max_iter = 50

solution = HHO(obj_func, lb, ub, dim, SearchAgents_no, Max_iter)
sol = numpy.array(solution.result)
"""

lb = [-100]
ub = [100]

obj_func = func_ackley
dim = 30
SearchAgents_no = 50
Max_iter = 100

solution = GA.GA(obj_func, -100, 100, dim, SearchAgents_no, Max_iter)
sol = numpy.array(solution.result)

""""
lb = [-100]
ub = [100]

obj_func = func_sum
dim = 30
SearchAgents_no = 50
Max_iter = 10

solution = HHO(obj_func, lb, ub, dim, SearchAgents_no, Max_iter)
sol = numpy.array(solution.result)
"""

plt.xlabel ('Iteration', fontsize = 12)
plt.ylabel ('Best fitness obtained so far', fontsize = 12)
plt.title ("Convergence curve", fontsize = 12)
plt.plot(sol[1:,1:]) 
plt.show()
