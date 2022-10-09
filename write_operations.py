import datetime
import numpy

from solution import solution
class WriteOperations():

    def __init__(self, optimizationName, fuctionName, solution, multipleRun = 1, multiple_run_result = []):
        self.fuctionName = fuctionName
        self.optimizationName = optimizationName
        self.solution = solution
        self.multipleRun = multipleRun
        self.multiple_run_result = multiple_run_result
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

        if(self.multipleRun > 1):
            
            file.write("\n")
            file.write("\n")
            file.write("\n")

            file.write("-- Multiple Run Result ---\n")
            file.write("Outputs:\n")
            file.write(str(self.multiple_run_result[0]) + "\n")
            file.write("Mean:\n" + str(self.multiple_run_result[1]) + "\n")
            file.write("Std:\n" + str(self.multiple_run_result[2]))

        file.close()
        

        
        