from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from Forms.Ui_main import Ui_MainWindow
import pyqtgraph as pg
import numpy as numpy
from scipy import interpolate
from scipy.interpolate import griddata
import mud_py_API as MudPy
import datetime

class AnalyserWindow(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.sensorList = MudPy.getSensors_All()
        self.sensorTypeList = MudPy.getSensorTypes()
        self.controlNodeList = MudPy.getControlNodes_All()
        self.controlNodeTypesList = MudPy.getControlNodeDataType()
        self.ZoneList = MudPy.getZones()
        self._fillComboBoxes()
        self._connectButtonEvents()
        date_axis_sensor = pg.DateAxisItem(orientation='bottom')
        self.sensorPlot.setAxisItems(axisItems = {'bottom': date_axis_sensor})   
        date_axis_controlNode = pg.DateAxisItem(orientation='bottom')
        self.controlNodePlot.setAxisItems(axisItems = {'bottom': date_axis_controlNode})   
        
        
    def _connectButtonEvents(self):
        self.pushButtonPlot.clicked.connect(self._on_ButtonPlotClicked)
        self.pushButtonPlotControlNode.clicked.connect(self._on_ButtonPlotControlNodeClicked)
        self.pushButtonPlotZone.clicked.connect(self._on_ButtonPlotZoneClicked)
        
    def _on_ButtonPlotControlNodeClicked(self):
        self._drawPlotOfControlNodeData()
        
    def _on_ButtonPlotClicked(self):
        self._drawPlotOfSensorData()
        
    def _on_ButtonPlotZoneClicked(self):
        self._drawPlotOfZoneSensorData()
            
    def _fillComboBoxes(self):
        self._fillComboBox(self.comboBoxSensorID, self.sensorList)
        self._fillComboBox(self.comboBoxSensorType,  self.sensorTypeList)
        self._fillComboBox(self.comboBoxControlNodeID, self.controlNodeList)
        self._fillComboBox(self.comboBoxControlNodeType, self.controlNodeTypesList)
        self._fillComboBox(self.comboBoxZone,  self.ZoneList)
        self._fillComboBox(self.comboBoxSensorTypeZone,  self.sensorTypeList)
        
    def _fillComboBox(self,  comboBoxToFill, items):
        i = 0
        for item in items:
            comboBoxToFill.insertItem(i,  str(item),  item)
            i = i +1
            
    def _drawPlotOfControlNodeData(self):
        self.controlNodePlot.getPlotItem().setLabel('left',self.comboBoxControlNodeType.currentData().id,  units = MudPy.getControlNodeDataType_Unit(self.comboBoxControlNodeType.currentData().id))
        selectedcontrolNodeData = MudPy.getControlNode_Date_TimeRange( self.comboBoxControlNodeID.currentData().id,  self.timeRangeControlNode.getStartDateTime(), self.timeRangeControlNode.getEndDateTime(),  self.comboBoxControlNodeType.currentData().id)
        self.controlNodePlot.clear()
        values = []
        for data in selectedcontrolNodeData.iterator():            
            values.append([data.timestamp.timestamp(), data.value])
        
        if len(values) == 0:
            return
            
        traceplot = self.controlNodePlot.plot([0], [0]) 
        traceplot.setData(self._getArrayFromList(values))
        
    def _drawPlotOfSensorData(self):
        self.sensorPlot.getPlotItem().setLabel('left',self.comboBoxSensorType.currentText(),  units = MudPy.getSensorDataType_Unit(self.comboBoxSensorType.currentData().id))
        selectedSensorData = MudPy.getSensorData_Date_TimeRange(self.comboBoxSensorID.currentData().id, self.timeRange.getStartDateTime(), self.timeRange.getEndDateTime(),  self.comboBoxSensorType.currentData().id)
        values = []
        self.sensorPlot.clear()
        for data in selectedSensorData.iterator():            
            values.append([data.timestamp.timestamp(), data.value])
        
        if len(values) == 0:
            return
            
        traceplot = self.sensorPlot.plot([0], [0]) 
        traceplot.setData(self._getArrayFromList(values))
    
    def  _drawPlotOfZoneSensorData(self):
        selectedSensorData = MudPy.getZoneSensorData_Date_TimeRange(self.comboBoxZone.currentData().id, self.timeRangeZone.getStartDateTime(), self.timeRangeZone.getEndDateTime(),  self.comboBoxSensorTypeZone.currentData().id )
        x = []
        y = []
        values = [] 
        coords = []
        for data in selectedSensorData.iterator():      
            x.append(data.location.location.x)
            y.append(data.location.location.y)
            values.append(data.value)
            coords.append([data.location.location.x, data.location.location.y])

        if len(values) <16:
            return
        
        #Need to replace the iterp2d with a simple collection of the maximum and minimum x and y
        zoneInterpolator = interpolate.interp2d(x, y, values, kind='cubic',  fill_value = 0.0)
        coordArray = self._getArrayFromList(coords)
        grid_x, grid_y = numpy.mgrid[zoneInterpolator.x_min:zoneInterpolator.x_max:400j, zoneInterpolator.y_max:zoneInterpolator.y_min:400j]
        smoothed = griddata(coordArray, values, (grid_x, grid_y), method='linear')
        self.zonePlot.setImage(smoothed)
        
        
    def _getArrayFromList(self, dataList):
        data = numpy.array(dataList)
        data = data[data[:,0].argsort()]
        return data
        

