import Run_Optimization
from write_operations import WriteOperations
from enumFunctions import Functions
from enumOptimizations import Optimizations


class Test:
    def __init__(self):
        self.functionIndex = Functions.ackley
        self._lb = -32768
        self._ub = 32768
        self.dim = 30
        self.problem_size = 30
        self.searchAgents_no = 100
        self.maxiter = 50
        self.verbose = True
        self.params = self.functionIndex, self._lb, self._ub, self.dim, self.searchAgents_no,self.maxiter
        self.sma = self.functionIndex, self.dim, self.verbose, self.maxiter, self.searchAgents_no, self._lb, self._ub 
