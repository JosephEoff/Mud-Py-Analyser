from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from mainwindow import AnalyserWindow

    
if __name__ == "__main__":
    QCoreApplication.setOrganizationName("JRE")
    QCoreApplication.setApplicationName("Mud-Py Analyser")
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AnalyserWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
