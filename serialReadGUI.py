#!/usr/bin/python

import sys, serial, time
from PyQt4 import QtGui, QtCore

class SerialCallResponseGUI(QtGui.QWidget):
    
    def __init__(self, port):
        super(SerialCallResponseGUI,self).__init__()

        self.port = port
        self.ser = serial.Serial(port=port, baudrate=9600)
        self.ser.open()

        self.initUI()

    def initUI(self):

        self.button = QtGui.QPushButton('Get Reading', self)
        self.button.resize(150, 50)
        self.button.move(125,300)
        self.button.clicked.connect(self.buttonClicked)

        self.textOut = QtGui.QLabel(self)
        self.textOut.resize(150,50)
        self.textOut.move(125,100)
        self.textOut.setAlignment(QtCore.Qt.AlignCenter)
        
        font = QtGui.QFont()
        font.setWeight(75)
        font.setPointSize(36)
        self.textOut.setFont(font)
        
        self.textOut.setFrameStyle(QtGui.QFrame.Sunken | QtGui.QFrame.Panel)

        #self.textOut.setStyleSheet(

        self.resize(400,400)
        self.move(400, 400)
        self.setWindowTitle('Ninjaneering Labs GUI')
        self.show()

    def buttonClicked(self):
        self.ser.write('x')
        startTime = time.clock()
        timeoutLength = 1
        while True:
            if self.ser.inWaiting() > 0:
                data = self.ser.readline()
                self.textOut.setText(data)
                break

            if time.clock() - startTime > timeoutLength:
                self.textOut.setText("Error")
                break



def main():
    app = QtGui.QApplication(sys.argv)
    
    port = sys.argv[1]

    window = SerialCallResponseGUI(port)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


