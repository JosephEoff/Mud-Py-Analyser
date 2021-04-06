# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dev/GitHub/Mud-Py-Analyser/Forms/timerangepicker.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TimeRangePicker(object):
    def setupUi(self, TimeRangePicker):
        TimeRangePicker.setObjectName("TimeRangePicker")
        TimeRangePicker.resize(240, 190)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TimeRangePicker.sizePolicy().hasHeightForWidth())
        TimeRangePicker.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(TimeRangePicker)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxDate_TimeRange = QtWidgets.QGroupBox(TimeRangePicker)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxDate_TimeRange.sizePolicy().hasHeightForWidth())
        self.groupBoxDate_TimeRange.setSizePolicy(sizePolicy)
        self.groupBoxDate_TimeRange.setObjectName("groupBoxDate_TimeRange")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBoxDate_TimeRange)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.groupBoxDate_TimeRange)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBoxQuickPick = QtWidgets.QComboBox(self.groupBoxDate_TimeRange)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxQuickPick.sizePolicy().hasHeightForWidth())
        self.comboBoxQuickPick.setSizePolicy(sizePolicy)
        self.comboBoxQuickPick.setObjectName("comboBoxQuickPick")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxQuickPick)
        self.labelStart = QtWidgets.QLabel(self.groupBoxDate_TimeRange)
        self.labelStart.setObjectName("labelStart")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelStart)
        self.dateTimeEditStart = QtWidgets.QDateTimeEdit(self.groupBoxDate_TimeRange)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEditStart.sizePolicy().hasHeightForWidth())
        self.dateTimeEditStart.setSizePolicy(sizePolicy)
        self.dateTimeEditStart.setCalendarPopup(True)
        self.dateTimeEditStart.setObjectName("dateTimeEditStart")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dateTimeEditStart)
        self.labelEnd = QtWidgets.QLabel(self.groupBoxDate_TimeRange)
        self.labelEnd.setObjectName("labelEnd")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelEnd)
        self.dateTimeEditEnd = QtWidgets.QDateTimeEdit(self.groupBoxDate_TimeRange)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEditEnd.sizePolicy().hasHeightForWidth())
        self.dateTimeEditEnd.setSizePolicy(sizePolicy)
        self.dateTimeEditEnd.setCalendarPopup(True)
        self.dateTimeEditEnd.setObjectName("dateTimeEditEnd")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateTimeEditEnd)
        self.labelStepSize = QtWidgets.QLabel(self.groupBoxDate_TimeRange)
        self.labelStepSize.setObjectName("labelStepSize")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelStepSize)
        self.comboBoxStepSize = QtWidgets.QComboBox(self.groupBoxDate_TimeRange)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxStepSize.sizePolicy().hasHeightForWidth())
        self.comboBoxStepSize.setSizePolicy(sizePolicy)
        self.comboBoxStepSize.setObjectName("comboBoxStepSize")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBoxStepSize)
        self.verticalLayout.addWidget(self.groupBoxDate_TimeRange)

        self.retranslateUi(TimeRangePicker)
        QtCore.QMetaObject.connectSlotsByName(TimeRangePicker)

    def retranslateUi(self, TimeRangePicker):
        _translate = QtCore.QCoreApplication.translate
        TimeRangePicker.setWindowTitle(_translate("TimeRangePicker", "Form"))
        self.groupBoxDate_TimeRange.setTitle(_translate("TimeRangePicker", "Date/Time Range"))
        self.label.setText(_translate("TimeRangePicker", "Quick pick"))
        self.labelStart.setText(_translate("TimeRangePicker", "Start"))
        self.labelEnd.setText(_translate("TimeRangePicker", "End"))
        self.labelStepSize.setText(_translate("TimeRangePicker", "Step Size"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TimeRangePicker = QtWidgets.QWidget()
    ui = Ui_TimeRangePicker()
    ui.setupUi(TimeRangePicker)
    TimeRangePicker.show()
    sys.exit(app.exec_())
