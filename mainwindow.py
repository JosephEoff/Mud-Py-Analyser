from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from Forms.Ui_main import Ui_MainWindow

import mud_py_API as MudPy
import datetime

class AnalyserWindow(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.sensorList = MudPy.getSensors_All()
        self.sensorTypeList = MudPy.getSensorTypes()
        self.stepSizes = ['Hourly', 'Daily']
        self.fillComboBoxes()
            
    def fillComboBoxes(self):
        self.fillComboBox(self.comboBoxSensorID, self.sensorList)
        self.fillComboBox(self.comboBoxSensorType,  self.sensorTypeList)
        self.fillComboBox(self.comboBoxStepSize,  self.stepSizes)
        
    def fillComboBox(self,  comboBoxToFill, items):
        for item in items:
            comboBoxToFill.addItem(str(item))
