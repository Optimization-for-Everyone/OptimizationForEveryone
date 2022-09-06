from Run_Optimization import Single, Double, Triple 
from write_operations import WriteOperations
from enumFunctions import Functions
from enumOptimizations import Optimizations
from multipleRun import MultipleRun


class Test:
    def __init__(self, opt = Optimizations.HHO):
        self.opt = opt
        self.functionIndex = Functions.ackley
        self._lb = -32768
        self._ub = 32768
        self.dim = 30
        self.problem_size = 30
        self.searchAgents_no = 100
        self.maxiter = 10
        self.verbose = True
        self.params = self.functionIndex, self.maxiter, self.dim, self.searchAgents_no, self._lb, self._ub
        self.sma = self.functionIndex, self.dim, self.verbose, self.maxiter, self.searchAgents_no, self._lb, self._ub 

    def Run(self, opt = Optimizations.FFA):
        sol = Single(opt, self.params, self.sma)
        WriteOperations(opt.name,self.functionIndex.name,sol).write()
        return sol
    
    def MultipleRun(self):
        MultipleRun(self.opt, self.params, self.sma, number = 5)

def main():
    test = Test()
    sol = test.Run()

    


if __name__ == "__main__":
    main()