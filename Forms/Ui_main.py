# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dev/GitHub/Mud-Py-Analyser/Forms/main.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(651, 532)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.summary = QtWidgets.QWidget()
        self.summary.setObjectName("summary")
        self.tabWidget.addTab(self.summary, "")
        self.zone = QtWidgets.QWidget()
        self.zone.setObjectName("zone")
        self.tabWidget.addTab(self.zone, "")
        self.sensor = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor.sizePolicy().hasHeightForWidth())
        self.sensor.setSizePolicy(sizePolicy)
        self.sensor.setObjectName("sensor")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.sensor)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBoxSensor_2 = QtWidgets.QGroupBox(self.sensor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxSensor_2.sizePolicy().hasHeightForWidth())
        self.groupBoxSensor_2.setSizePolicy(sizePolicy)
        self.groupBoxSensor_2.setTitle("")
        self.groupBoxSensor_2.setObjectName("groupBoxSensor_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBoxSensor_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxSensor = QtWidgets.QGroupBox(self.groupBoxSensor_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxSensor.sizePolicy().hasHeightForWidth())
        self.groupBoxSensor.setSizePolicy(sizePolicy)
        self.groupBoxSensor.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBoxSensor.setTitle("")
        self.groupBoxSensor.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBoxSensor.setCheckable(False)
        self.groupBoxSensor.setObjectName("groupBoxSensor")
        self.formLayout = QtWidgets.QFormLayout(self.groupBoxSensor)
        self.formLayout.setObjectName("formLayout")
        self.comboBoxSensorID = QtWidgets.QComboBox(self.groupBoxSensor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSensorID.sizePolicy().hasHeightForWidth())
        self.comboBoxSensorID.setSizePolicy(sizePolicy)
        self.comboBoxSensorID.setObjectName("comboBoxSensorID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxSensorID)
        self.labelValueType = QtWidgets.QLabel(self.groupBoxSensor)
        self.labelValueType.setObjectName("labelValueType")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelValueType)
        self.comboBoxSensorType = QtWidgets.QComboBox(self.groupBoxSensor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSensorType.sizePolicy().hasHeightForWidth())
        self.comboBoxSensorType.setSizePolicy(sizePolicy)
        self.comboBoxSensorType.setObjectName("comboBoxSensorType")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBoxSensorType)
        self.labelSensorID = QtWidgets.QLabel(self.groupBoxSensor)
        self.labelSensorID.setObjectName("labelSensorID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelSensorID)
        self.verticalLayout.addWidget(self.groupBoxSensor)
        self.timeRange = TimeRangePicker(self.groupBoxSensor_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeRange.sizePolicy().hasHeightForWidth())
        self.timeRange.setSizePolicy(sizePolicy)
        self.timeRange.setMinimumSize(QtCore.QSize(0, 20))
        self.timeRange.setObjectName("timeRange")
        self.verticalLayout.addWidget(self.timeRange)
        self.pushButtonPlot = QtWidgets.QPushButton(self.groupBoxSensor_2)
        self.pushButtonPlot.setObjectName("pushButtonPlot")
        self.verticalLayout.addWidget(self.pushButtonPlot)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addWidget(self.groupBoxSensor_2)
        self.sensorPlot = PlotWidget(self.sensor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensorPlot.sizePolicy().hasHeightForWidth())
        self.sensorPlot.setSizePolicy(sizePolicy)
        self.sensorPlot.setObjectName("sensorPlot")
        self.horizontalLayout_3.addWidget(self.sensorPlot)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.sensor, "")
        self.control_node = QtWidgets.QWidget()
        self.control_node.setObjectName("control_node")
        self.tabWidget.addTab(self.control_node, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mud-Py Analyser"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.summary), _translate("MainWindow", "Summary"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zone), _translate("MainWindow", "Zone"))
        self.labelValueType.setText(_translate("MainWindow", "Value Type"))
        self.labelSensorID.setText(_translate("MainWindow", "Sensor ID"))
        self.pushButtonPlot.setText(_translate("MainWindow", "Plot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sensor), _translate("MainWindow", "Sensor"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.control_node), _translate("MainWindow", "Control Node"))
from Forms.TimeRangePicker import TimeRangePicker
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
