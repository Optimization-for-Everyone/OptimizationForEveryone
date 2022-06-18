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
from enumOptimizations import Optimizations

class MatplotlibWidget(QMainWindow):
    #Inputs HHO
    MaxIter=50
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
        self.inputButton_2.clicked.connect(self.InputButtonSMA)
        
       
        
        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))


    def InfoButton(self):
        if self.functionComboBox.currentIndex()==0 : #Open Ackley Info Window   
            self.window = PyQt5.QtWidgets.QMainWindow()
            loadUi('ackleyFunctionWindow.ui', self.window)
            self.window.show()
            self.window.okButton.clicked.connect(self.AckleyInfoOkButton)

    def Plot(self,sol):
        opt = Optimizations(self.optimizationComboBox.currentIndex())
        opt2 = Optimizations(self.optimizationComboBox_2.currentIndex())
        opt3 = Optimizations(self.optimizationComboBox_3.currentIndex())
        params = self.functionComboBox.currentIndex(),int(self.MaxIter),int(self.dimension),int(self.searchAgentsNo),int(self.lb[0]),int(self.ub[0])
        paramsSMA = self.functionComboBox.currentIndex(), self.problem_size, self.verbose,self.epoch,self.pop_size,self.smalb,self.smaub
        if self.optimizationComboBox_2.currentIndex()==15 and self.optimizationComboBox_3.currentIndex()==15 :
            #Run single
            opt = Optimizations(self.optimizationComboBox.currentIndex())
            sol = Run_Optimization.Single(opt,params,paramsSMA)
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(sol)
            self.MplWidget.canvas.axes.legend((opt.name, 'Best fitness'),loc='upper right')
            
        elif self.optimizationComboBox_2.currentIndex()!=15 and self.optimizationComboBox_3.currentIndex()==15 :
            #Run double first and second
            sol, sol2 = Run_Optimization.Double(opt, opt2,params,paramsSMA)
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(sol)
            self.MplWidget.canvas.axes.plot(sol2)
            self.MplWidget.canvas.axes.legend((opt.name, opt2.name),loc='upper right')
        elif self.optimizationComboBox_2.currentIndex()==15 and self.optimizationComboBox_3.currentIndex()!=15 :     
            # run double first and third
            sol, sol2 = Run_Optimization.Double(opt, opt3,params,paramsSMA)
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(sol)
            self.MplWidget.canvas.axes.plot(sol2)
            self.MplWidget.canvas.axes.legend((opt.name, opt3.name),loc='upper right')
        else:
            #run all
            params = self.functionComboBox.currentIndex(),int(self.MaxIter),int(self.dimension),int(self.searchAgentsNo),int(self.lb[0]),int(self.ub[0])
            sol, sol2, sol3 = Run_Optimization.Triple(opt, opt2,opt3,params,paramsSMA)
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(sol)
            self.MplWidget.canvas.axes.plot(sol2)
            self.MplWidget.canvas.axes.plot(sol3)
            self.MplWidget.canvas.axes.legend((opt.name, opt2.name,opt3.name),loc='upper right')
        self.MplWidget.canvas.axes.set_title('Convergence curve')
        self.MplWidget.canvas.draw()

    def InputButton(self):
            self.window = PyQt5.QtWidgets.QMainWindow()
            loadUi('HHO_Inputs.ui', self.window)
            self.window.show()
            self.window.hhoButton.clicked.connect(self.HHOInputOkButton)
    def InputButtonSMA(self):       
            self.window = PyQt5.QtWidgets.QMainWindow()
            loadUi('SMA_Inputs.ui', self.window)
            self.window.show()
            self.window.smaButton.clicked.connect(self.SMAInputOkButton)
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
        for x in range(3):
            if x==0:
                AddToOptimizationCombobox(self.optimizationComboBox)
            elif x==1:
                AddToOptimizationCombobox(self.optimizationComboBox_2)
                self.optimizationComboBox_2.addItem('None')
                self.optimizationComboBox_2.setCurrentIndex(15)
            elif x==2:
                AddToOptimizationCombobox(self.optimizationComboBox_3)
                self.optimizationComboBox_3.addItem('None')
                self.optimizationComboBox_3.setCurrentIndex(15)
                
        

def AddToOptimizationCombobox(combobox):
        combobox.addItem('BAT')
        combobox.addItem('Cuckoo Search (CS)')
        combobox.addItem('Differential evolution (DE)')
        combobox.addItem('Firefly Optimization Algorithm (FFA)')
        combobox.addItem('Genetic Algorithm (GA)')
        combobox.addItem('Grey Wolf Optimizer (GWO)')
        combobox.addItem('Harris Hawks Optimization (HHO)')
        combobox.addItem('JAYA')
        combobox.addItem('Moth-Flame Optimization (MFO)')
        combobox.addItem('Multi-Verse Optimizer (MVO)')
        combobox.addItem('Particle Swarm Optimization (PSO)')
        combobox.addItem('Sine Cosine Algorithm (SCA)')
        combobox.addItem('Slime Mould Algorithm (SMA)')
        combobox.addItem('Salp Swarm Algorithm (SSA)')
        combobox.addItem('Whale Optimization Algorithm (WOA)')   

app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()