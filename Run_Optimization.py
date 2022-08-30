import numpy
import functions
from algorithms import HHO,BAT,CS,DE,FFA,GWO,JAYA,MFO,MVO,PSO,SCA,SSA,WOA,GA
from algorithms.SMA import BaseSMA
from algorithms.HHO import HHO
from solution import solution
from enumOptimizations import Optimizations

def Single(opt, params, sma):
    switcher = {
                Optimizations.BAT: lambda: Run_BAT(params[0],params[1],params[2],params[3],params[4],params[5]),
                Optimizations.CS: lambda: Run_CS(params[0],params[1],params[2],params[3],params[4],params[5]),
                Optimizations.DE: lambda: Run_DE(params[0],params[1],params[2],params[3],params[4],params[5]),
                Optimizations.FFA: lambda: Run_FFA(params[0],params[1],params[2],params[3],params[4],params[5]),
                Optimizations.GA: lambda: Run_GA(params[0],params[1],params[2],params[3],params[4],params[5]),
                Optimizations.GWO: lambda: Run_GWO(params[0],params[1],params[2],params[3],params[4],params[5]),
                Optimizations.HHO: lambda: Run_HHO(params[0],params[1],params[2],params[3],params[4],params[5]),
                Optimizations.JAYA: lambda: Run_JAYA(params[0],params[1],params[2],params[3],params[4],params[5]),
                Optimizations.MFO: lambda: Run_MFO(params[0],params[1],params[2],params[3],params[4],params[5]),
                Optimizations.MVO: lambda: Run_MVO(params[0],params[1],params[2],params[3],params[4],params[5]),
                Optimizations.PSO: lambda: Run_PSO(params[0],params[1],params[2],params[3],params[4],params[5]),
                Optimizations.SCA: lambda: Run_SCA(params[0],params[1],params[2],params[3],params[4],params[5]),
                Optimizations.SMA: lambda: Run_SMA(sma[0], sma[1], sma[2], sma[3], sma[4], sma[5], sma[6]),
                Optimizations.SSA: lambda: Run_SSA(params[0],params[1],params[2],params[3],params[4],params[5]),
                Optimizations.WOA: lambda: Run_WOA(params[0],params[1],params[2],params[3],params[4],params[5])
        }
    func = switcher.get(opt, lambda: 'Invalid')
    sol = func()
    return sol

def Triple(opt1, opt2, opt3, param1,param2,param3, sma1,sma2,sma3):
    sol1 = Single(opt1, param1, sma1)
    sol2 = Single(opt2, param2, sma2)
    sol3 = Single(opt3, param3, sma3)
    return sol1, sol2, sol3

def Double(opt1, opt2, param1,param2, sma1, sma2):
    sol1 = Single(opt1, param1, sma1)
    sol2 = Single(opt2, param2, sma2)
    return sol1, sol2

def Run_HHO(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        #lb=TextBox_lb.text
        lb = [_lb]
        ub = [_ub]
        obj_func=functions.selectFunction(functionIndex)  
        solution = HHO(obj_func, lb, ub, dim, searchAgents_no, maxiter)
        sol = numpy.array(solution.convergence)
        return solution
def Run_SMA(functionIndex,problem_size,verbose,epoch,pop_size,_lb,_ub):
        lb = [_lb]
        ub = [_ub]    
        obj_func=functions.selectFunction(functionIndex)
        md1 = BaseSMA(obj_func, lb, ub, problem_size, verbose, epoch, pop_size)
        best_pos1, best_fit1, list_loss1, sol1, sol2 = md1.train()
        # return : the global best solution, the fitness of global best solution and the loss of training process in each epoch/iteration
        #print(md1.solution[0])
        #print(md1.solution[1])
        #print(md1.loss_train)
        return sol2
def Run_GA(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = GA.GA(obj_func, _lb, _ub, dim, searchAgents_no, maxiter)
        sol = numpy.array(solution.convergence)
        return solution

def Run_BAT(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = BAT.BAT(obj_func, _lb, _ub, dim, searchAgents_no, maxiter)
        return solution

def Run_CS(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = CS.CS(obj_func, _lb, _ub, dim, searchAgents_no, maxiter)
        return solution

def Run_DE(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = DE.DE(obj_func, _lb, _ub, dim, searchAgents_no, maxiter)
        return solution

def Run_FFA(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = FFA.FFA(obj_func, _lb, _ub, dim, searchAgents_no, maxiter)
        return solution

def Run_GWO(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = GWO.GWO(obj_func, _lb, _ub, dim, searchAgents_no, maxiter)
        return solution

def Run_JAYA(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = JAYA.JAYA(obj_func, _lb, _ub, dim, searchAgents_no, maxiter)
        return solution

def Run_MFO(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = MFO.MFO(obj_func, _lb, _ub, dim, searchAgents_no, maxiter)
        return solution

def Run_MVO(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = MVO.MVO(obj_func, _lb, _ub, dim, searchAgents_no, maxiter)
        return solution

def Run_PSO(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = PSO.PSO(obj_func, _lb, _ub, dim, searchAgents_no, maxiter)
        return solution

def Run_SCA(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = SCA.SCA(obj_func, _lb, _ub, dim, searchAgents_no, maxiter)
        return solution
def Run_SSA(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = SSA.SSA(obj_func, _lb, _ub, dim, searchAgents_no, maxiter)
        return solution

def Run_WOA(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        lb = [_lb]
        ub = [_ub]
        obj_func = functions.selectFunction(functionIndex)
        solution = WOA.WOA(obj_func, _lb, _ub, dim, searchAgents_no, maxiter)
        return solution