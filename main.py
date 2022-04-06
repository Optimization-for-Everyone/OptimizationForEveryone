#------------------------------------------------------
# ---------------------- main.py -----------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
import numpy
from HHO import HHO, Levy
from SMA import BaseSMA, OriginalSMA
from numpy import sum, pi, exp, sqrt, cos
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import functions
import numpy as np
import random

#Functions
def func_sum(solution):
    return sum(solution ** 2)
def func_ackley(solution):
    a, b, c = 20, 0.2, 2 * pi
    d = len(solution)
    sum_1 = -a * exp(-b * sqrt(sum(solution ** 2) / d))
    sum_2 = exp(sum(cos(c * solution)) / d)
    return sum_1 - sum_2 + a + exp(1)
#Select wich function used;
def selectFunction(cbIndex):
        if cbIndex==0 :
            return func_sum
        elif cbIndex==1 :
            return func_ackley
#Optimization Algorthms
def Run_HHO(functionIndex,maxiter):
        #lb=TextBox_lb.text
        lb = [-32768]
        ub = [32768]
        obj_func=selectFunction(functionIndex)  
        dim = 30
        SearchAgents_no = 1000
        Max_iter = maxiter
        solution = HHO(obj_func, lb, ub, dim, SearchAgents_no, Max_iter)
        sol = np.array(solution.result)
        return sol
def Run_SMA(functionIndex):
        lb = [-100]
        ub = [100]
        problem_size = 100       
        obj_func=selectFunction(functionIndex)
        verbose = True
        epoch = 50
        pop_size = 50
        md1 = BaseSMA(obj_func, lb, ub, problem_size, verbose, epoch, pop_size)
        best_pos1, best_fit1, list_loss1, sol1 = md1.train()
        sol=numpy.array(sol1)
        # return : the global best solution, the fitness of global best solution and the loss of training process in each epoch/iteration
        print(md1.solution[0])
        print(md1.solution[1])
        print(md1.loss_train)
        return sol    

class MatplotlibWidget(QMainWindow):
    #Inputs
    MaxIter=0      
    def LoadMenu(self):
        loadUi("qt_designer.ui",self)
        

        self.setWindowTitle("Optimization Algorthms")

        self.pushButton.clicked.connect(self.Plot)
        self.inputButton.clicked.connect(self.InputButton)
        
        #Add items to functions combo Box
        self.functionComboBox.addItem('X^2')
        self.functionComboBox.addItem('Ackley Function')
        #Add items to optimization combo Box
        self.optimizationComboBox.addItem('HHO')
        self.optimizationComboBox.addItem('SMA')
        
        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))

    def __init__(self):
        
        QMainWindow.__init__(self)

        loadUi("qt_designer.ui",self)
        

        self.setWindowTitle("Optimization Algorthms")

        self.pushButton.clicked.connect(self.Plot)
        self.inputButton.clicked.connect(self.InputButton)
        
        #Add items to functions combo Box
        self.functionComboBox.addItem('X^2')
        self.functionComboBox.addItem('Ackley Function')
        #Add items to optimization combo Box
        self.optimizationComboBox.addItem('HHO')
        self.optimizationComboBox.addItem('SMA')
        
        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))

    

        #self.MplWidget.canvas.axes.clear()
        #self.MplWidget.canvas.axes.plot(t, cosinus_signal)
        #self.MplWidget.canvas.axes.plot(t, sinus_signal)
        #self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
        #self.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
        #self.MplWidget.canvas.draw()
        
         
    def Plot(self,sol):
        if self.optimizationComboBox.currentIndex()==0 :
            sol=Run_HHO(self.functionComboBox.currentIndex(),int(self.MaxIter))
        elif self.optimizationComboBox.currentIndex()==1 :
            sol=Run_SMA(self.functionComboBox.currentIndex())
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(sol[1:,1:])
        self.MplWidget.canvas.axes.legend(('Iteration', 'Best fitness'),loc='upper right')
        self.MplWidget.canvas.axes.set_title('Convergence curve')
        self.MplWidget.canvas.draw()
    def InputButton(self):
        loadUi("HHO_Inputs.ui",self)
        self.hhoButton.clicked.connect(self.HHOInputOkButton)
    #HHO input window    
    def HHOInputOkButton(self):
        self.MaxIter=self.maxIterationTextBox.toPlainText()
        self.LoadMenu()
        print(self.MaxIter)
        



app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()