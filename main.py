#------------------------------------------------------
# ---------------------- main.py -----------------------
# ------------------------------------------------------
from tabnanny import verbose
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
import PyQt5
import Run_Optimization
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import OptimizationInputs
#Optimization Algorthms


class MatplotlibWidget(QMainWindow):
    #Inputs HHO
    MaxIter=10
    dimension=30
    searchAgentsNo=1000
    lb = [-32768]
    ub = [32768]
    #Inputs SMA
    smalb = [-100]
    smaub = [100]
    problem_size = 100       
    verbose = True
    epoch = 50
    pop_size = 50

    def __init__(self):
        
        QMainWindow.__init__(self)

        loadUi("qt_designer.ui",self)
        AddItemsToComboBox(self)
        

        self.setWindowTitle("Optimization Algorthms")
        #Set button functions
        
        self.pushButton.clicked.connect(self.Plot)
        self.inputButton.clicked.connect(self.InputButton)
        self.infoButton.clicked.connect(self.InfoButton)
        self.runMultipleButton.clicked.connect(self.PlotMultiple)
        
       
        
        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))


    def InfoButton(self):
        if self.functionComboBox.currentIndex()==0 : #Open Ackley Info Window   
            self.window = PyQt5.QtWidgets.QMainWindow()
            loadUi('ackleyFunctionWindow.ui', self.window)
            self.window.show()
            self.window.okButton.clicked.connect(self.AckleyInfoOkButton)

    def Plot(self,sol):
        if self.optimizationComboBox.currentIndex()==0 :
            sol=Run_Optimization.Run_HHO(self.functionComboBox.currentIndex(),int(self.MaxIter),int(self.dimension),int(self.searchAgentsNo),int(self.lb[0]),int(self.ub[0]))
        elif self.optimizationComboBox.currentIndex()==1 :
            sol=Run_Optimization.Run_SMA(self.functionComboBox.currentIndex(),int(self.problem_size),self.verbose,int(self.epoch),int(self.pop_size),int(self.smalb[0]),int(self.smaub[0]))
        elif self.optimizationComboBox.currentIndex()==2 :
            sol=Run_Optimization.Run_GA(self.functionComboBox.currentIndex(),int(self.MaxIter),int(self.dimension),int(self.searchAgentsNo),int(self.lb[0]),int(self.ub[0]))
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(sol[1:,1:])
        self.MplWidget.canvas.axes.legend(('Iteration', 'Best fitness'),loc='upper right')
        self.MplWidget.canvas.axes.set_title('Convergence curve')
        self.MplWidget.canvas.draw()
    def PlotMultiple(self,sol):
        sol=Run_Optimization.Run_HHO(self.functionComboBox.currentIndex(),int(self.MaxIter),int(self.dimension),int(self.searchAgentsNo),int(self.lb[0]),int(self.ub[0]))
        sol2=Run_Optimization.Run_SMA(self.functionComboBox.currentIndex(),int(self.problem_size),self.verbose,int(self.epoch),int(self.pop_size),int(self.smalb[0]),int(self.smaub[0]))
        sol3=Run_Optimization.Run_GA(self.functionComboBox.currentIndex(),int(self.MaxIter),int(self.dimension),int(self.searchAgentsNo),int(self.lb[0]),int(self.ub[0]))
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(sol[1:,1:])
        self.MplWidget.canvas.axes.plot(sol2[1:,1:])
        self.MplWidget.canvas.axes.plot(sol3[1:,1:])
        self.MplWidget.canvas.axes.legend(('HHO', 'SMA','GA'),loc='upper right')
        self.MplWidget.canvas.axes.set_title('Convergence curve') 
        self.MplWidget.canvas.draw()
    def InputButton(self):
        if self.optimizationComboBox.currentIndex()==1:
            self.window = PyQt5.QtWidgets.QMainWindow()
            loadUi('SMA_Inputs.ui', self.window)
            self.window.show()
            self.window.smaButton.clicked.connect(self.SMAInputOkButton)
        else :
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
    def SMAInputOkButton(self):
        self.problem_size=self.window.problemSizeTextBox.toPlainText()
        self.verbose=self.window.verboseCheckBox.isChecked()
        self.epoch=self.window.epochTextBox.toPlainText()
        self.pop_size=self.window.popSizeTextBox.toPlainText()
        self.smalb=self.window.lbTextBox.toPlainText()
        self.smaub=self.window.ubTextBox.toPlainText()
        self.window.close()
    #SMA InpuWindow
    #=================
    #=================
    #=================
    #Info Ok Buttons
    def AckleyInfoOkButton(self):        
        self.window.close()
    
def AddItemsToComboBox(self):
         #Add items to functions combo Box
        self.functionComboBox.addItem('ackley')
        self.functionComboBox.addItem('dixonprice')
        self.functionComboBox.addItem('griewank')
        self.functionComboBox.addItem('michalewicz')
        self.functionComboBox.addItem('perm')
        self.functionComboBox.addItem('powell')
        self.functionComboBox.addItem('powersum')
        self.functionComboBox.addItem('rastrigin')
        self.functionComboBox.addItem('rosenbrock')
        self.functionComboBox.addItem('schwefel')
        self.functionComboBox.addItem('sphere')
        self.functionComboBox.addItem('sum2')
        self.functionComboBox.addItem('trid')
        self.functionComboBox.addItem('zakharov')
        self.functionComboBox.addItem('ellipse')
        self.functionComboBox.addItem('nesterov')
        self.functionComboBox.addItem('saddle')
        #Add items to optimization combo Box
        self.optimizationComboBox.addItem('HHO')
        self.optimizationComboBox.addItem('SMA')
        self.optimizationComboBox.addItem('GA')

  

app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()