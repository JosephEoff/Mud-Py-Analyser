from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from Forms.Ui_main import Ui_MainWindow
import pyqtgraph as pg
import numpy as numpy
from scipy.interpolate import griddata
import mud_py_API as MudPy
from datetime import  timedelta

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
        self.zoneTimestamps = []
        self._connectZonePlotEvents()
    
        
    def _connectZonePlotEvents(self):
        self.zonePlot.sigTimeChanged.connect(self._changeZonePlotTimeDisplay)
    
    def _connectButtonEvents(self):
        self.pushButtonPlot.clicked.connect(self._on_ButtonPlotClicked)
        self.pushButtonPlotControlNode.clicked.connect(self._on_ButtonPlotControlNodeClicked)
        self.pushButtonPlotZone.clicked.connect(self._on_ButtonPlotZoneClicked)
        self.pushButtonZonePlay.clicked.connect(self._onButtonZonePlayClicked)
        
    def _on_ButtonPlotControlNodeClicked(self):
        self._drawPlotOfControlNodeData()
        
    def _on_ButtonPlotClicked(self):
        self._drawPlotOfSensorData()
        
    def _on_ButtonPlotZoneClicked(self):
        self._drawPlotOfZoneSensorData()
        
    def _onButtonZonePlayClicked(self):
        if len(self.zoneTimestamps)>0:
            self.zonePlot.setCurrentIndex(0)
            self.zonePlot.play(self.doubleSpinBoxZonePlayHoursPerSecond.value())
            
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
    
    def _changeZonePlotTimeDisplay(self,  timeIndex,  timeValue):
        if len(self.zoneTimestamps)<1:
            return

        self.labelZonePlotDateTime.setText(self.zoneTimestamps[timeIndex].isoformat(sep= ' '))
    
    def  _drawPlotOfZoneSensorData(self):
        frames = []
        self.zoneTimestamps = []
        count = 0
        dateRangeCount = self.timeRangeZone.getRangeGeneratorCount()
        progress = 0.0
        for startTimeDate in self.timeRangeZone.dateRangeGenerator():
            if dateRangeCount>0:
                progress = 100 * float(count)/float(dateRangeCount)
                self.progressBarZonePlot.setValue(progress)
            endTimeDate = startTimeDate + self.timeRangeZone.getTimeDelta()
            selectedSensorData = MudPy.getZoneSensorData_Date_TimeRange(self.comboBoxZone.currentData().id, startTimeDate, endTimeDate,  self.comboBoxSensorTypeZone.currentData().id )
            interpolated = self._getInterpolatedGridFromSelectedSensorData(selectedSensorData)
            count = count + 1
            if not interpolated is None:
                frames.append( interpolated)
                self.zoneTimestamps.append(startTimeDate)
        
        self.progressBarZonePlot.setValue(0.0)
        
        if len(frames) == 0:
                return
        frameArray = numpy.stack(frames, axis=0)
        self.zonePlot.setImage(img = frameArray)
        
    def _getArrayFromList(self, dataList):
        data = numpy.array(dataList)
        data = data[data[:,0].argsort()]
        return data
        
    def _getInterpolatedGridFromSelectedSensorData(self, selectedSensorData):
        x_min = self.comboBoxZone.currentData().boundary.extent[0]
        x_max = self.comboBoxZone.currentData().boundary.extent[2]
        y_min = self.comboBoxZone.currentData().boundary.extent[1]
        y_max = self.comboBoxZone.currentData().boundary.extent[3]

        values = [] 
        coords = []
        for data in selectedSensorData.iterator():      
            values.append(data.value)
            coords.append([data.location.location.x, data.location.location.y])
        
        if len(coords)== 0 or len (coords)<16:
            return None
            
        coordArray = self._getArrayFromList(coords)        
        grid_x, grid_y = numpy.mgrid[x_min:x_max:400j, y_max:y_min:400j]
        interpolated = griddata(coordArray, values, (grid_x, grid_y), method='linear')
        return interpolated



