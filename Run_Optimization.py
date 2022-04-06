from HHO import HHO, Levy
import numpy
import functions
import GA 
from SMA import BaseSMA, OriginalSMA
from solution import solution


def Run_HHO(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        #lb=TextBox_lb.text
        lb = [_lb]
        ub = [_ub]
        obj_func=functions.selectFunction(functionIndex)  
        solution = HHO(obj_func, lb, ub, dim, searchAgents_no, maxiter)
        sol = numpy.array(solution.result)
        return sol
def Run_SMA(functionIndex,problem_size,verbose,epoch,pop_size,_lb,_ub):
        lb = [_lb]
        ub = [_ub]    
        obj_func=functions.selectFunction(functionIndex)
        md1 = BaseSMA(obj_func, lb, ub, problem_size, verbose, epoch, pop_size)
        best_pos1, best_fit1, list_loss1, sol1 = md1.train()
        sol=numpy.array(sol1)
        # return : the global best solution, the fitness of global best solution and the loss of training process in each epoch/iteration
        print(md1.solution[0])
        print(md1.solution[1])
        print(md1.loss_train)
        return sol
def Run_GA(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = GA.GA(obj_func, -100, 100, dim, searchAgents_no, maxiter)
        sol = numpy.array(solution.result)
        return sol    