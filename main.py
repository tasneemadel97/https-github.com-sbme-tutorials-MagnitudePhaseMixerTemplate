from PyQt5 import QtWidgets
from task import Ui_MainWindow 
from pyqtgraph import PlotWidget
# replace <...> with your py file generate from pyuic5 command - without .py-

# It's preferaple to work on MainWindow in qt designer to support layouts
# use Dialog for relatively small windows or windows that don't have too much elements  

import sys
from imageModel import ImageModel
from cv2 import cv2
from PIL import Image
import pyqtgraph as pg
import numpy as np




class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.uploadPIC)
        # self.ui.up.clicked.connect(self.uploadPIC)
        # self.ui.magnitude.clicked.connect(self.FTMagnitude)
        self.ui.pushButton_2.clicked.connect(self.uploadPIC2)

    def uploadPIC2(self):
        self.image2 = cv2.imread('test2.jpg',0)
        drawthis = pg.ImageItem(self.image2)
        self.ui.graphicsView_6.addItem(drawthis)
        drawthis.rotate(270) 

    def uploadPIC(self):
        self.image = cv2.imread('test.jpg',0)
        drawthis = pg.ImageItem(self.image)
        self.ui.graphicsView_5.addItem(drawthis)
        drawthis.rotate(270) 

    def FTMagnitude(self):
        self.ui.graphicsView_7.clear()
        f = np.fft.fft2(self.image)
        self.magnitude = abs(f)
        self.magnitude_spectrum=20*np.log(self.magnitude)
        x= np.asarray(self.magnitude_spectrum)
        img = pg.ImageItem(x)
        self.ui.graphicsView_7.addItem(img)
    def FTPhase(self):
        self.ui.graphicsView_7.clear()
        fourier=np.fft.fft2(self.image)
        self.phase=np.angle(fourier)
        x= np.asarray(self.phase)
        PhaseImage1Array = pg.ImageItem(x)
        self.ui.graphicsView_7.addItem(PhaseImage1Array)
    def FTReal(self):
        self.ui.graphicsView_7.clear()
        fourier=np.fft.fft2(self.image)
        self.real=np.real(fourier)
        x= np.asarray(self.real)
        PhaseImage1Array = pg.ImageItem(x)
        self.ui.graphicsView_7.addItem(PhaseImage1Array)
    def FTImaginary(self):
        self.ui.graphicsView_7.clear()
        fourier=np.fft.fft2(self.image)
        self.imaginary=np.imag(fourier)
        x= np.asarray(self.imaginary)
        PhaseImage1Array = pg.ImageItem(x)
        self.ui.graphicsView_7.addItem(PhaseImage1Array)



        