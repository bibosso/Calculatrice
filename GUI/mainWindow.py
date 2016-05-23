# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""

from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature
from GUI.Objects.NumericStringParser import NumericStringParser


from GUI.Ui_mainWindow import Ui_Form

class Form(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.nsp=NumericStringParser()
        
    ################################################################## Ecran ###################################################
    @pyqtSignature("")
    def on_textEdit_textChanged(self):
        """
        Slot documentation goes here.
        """
        if (self.textEdit.toPlainText()[-1:]) == "\n":
            try:
                self.lineEdit.setText(str(self.nsp.eval(self.textEdit.toPlainText().replace("\n", "").replace("\r", "").replace("\r\n", ""))))
            except:
                pass
    
    
    @pyqtSignature("QString")
    def on_lineEdit_textChanged(self, p0):
        """
        Slot documentation goes here.
        """
        
    
    ################################################################## Suprimé ###################################################
    @pyqtSignature("")
    def on_pushButton_6_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText()[:-1])
    
    ################################################################## Reset ###################################################
    @pyqtSignature("")
    def on_pushButton_7_clicked(self):
        """
        Slot documentation goes here.
        """
        
        self.textEdit.setText("")
        
    
    ################################################################## 0 ###################################################
    @pyqtSignature("")
    def on_pushButton_8_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "0")
    
    ################################################################## 1 ###################################################
    @pyqtSignature("")
    def on_pushButton_10_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "1")
    
    
    ################################################################## 2 ###################################################
    @pyqtSignature("")
    def on_pushButton_11_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "2")
    
    
    ################################################################## 3 ###################################################
    @pyqtSignature("")
    def on_pushButton_12_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "3")
    
    
    ################################################################## 4 ###################################################
    @pyqtSignature("")
    def on_pushButton_13_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "4")
    
    
    ################################################################## 5 ###################################################
    @pyqtSignature("")
    def on_pushButton_14_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "5")
    
    
    ################################################################## 6 ###################################################
    @pyqtSignature("")
    def on_pushButton_15_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "6")
    
    
    ################################################################## 7 ###################################################
    @pyqtSignature("")
    def on_pushButton_16_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "7")
    
    
    ################################################################## 8 ###################################################
    @pyqtSignature("")
    def on_pushButton_17_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "8")
    
    
    ################################################################## 9 ###################################################
    @pyqtSignature("")
    def on_pushButton_18_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "9")
    
    
    ################################################################## , ###################################################
    @pyqtSignature("")
    def on_pushButton_9_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + ".")
    
    
    ################################################################## + ###################################################
    @pyqtSignature("")
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "+")
    
    
    ################################################################## - ###################################################
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "-")
    
    
    ################################################################## / ###################################################
    @pyqtSignature("")
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "/")
    
    
    ################################################################## * ###################################################
    @pyqtSignature("")
    def on_pushButton_5_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "*")
    
    ################################################################## = ###################################################
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            self.lineEdit.setText(str(self.nsp.eval(self.textEdit.toPlainText().replace("\n", "").replace("\r", "").replace("\r\n", ""))))
        except:
            pass
            
    
    ################################################################## cos ###################################################
    @pyqtSignature("")
    def on_pushButton_19_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "cos()")
    
    ################################################################## sin ###################################################
    @pyqtSignature("")
    def on_pushButton_20_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "sin()")
    ################################################################## tan ###################################################
    @pyqtSignature("")
    def on_pushButton_21_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "tan()")
    
    ################################################################## abs ###################################################
    @pyqtSignature("")
    def on_pushButton_22_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "abs()")
    
    ################################################################## sgn ###################################################
    @pyqtSignature("")
    def on_pushButton_23_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "sgn()")
    
    ################################################################## acos ###################################################
    @pyqtSignature("")
    def on_pushButton_24_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "acos()")
    
    ################################################################## asin ###################################################
    @pyqtSignature("")
    def on_pushButton_25_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "asin()")
    
    ################################################################## atan ###################################################
    @pyqtSignature("")
    def on_pushButton_26_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "atan()")
    
    ##################################################################  trunc ###################################################
    @pyqtSignature("")
    def on_pushButton_27_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "trunc()")
    
    ################################################################## round ###################################################
    @pyqtSignature("")
    def on_pushButton_28_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit.setText(self.textEdit.toPlainText() + "round()")
    
    
