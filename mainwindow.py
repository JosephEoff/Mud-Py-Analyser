from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from Forms.Ui_main import Ui_MainWindow
import pyqtgraph as pg
import numpy as numpy
import mud_py_API as MudPy
import datetime

class AnalyserWindow(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.sensorList = MudPy.getSensors_All()
        self.sensorTypeList = MudPy.getSensorTypes()
        self._fillComboBoxes()
        self._connectButtonEvents()
        date_axis = pg.DateAxisItem(orientation='bottom')
        self.sensorPlot.setAxisItems(axisItems = {'bottom': date_axis})   
        
    def _connectButtonEvents(self):
        self.pushButtonPlot.clicked.connect(self.on_ButtonPlotClicked)
        
    def on_ButtonPlotClicked(self):
        self._drawPlotOfSensorData()
            
    def _fillComboBoxes(self):
        self._fillComboBox(self.comboBoxSensorID, self.sensorList)
        self._fillComboBox(self.comboBoxSensorType,  self.sensorTypeList)
        
    def _fillComboBox(self,  comboBoxToFill, items):
        for item in items:
            comboBoxToFill.addItem(str(item))
            
    def _drawPlotOfSensorData(self):
        self.sensorPlot.getPlotItem().setLabel('left',self.comboBoxSensorType.currentText(),  units = MudPy.getSensorDataType_Unit(self.comboBoxSensorType.currentText()))
        selectedSensorData = MudPy.getSensorData_Date_TimeRange(self.comboBoxSensorID.currentText(), self.timeRange.getStartDateTime(), self.timeRange.getEndDateTime(),  self.comboBoxSensorType.currentText())
        values = []
        self.sensorPlot.clear()
        for data in selectedSensorData.iterator():            
            values.append([data.timestamp.timestamp(), data.value])
        
        if len(values) == 0:
            return
            
        traceplot = self.sensorPlot.plot([0], [0]) 
        traceplot.setData(self._getArrayFromList(values))
            
    def _getArrayFromList(self, dataList):
        data = numpy.array(dataList)
        data = data[data[:,0].argsort()]
        return data
        

