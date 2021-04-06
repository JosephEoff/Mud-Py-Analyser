from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget
from Forms.Ui_timerangepicker import Ui_TimeRangePicker
from Forms.StepSizes import StepSizeEnum

class TimeRangePicker( QWidget,  Ui_TimeRangePicker):
    def __init__(self, parent = None):
        super(TimeRangePicker, self).__init__(parent)
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.quickPick_Descriptions = ['-', '1 day', '7 days', '14 days', '30 days', '60 days', '120 days', '240 days',  '365 days']
        self. quickPick_Days = [0, -1, -7, -14, -30,-60, -120, -240, -365]
        self._fillComboBoxes()
        self._setDefaultDateTime()
        self.comboBoxQuickPick.currentIndexChanged.connect(self._changeRange)
        
    def _setDefaultDateTime(self):
        now = QtCore.QDateTime.currentDateTime()
        now_Time= now.time()
        now_Time.setHMS(now_Time.hour(), 0, 0, 0)
        now.setTime(now_Time)
        self.dateTimeEditStart.setDateTime(now)
        self.dateTimeEditEnd.setDateTime(now)
            
    def _fillComboBoxes(self):
        self._fillComboBox(self.comboBoxQuickPick,  self.quickPick_Descriptions)
        i=0
        for stepsize in StepSizeEnum:
            self.comboBoxStepSize.insertItem(i, stepsize.name,  stepsize)
            i = i + 1
        
    def _fillComboBox(self,  comboBoxToFill, items):
        for item in items:
            comboBoxToFill.addItem(str(item))
        
    def _changeRange(self, selectedQuickPickIndex):
        if selectedQuickPickIndex == 0:
            return
        
        self._setDefaultDateTime()
        startTime = self.dateTimeEditStart.dateTime().addDays(self. quickPick_Days[selectedQuickPickIndex])        
        self.dateTimeEditStart.setDateTime(startTime)
        
    def getStepSize(self):
        return self.self.comboBoxStepSize.currentData()   
        
    def getStartDateTime(self):
        return self.dateTimeEditStart.dateTime().toPyDateTime()
        
    def getEndDateTime(self):
        return self.dateTimeEditEnd.dateTime().toPyDateTime()
