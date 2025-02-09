#!/usr/bin/python
#
# Copyright 2016 British Broadcasting Corporation and Contributors(1)
# Copyright 2025 Davy Robertson - updated to PySide6 and dedicated to Windows...
#
# (1) Contributors are listed in the AUTHORS file (please extend AUTHORS,
#     not this header)
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance this license (or the alternative
# license below).
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# This file is also alternatively licensed under the terms of the GPL
# version 2. You may obtain a copy of the license at:
#
#     http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys
import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
    QFileDialog,
    QMessageBox
)







#class MicrobugLoader():
class MicrobugLoader(QMainWindow):

    def __init__(self):
        super(MicrobugLoader, self).__init__()
        self.initUI()

    def initUI(self):

        self.loadedHexFile = ""
        
        self.setWindowTitle("Microbug Loader")
        self.btn_is_checked = True

        self.btn = QPushButton('Load Arduino Hex file!')
        #self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        #self.btn.setGeometry(300, 340, 180, 30)

        # Erase the bug'
        self.btnErase = QPushButton(' ERASE MICROBUG!')
        #self.btnErase.move(20, 20)
        self.btnErase.clicked.connect(self.eraseDevice)
        #self.btnErase.setGeometry(300, 340, 180, 30)

        # Erase the bug'
        self.btnFlash = QPushButton('PROGRAM/FLASH MICROBUG!')
        #self.btnErase.move(20, 20)
        self.btnFlash.clicked.connect(self.flashDevice)
        #self.btnErase.setGeometry(300, 340, 180, 30)

        self.lableHexFileName = QLabel("Loaded: ")
        self.lableHexFile = QLabel("TBC")

        ' Hex File name and layout '
        hexfileLayout = QHBoxLayout()
        hexfileLayout.addWidget(self.lableHexFileName)
        hexfileLayout.addWidget(self.lableHexFile)

        # Get a layout for horizonal - keep it simple 
        buttonsLayout = QHBoxLayout()
        
        buttonsLayout.addWidget(self.btn)
        buttonsLayout.addWidget(self.btnErase)
        buttonsLayout.addWidget(self.btnFlash)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(hexfileLayout)
        mainLayout.addLayout(buttonsLayout)

        window = QWidget()
        window.setLayout(mainLayout)
        self.setCentralWidget(window)

        return



        self.btn = QApplication.QPushButton('PROGRAM MICROBUG!', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        self.btn.setGeometry(300, 340, 180, 30)

        pixmap = QtGui.QPixmap("microbug-small.jpg")

        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(pixmap))

        self.setPalette(palette)
        self.setWindowTitle('Microbug Loader')
        self.setGeometry(300, 300, 512, 384)
        #self.show()


    def flashDevice(self, filename):
        print ("Flashing the device - needs to be in DFU mode")
        os.system('..\\dfu\\dfu-programmer atmega32u4 flash "' + self.loadedHexFile +'"')
        os.system('..\\dfu\\dfu-programmer atmega32u4 launch --no-reset ')

    def eraseDevice(self):
        print ("DFU Erase the device... ")
        os.system("..\\dfu\\dfu-programmer atmega32u4 erase --force")

    def checkHexfileIsMicrobugFile(self): # This could be checked by looking for a magic string sequence
        return True

    def waitDeviceReady(self):
        # get devices plugged in to USB
        old_device_lines = []
        while True:
            while True:
                device_lines = os.popen('lsusb').readlines()
                if old_device_lines != device_lines:
                    old_device_lines = device_lines
                    break
                else:
                    sleep(1)
            #
            print ("CHANGE IN USB DEVICES")
            #
            devices = []
            for device_line in device_lines:
                parts = device_line.split()
                _, busid, _, deviceid, _, usbid = parts[0:6]
                usbid = usbid.lower()
                devices.append(usbid)
            #
            if "2341:8036" in devices:
                print ("You need to plug in the device in 'program me' mode")
                print ("You do this by plugging in an holding down button A")
            #
            if "03eb:2ff4" in devices:
                print ("The device is now in program me mode, and will now")
                print ("flash the device with your hex file")
                return

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self):
        print("Clicked!")
        #print("Checked?", checked)

    def showDialog(self):
        print ("Open the Hex File")
        
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', '../compiler/microbug/build/arduino.avr.leonardo')
        self.lableHexFile.setText(fname)
        self.loadedHexFile = fname

        button = QMessageBox.critical(
            self,
            "Loader",
            "Go ahead and erase and load the Hex file ? You need to be in DFU mode",
            buttons=QMessageBox.Yes | QMessageBox.No ,
            defaultButton=QMessageBox.No,
        )

        if button == QMessageBox.No:
            print("Hex file loaded - no upload!")
            
            return
        elif button == QMessageBox.Yes:
            print("Lets go ahead")
        
        if fname:
            self.waitDeviceReady()
            self.eraseDevice()
            self.flashDevice(fname)



def main():

    
    app = QApplication(sys.argv)

    window = MicrobugLoader()
    window.show()

    #app = QtGui.QApplication(sys.argv)
    #ex = MicrobugLoader()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
