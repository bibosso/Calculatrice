# coding=utf8


import sys
import os
sys.path.append(os.getcwd() + "\\GUI")
from PyQt4 import QtGui
from GUI.mainWindow import Form
import qdarkstyle

def main():
    
    
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("Calculatrice")
    myapp = Form()
    myapp.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
    myapp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()