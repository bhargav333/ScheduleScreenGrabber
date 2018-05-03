# -*- coding: utf-8 -*-
"""
Created on Thu May  3 18:14:22 2018

@author: 672028
"""


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):
        self.statusBar().showMessage('Hello')
        self.setGeometry(300,300,250,250)
        self.setWindowTitle('StatusBar')
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    sys.exit(app.exec())
        
        
        