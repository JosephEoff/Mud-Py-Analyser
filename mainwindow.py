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
        self.controlNodeList = MudPy.getControlNodes_All()
        self.controlNodeTypesList = MudPy.getControlNodeDataType()
        self._fillComboBoxes()
        self._connectButtonEvents()
        date_axis_sensor = pg.DateAxisItem(orientation='bottom')
        self.sensorPlot.setAxisItems(axisItems = {'bottom': date_axis_sensor})   
        date_axis_controlNode = pg.DateAxisItem(orientation='bottom')
        self.controlNodePlot.setAxisItems(axisItems = {'bottom': date_axis_controlNode})   
    def _connectButtonEvents(self):
        self.pushButtonPlot.clicked.connect(self.on_ButtonPlotClicked)
        self.pushButtonPlotControlNode.clicked.connect(self._on_ButtonPlotControlNodeClicked)
        
    def _on_ButtonPlotControlNodeClicked(self):
        self._drawPlotOfControlNodeData()
        
    def on_ButtonPlotClicked(self):
        self._drawPlotOfSensorData()
            
    def _fillComboBoxes(self):
        self._fillComboBox(self.comboBoxSensorID, self.sensorList)
        self._fillComboBox(self.comboBoxSensorType,  self.sensorTypeList)
        self._fillComboBox(self.comboBoxControlNodeID, self.controlNodeList)
        self._fillComboBox(self.comboBoxControlNodeType, self.controlNodeTypesList)
        
    def _fillComboBox(self,  comboBoxToFill, items):
        for item in items:
            comboBoxToFill.addItem(str(item))
            
    def _drawPlotOfControlNodeData(self):
        self.controlNodePlot.getPlotItem().setLabel('left',self.comboBoxControlNodeType.currentText(),  units = MudPy.getControlNodeDataType_Unit(self.comboBoxControlNodeType.currentText()))
        selectedcontrolNodeData = MudPy.getControlNode_Date_TimeRange( self.comboBoxControlNodeID.currentText(),  self.timeRangeControlNode.getStartDateTime(), self.timeRangeControlNode.getEndDateTime(),  self.comboBoxControlNodeType.currentText())
        self.controlNodePlot.clear()
        values = []
        for data in selectedcontrolNodeData .iterator():            
            values.append([data.timestamp.timestamp(), data.value])
        
        if len(values) == 0:
            return
            
        traceplot = self.controlNodePlot.plot([0], [0]) 
        traceplot.setData(self._getArrayFromList(values))
        
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
        

