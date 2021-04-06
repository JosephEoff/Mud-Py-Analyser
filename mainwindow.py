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
        self._fillComboBoxes()
            
    def _fillComboBoxes(self):
        self._fillComboBox(self.comboBoxSensorID, self.sensorList)
        self._fillComboBox(self.comboBoxSensorType,  self.sensorTypeList)
        
    def _fillComboBox(self,  comboBoxToFill, items):
        for item in items:
            comboBoxToFill.addItem(str(item))
