#------------------------------------------------------
# ---------------------- main.py -----------------------
# ------------------------------------------------------
from tabnanny import verbose
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
import PyQt5
from matplotlib.pyplot import get
import functions
from functions import custom
import Run_Optimization
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import OptimizationInputs
from multipleRun import MultipleRun
#Optimization Algorthms
from enumOptimizations import Optimizations
from solution import solution
from write_operations import WriteOperations
from enumFunctions import Functions

class MatplotlibWidget(QMainWindow):
    inputs = [] 
    inputs.append(OptimizationInputs.OptimizationStructure())
    inputs.append(OptimizationInputs.OptimizationStructure())
    inputs.append(OptimizationInputs.OptimizationStructure())
    inputs.append(OptimizationInputs.OptimizationSMAStructure())
    inputs.append(OptimizationInputs.OptimizationSMAStructure())
    inputs.append(OptimizationInputs.OptimizationSMAStructure())


    def __init__(self):
        
        QMainWindow.__init__(self)

        loadUi("UI/qt_designer.ui",self)
        AddItemsToComboBox(self)
        

        self.setWindowTitle("Optimization Algorthms")
        #Set button functions
        
        self.pushButton.clicked.connect(self.Plot)
        self.infoButton.clicked.connect(self.InfoButton)
        self.inputButton.clicked.connect(self.InputButton1)
        self.inputButton_2.clicked.connect(self.InputButton2)
        self.inputButton_3.clicked.connect(self.InputButton3)
        #Fill the multi run textbox
        self.multiRunTextBox.setText("1")

        self.functionComboBox.currentIndexChanged.connect(self.CustomFunctionSelected)
        self.functionTextbox.setVisible(False)
        self.functionLabel.setVisible(False)
        
       
        
        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))

    def CustomFunctionSelected(self):
         if self.functionComboBox.currentIndex()==Functions.custom:
            self.functionTextbox.setVisible(True)
            self.functionLabel.setVisible(True)
         else: 
            self.functionTextbox.setVisible(False)
            self.functionLabel.setVisible(False)

    def InfoButton(self):

        switcher = {
            0: 'UI/ackleyFunctionWindow.ui',
            1: 'UI/DixonPriceFunctionWindow.ui',
            2: 'UI/GriewankFunctionWindow.ui',
            3: 'UI/MichalewiczFunctionWindow.ui',
            4: 'UI/PermFunctionWindow.ui',
            5: 'UI/PowellFunctionWindow.ui',
            6: 'UI/PowerSumFunctionWindow.ui',
            7: 'UI/rastriginFunctionWindow.ui',
            8: 'UI/rosenbrockFunctionWindow.ui',
            9: 'UI/schwefelFunctionWindow.ui',
            10: 'UI/sphereFunctionWindow.ui',
            11: 'UI/sum2FunctionWindow.ui',
            12: 'UI/tridFunctionWindow.ui',
            13: 'UI/zakharovFunctionWindow.ui',
            14: 'UI/ellipseFunctionWindow.ui',
            15: 'UI/nesterovFunctionWindow.ui',
            16: 'UI/saddleFunctionWindow.ui',
            17: ''
        }
        infowindow=switcher.get(self.functionComboBox.currentIndex(), "nothing")

        if self.functionComboBox.currentIndex()==Functions : #Check if custom selected   
            return
        else: 
            self.window = PyQt5.QtWidgets.QMainWindow()
            loadUi(infowindow, self.window)           
        self.window.show()
        self.window.okButton.clicked.connect(self.CloseUI)          

    def Plot(self,sol):
        opt = Optimizations(self.optimizationComboBox.currentIndex())
        opt2 = Optimizations(self.optimizationComboBox_2.currentIndex())
        opt3 = Optimizations(self.optimizationComboBox_3.currentIndex())
        if self.functionTextbox.toPlainText()!="":
            functions.createFunction(str(self.functionTextbox.toPlainText()))

      
        param1 = self.functionComboBox.currentIndex(),int(self.inputs[0].MaxIter),int(self.inputs[0].dimension),int(self.inputs[0].searchAgentsNo),int(self.inputs[0].lb),int(self.inputs[0].ub)
        param2 = self.functionComboBox.currentIndex(),int(self.inputs[1].MaxIter),int(self.inputs[1].dimension),int(self.inputs[1].searchAgentsNo),int(self.inputs[1].lb),int(self.inputs[1].ub)
        param3 = self.functionComboBox.currentIndex(),int(self.inputs[2].MaxIter),int(self.inputs[2].dimension),int(self.inputs[2].searchAgentsNo),int(self.inputs[2].lb),int(self.inputs[2].ub)
        paramSMA1 = self.functionComboBox.currentIndex(), int(self.inputs[3].problem_size), self.inputs[3].verbose,int(self.inputs[3].epoch),int(self.inputs[3].pop_size),int(self.inputs[3].smalb),int(self.inputs[3].smaub)
        paramSMA2 = self.functionComboBox.currentIndex(), int(self.inputs[4].problem_size), self.inputs[4].verbose,int(self.inputs[4].epoch),int(self.inputs[4].pop_size),int(self.inputs[4].smalb),int(self.inputs[4].smaub)
        paramSMA3 = self.functionComboBox.currentIndex(), int(self.inputs[5].problem_size), self.inputs[5].verbose,int(self.inputs[5].epoch),int(self.inputs[5].pop_size),int(self.inputs[5].smalb),int(self.inputs[5].smaub)

        if self.optimizationComboBox_2.currentIndex()==Optimizations.NONE and self.optimizationComboBox_3.currentIndex()==Optimizations.NONE :
            #Run single algorithm
            opt = Optimizations(self.optimizationComboBox.currentIndex())
            sol = MultipleRun(opt,param1,paramSMA1,int(self.multiRunTextBox.toPlainText()))
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(sol.convergence)
            self.MplWidget.canvas.axes.legend((opt.name, 'Best fitness'),loc='upper right')
            functionName = Functions(self.functionComboBox.currentIndex())
            WriteOperations(opt.name,functionName.name,sol).write()        
        elif self.optimizationComboBox_2.currentIndex()!=Optimizations.NONE and self.optimizationComboBox_3.currentIndex()==Optimizations.NONE :
            #Run double first and second algorithm
            sol, sol2 = Run_Optimization.Double(opt, opt2,param1,param2,paramSMA1,paramSMA2,int(self.multiRunTextBox.toPlainText()),int(self.multiRunTextBox_2.toPlainText()))
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(sol.convergence)
            self.MplWidget.canvas.axes.plot(sol2.convergence)
            self.MplWidget.canvas.axes.legend((opt.name, opt2.name),loc='upper right')
        elif self.optimizationComboBox_2.currentIndex()==Optimizations.NONE and self.optimizationComboBox_3.currentIndex()!=Optimizations.NONE :     
            #Run double first and third algorithm
            sol, sol2 = Run_Optimization.Double(opt, opt3,param1,param3,paramSMA1,paramSMA2,int(self.multiRunTextBox.toPlainText()),int(self.multiRunTextBox_3.toPlainText()))
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(sol.convergence)
            self.MplWidget.canvas.axes.plot(sol2.convergence)
            self.MplWidget.canvas.axes.legend((opt.name, opt3.name),loc='upper right')
        else:
            #Run all algorithms
            sol, sol2, sol3 = Run_Optimization.Triple(opt, opt2,opt3,param1,param2,param3,paramSMA1,paramSMA2,paramSMA3,int(self.multiRunTextBox.toPlainText()),int(self.multiRunTextBox_2.toPlainText()),int(self.multiRunTextBox_3.toPlainText()))
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(sol.convergence)
            self.MplWidget.canvas.axes.plot(sol2.convergence)
            self.MplWidget.canvas.axes.plot(sol3.convergence)
            self.MplWidget.canvas.axes.legend((opt.name, opt2.name,opt3.name),loc='upper right')
        self.MplWidget.canvas.axes.set_title('Convergence curve')
        self.MplWidget.canvas.draw()

    def InputButton(self,isSMA,input):
            if  isSMA:
                #SMA
                self.window = PyQt5.QtWidgets.QMainWindow()
                loadUi('UI/SMA_Inputs.ui', self.window)
                self.window.show()
                self.window.smaButton.clicked.connect(lambda: self.CloseUI())
                #Set predefined values & Set inputs
                self.window.problemSizeTextBox.setText(str(self.inputs[input+3].problem_size))
                self.window.verboseCheckBox.setChecked(self.inputs[input+3].verbose)
                self.window.epochTextBox.setText(str(self.inputs[input+3].epoch))
                self.window.popSizeTextBox.setText(str(self.inputs[input+3].pop_size))
                self.window.lbTextBox.setText(str(self.inputs[input+3].smalb))
                self.window.ubTextBox.setText(str(self.inputs[input+3].smaub))
                #Subscribe textboxes to textchange event
                self.window.problemSizeTextBox.textChanged.connect(lambda: self.UpdateInputsSMA(input))
                self.window.verboseCheckBox.stateChanged.connect(lambda: self.UpdateInputsSMA(input))
                self.window.epochTextBox.textChanged.connect(lambda: self.UpdateInputsSMA(input))
                self.window.popSizeTextBox.textChanged.connect(lambda: self.UpdateInputsSMA(input))
                self.window.lbTextBox.textChanged.connect(lambda: self.UpdateInputsSMA(input))
                self.window.ubTextBox.textChanged.connect(lambda: self.UpdateInputsSMA(input))
            else:
                #Other Optimizations
                self.window = PyQt5.QtWidgets.QMainWindow()
                loadUi('UI/Inputs.ui', self.window)
                self.window.show()
                self.window.hhoButton.clicked.connect(lambda: self.CloseUI())
                #Set predefined values & Set inputs
                self.window.maxIterationTextBox.setText(str(self.inputs[input].MaxIter))
                self.window.dimensionTextBox.setText(str(self.inputs[input].dimension))
                self.window.searchAgentsTextBox.setText(str(self.inputs[input].searchAgentsNo))
                self.window.lbTextBox.setText(str(self.inputs[input].lb))
                self.window.ubTextBox.setText(str(self.inputs[input].ub))               
                #Subscribe textboxes to textchange event
                self.window.maxIterationTextBox.textChanged.connect(lambda: self.UpdateInputsOther(input))
                self.window.dimensionTextBox.textChanged.connect(lambda: self.UpdateInputsOther(input))
                self.window.searchAgentsTextBox.textChanged.connect(lambda: self.UpdateInputsOther(input))
                self.window.lbTextBox.textChanged.connect(lambda: self.UpdateInputsOther(input))
                self.window.ubTextBox.textChanged.connect(lambda: self.UpdateInputsOther(input))
               
    def InputButton1(self):
        isSMA = self.optimizationComboBox.currentIndex()==Optimizations.SMA
        self.InputButton(isSMA,0)
    def InputButton2(self):
        if self.optimizationComboBox_2.currentText()=="None" :
            return
        isSMA = self.optimizationComboBox_2.currentIndex()==Optimizations.SMA
        self.InputButton(isSMA,1)
    def InputButton3(self):
        if self.optimizationComboBox_3.currentText()=="None" :
            return
        isSMA = self.optimizationComboBox_3.currentIndex()==Optimizations.SMA
        self.InputButton(isSMA,2)        
     
    #HHO input window    
    def UpdateInputsOther(self,inputNumber):
        self.inputs[inputNumber].MaxIter=self.window.maxIterationTextBox.toPlainText()
        self.inputs[inputNumber].dimension=self.window.dimensionTextBox.toPlainText()
        self.inputs[inputNumber].searchAgentsNo=self.window.searchAgentsTextBox.toPlainText()
        self.inputs[inputNumber].lb=self.window.lbTextBox.toPlainText()
        self.inputs[inputNumber].ub=self.window.ubTextBox.toPlainText()     
    def UpdateInputsSMA(self,inputNumber):
        self.inputs[inputNumber+3].problem_size=self.window.problemSizeTextBox.toPlainText()
        self.inputs[inputNumber+3].verbose=self.window.verboseCheckBox.isChecked()
        self.inputs[inputNumber+3].epoch=self.window.epochTextBox.toPlainText()
        self.inputs[inputNumber+3].pop_size=self.window.popSizeTextBox.toPlainText()
        self.inputs[inputNumber+3].smalb=self.window.lbTextBox.toPlainText()
        self.inputs[inputNumber+3].smaub=self.window.ubTextBox.toPlainText()
    def CloseUI(self):
        self.window.close()    
    #SMA InpuWindow
    #=================
    #=================
    #=================
    
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
        self.functionComboBox.addItem('custom')

        #Add items to optimization combo Box
        for x in range(3):
            if x==0:
                AddToOptimizationCombobox(self.optimizationComboBox)
            elif x==1:
                AddToOptimizationCombobox(self.optimizationComboBox_2)
                self.optimizationComboBox_2.addItem('None')
                self.optimizationComboBox_2.setCurrentIndex(Optimizations.NONE)
            elif x==2:
                AddToOptimizationCombobox(self.optimizationComboBox_3)
                self.optimizationComboBox_3.addItem('None')
                self.optimizationComboBox_3.setCurrentIndex(Optimizations.NONE)
                
        

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