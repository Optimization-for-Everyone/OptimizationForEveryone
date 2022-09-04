import numpy as np
from Run_Optimization import Single

def MultipleRun(opt, params, sma, number):
    outputs = np.array([], dtype='float64')
    for i in range(number):
        sol = Single(opt, params, sma)
        output = sol.best
        outputs = np.append(outputs,output)
    
    bestfitnessMean = np.mean(outputs)
    bestfitnessStd = np.std(outputs)

    print("outputs:")
    print(outputs)
    print("mean:", bestfitnessMean)
    print("std:", bestfitnessStd)

    
    