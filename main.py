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
import PyQt5

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
def Run_HHO(functionIndex,maxiter,dim,searchAgents_no,_lb,_ub):
        #lb=TextBox_lb.text
        lb = [_lb]
        ub = [_ub]
        obj_func=selectFunction(functionIndex)  
        solution = HHO(obj_func, lb, ub, dim, searchAgents_no, maxiter)
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
    #Inputs HHO
    MaxIter=100
    dimension=30
    searchAgentsNo=1000
    lb = [-32768]
    ub = [32768]   

    def __init__(self):
        
        QMainWindow.__init__(self)

        loadUi("qt_designer.ui",self)
        

        self.setWindowTitle("Optimization Algorthms")

        self.pushButton.clicked.connect(self.Plot)
        self.inputButton.clicked.connect(self.InputButton)
        self.infoButton.clicked.connect(self.InfoButton)
        
        #Add items to functions combo Box
        self.functionComboBox.addItem('X^2')
        self.functionComboBox.addItem('Ackley Function')
        #Add items to optimization combo Box
        self.optimizationComboBox.addItem('HHO')
        self.optimizationComboBox.addItem('SMA')
        
        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))


    def InfoButton(self):
        if self.functionComboBox.currentIndex()==1 : #Open Ackley Info Window   
            self.window = PyQt5.QtWidgets.QMainWindow()
            loadUi('ackleyFunctionWindow.ui', self.window)
            self.window.show()
            self.window.okButton.clicked.connect(self.AckleyInfoOkButton)      
    def Plot(self,sol):
        if self.optimizationComboBox.currentIndex()==0 :
            sol=Run_HHO(self.functionComboBox.currentIndex(),int(self.MaxIter),int(self.dimension),int(self.searchAgentsNo),int(self.lb),int(self.ub))
        elif self.optimizationComboBox.currentIndex()==1 :
            sol=Run_SMA(self.functionComboBox.currentIndex())
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(sol[1:,1:])
        self.MplWidget.canvas.axes.legend(('Iteration', 'Best fitness'),loc='upper right')
        self.MplWidget.canvas.axes.set_title('Convergence curve')
        self.MplWidget.canvas.draw()
    def InputButton(self):
        self.window = PyQt5.QtWidgets.QMainWindow()
        loadUi('HHO_Inputs.ui', self.window)
        self.window.show()
        self.window.hhoButton.clicked.connect(self.HHOInputOkButton)
    #HHO input window    
    def HHOInputOkButton(self):
        self.MaxIter=self.window.maxIterationTextBox.toPlainText()
        self.dimension=self.window.dimensionTextBox.toPlainText()
        self.searchAgentsNo=self.window.searchAgentsTextBox.toPlainText()
        self.lb=self.window.lbTextBox.toPlainText()
        self.ub=self.window.ubTextBox.toPlainText()
        self.window.close()
    #SMA InpuWindow
    #=================
    #=================
    #=================
    #Info Ok Buttons
    def AckleyInfoOkButton(self):        
        self.window.close()   

  

app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()