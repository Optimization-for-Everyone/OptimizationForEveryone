from Run_Optimization import Single, Double, Triple 
from write_operations import WriteOperations
from enumFunctions import Functions
from enumOptimizations import Optimizations
from multipleRun import MultipleRun
from algorithms.BAT2 import BatAlgorithm
from algorithms.FFA2 import FireflyAlgorithm
import functions


class Test:
    def __init__(self, opt = Optimizations.HHO):
        self.opt = opt
        self.functionIndex = Functions.ackley
        self._lb = -32768
        self._ub = 32768
        self.dim = 30
        #self.problem_size = 30
        self.searchAgents_no = 100 # pop size
        self.maxiter = 25
        self.verbose = True
        self.params = self.functionIndex, self.maxiter, self.dim, self.searchAgents_no, self._lb, self._ub
        self.sma = self.functionIndex, self.dim, self.verbose, self.maxiter, self.searchAgents_no, self._lb, self._ub 

    def Run(self, opt = Optimizations.FFA):
        sol = Single(opt, self.params, self.sma)
        WriteOperations(opt.name,self.functionIndex.name,sol).write()
        return sol
    
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




def main():

    test = Test()

    #-----------MULTIRUN TESTING START-----------#

    #test.MultipleRun(Optimizations.FFA)

    #-----------MULTIRUN TESTING END-------------#

    #-----------BAT 2 TESTING START-----------#

    test.RunBAT2()

    #-----------BAT 2 TESTING END-----------#

    #-----------FFA 2 TESTING START-----------#

    #test.RunFFA2()

    #-----------FFA 2 TESTING END-------------#




if __name__ == "__main__":
    main()