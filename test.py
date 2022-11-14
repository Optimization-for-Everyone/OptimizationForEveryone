from Run_Optimization import Single, Double, Triple 
from write_operations import WriteOperations
from enumFunctions import Functions
from enumOptimizations import Optimizations
from multipleRun import MultipleRun
from algorithms.BAT2 import BatAlgorithm
from algorithms.FFA2 import FireflyAlgorithm
from algorithms.SA import simulated_annealing 
from algorithms.HS import HS
import functions
from math import pow
import random
from multiprocessing import cpu_count

class Test:
    def __init__(self, opt = Optimizations.HHO):
        self.opt = opt
        self.functionIndex = Functions.ackley
        self._lb = -32768
        self._ub = 32768
        self.dim = 30
        #self.problem_size = 30
        self.searchAgents_no = 1000 # pop size
        self.maxiter = 25
        self.verbose = True
        self.params = self.functionIndex, self.maxiter, self.dim, self.searchAgents_no, self._lb, self._ub
        self.sma = self.functionIndex, self.dim, self.verbose, self.maxiter, self.searchAgents_no, self._lb, self._ub 

    def Run(self, opt = Optimizations.FFA):
        Single(opt, self.params, self.sma)
        #WriteOperations(opt.name,self.functionIndex.name,sol).write()
        #return sol
    
    def MultipleRun(self, opt = Optimizations.FFA):
        MultipleRun(self.opt, self.params, self.sma, number = 5)

    def RunBAT2(self):
        obj_func = functions.selectFunction(Functions.schwefel)

        # D = Dimension, NP = Population size, N_Gen = Number of Generation
        bat = BatAlgorithm(obj_func,Lower=-500,Upper=500,D=30,NP=1000,N_Gen = 200) 

        bat.move_bat()
    
    def RunFFA2(self):
        obj_func = functions.selectFunction(Functions.ackley)

        ffa = FireflyAlgorithm()

        ffa.run(obj_func, dim = 30, lb=-32768, ub=32768, max_evals=200)
    
    def SimulatedAnnealing(self):
        obj_func = functions.selectFunction(Functions.schwefel)
        # dim array size, -5 lb +5 lb 
        simulated_annealing( min_values = [-500,-500,-500,-500,-500,-500,-500,-500,-500], max_values = [500,500,500,500,500,500,500,500,500], mu = 0, sigma = 1, initial_temperature = 1.0, temperature_iterations = 100,
            final_temperature = 0.0001, alpha = 0.9, target_function = obj_func, verbose = True)
    
    def HarmonySearch(self):
        obj_func = functions.selectFunction(Functions.ackley)
        sol = HS(obj_func, lb = -1000, ub = 1000, dim = 2, SearchAgents_no=0, num_iterations = 5, num_processes = 2)
        # print('endTime: ',sol.endTime)
        # print('executionTime: ',sol.executionTime)
        # print('convergence: ',sol.convergence)
        # print('optimizer: ',sol.optimizer)
        # print('objfname: ',sol.objfname)
        # print('best: ',sol.best)
        # print('bestIndividual: ',sol.bestIndividual)
        return sol

def main():

    test = Test()

    #-----------MULTIRUN TESTING START-----------#

    test.MultipleRun(Optimizations.BAT)

    #-----------MULTIRUN TESTING END-------------#

    #-----------BAT 2 TESTING START-----------#

    #test.RunBAT2()

    #-----------BAT 2 TESTING END-----------#

    #-----------FFA 2 TESTING START-----------#

    #test.RunFFA2()

    #-----------FFA 2 TESTING END-------------#

    # test.SimulatedAnnealing()

    



if __name__ == "__main__":
    main()