import datetime
import numpy

from solution import solution
class WriteOperations():

    def __init__(self, optimizationName, fuctionName, solution):
        self.fuctionName = fuctionName
        self.optimizationName = optimizationName
        self.solution = solution
        time = str(datetime.datetime.now())
        time = time.replace(" ", "_")
        time = time.replace(":", "_")
        time = time.replace(".", "_")
        self.time = time

    def write(self):
        file = open('outputs/'+self.optimizationName + '_' + self.time + '.txt', 'w+')
        file.write("Optimizer: "+ self.optimizationName + "\n")
        file.write("ObjFucName: "+ self.fuctionName + "\n")
        file.write("StartTime: "+ str(self.solution.startTime) + "\n")
        file.write("EndTime: "+ str(self.solution.endTime) + "\n")
        file.write("ExecutionTime: "+ str(self.solution.executionTime) + "\n")
        file.write("Best: "+ str(self.solution.best) + "\n")
        file.write("BestIndividual:\n")
        file.write(str(numpy.array(self.solution.bestIndividual)))
        file.close()
        

        
        