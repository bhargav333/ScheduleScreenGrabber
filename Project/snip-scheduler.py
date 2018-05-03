# -*- coding: utf-8 -*-
"""
Created on Thu May  3 14:07:03 2018

@author: 672028
"""
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PIL import ImageGrab
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from documentscheduler import Documentmaker
import time 
    
class MySnippingtool(QtWidgets.QWidget):
    img_path = 'C:/Users/672028/Pictures/Project/capture.png'
    doc_path = 'C:/Users/672028/Pictures/Project/demo.docx'
    keyPressed = QtCore.pyqtSignal(QtCore.QEvent)
    def __init__(self):
        super().__init__()
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.setGeometry(0, 0, screen_width, screen_height)
        self.setWindowTitle(' ')
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.01)
        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        print('Capture the screen...')
        self.show()
        self.keyPressed.connect(self.on_key)
        
    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        self.keyPressed.emit(event)
        
    def on_key(self, event): 
        if event.key() == QtCore.Qt.Key_Q:
            print("Killing")
            self.deleteLater()  # a test I implemented to see if pressing 'Q' would close the window
    
    def paintEvent(self, event):
            qp = QtGui.QPainter(self)
            qp.setPen(QtGui.QPen(QtGui.QColor('black'), 3))
            qp.setBrush(QtGui.QColor(128, 128, 255, 128))
            qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()
    
    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()

        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())

        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        img.save(self.img_path)
        Documentmaker(self.img_path,self.doc_path)
if __name__ == '__main__':
    start = time.time()
    app = QtWidgets.QApplication(sys.argv)
    window = MySnippingtool()
    window.show()
    end = time.time()
    print(end - start)
    sys.exit(app.exec_())
