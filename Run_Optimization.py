from HHO import HHO
import BAT,CS,DE,FFA,GWO,JAYA,MFO,MVO,PSO,SCA,SSA,WOA
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
        sol = numpy.array(solution.convergence)
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
        sol = numpy.array(solution.convergence)
        return sol

def Run_GA_Read(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        sss = GA.GA(obj_func, -100, 100, dim, searchAgents_no, maxiter)
        solution = GA.read(obj_func, -100, 100, dim, searchAgents_no, maxiter, sss.ga)
        sol = numpy.array(solution.result)
        return sol   

def Run_BAT(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = BAT.BAT(obj_func, -100, 100, dim, searchAgents_no, maxiter)
        return solution.convergence

def Run_CS(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = CS.CS(obj_func, -100, 100, dim, searchAgents_no, maxiter)
        return solution.convergence

def Run_DE(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = DE.DE(obj_func, -100, 100, dim, searchAgents_no, maxiter)
        return solution.convergence

def Run_FFA(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = FFA.FFA(obj_func, -100, 100, dim, searchAgents_no, maxiter)
        return solution.convergence

def Run_GWO(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = GWO.GWO(obj_func, -100, 100, dim, searchAgents_no, maxiter)
        return solution.convergence

def Run_JAYA(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = JAYA.JAYA(obj_func, -100, 100, dim, searchAgents_no, maxiter)
        return solution.convergence

def Run_MFO(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = MFO.MFO(obj_func, -100, 100, dim, searchAgents_no, maxiter)
        return solution.convergence

def Run_MVO(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = MVO.MVO(obj_func, -100, 100, dim, searchAgents_no, maxiter)
        return solution.convergence

def Run_PSO(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = PSO.PSO(obj_func, -100, 100, dim, searchAgents_no, maxiter)
        return solution.convergence

def Run_SCA(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = SCA.SCA(obj_func, -100, 100, dim, searchAgents_no, maxiter)
        return solution.convergence

def Run_SSA(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = SSA.SSA(obj_func, -100, 100, dim, searchAgents_no, maxiter)
        return solution.convergence

def Run_WOA(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = WOA.WOA(obj_func, -100, 100, dim, searchAgents_no, maxiter)
        return solution.convergence