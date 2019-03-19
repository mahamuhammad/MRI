import numpy as np
import random
import time
from PIL import Image ,ImageEnhance
import numpy as np
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog , QMessageBox,QApplication
from PyQt5.QtGui import QPixmap
from part1 import Ui_MainWindow
import sys
import qimage2ndarray
np.set_printoptions(threshold=np.nan)

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Image_display.setGeometry(QtCore.QRect(170, 30, 256, 256))
        
            
	    array = np.zeros((256,256))
        array[10:100,10:100] = 140
        array1 = np.zeros((256,256))
        array1[80:200,80:200] = 90
        M=array+array1
        
        m=self.adding_image_to_lbl(M)
        self.ui.lbl_phantom.setPixmap(m
                                      
    def adding_image_to_lbl(self , array):
        S= qimage2ndarray.array2qimage(array)
        S.save("s.jpg")
        pixmap = QPixmap("s.jpg")
        pixmap = pixmap.scaled(int(pixmap.height()), int(pixmap.width()), QtCore.Qt.KeepAspectRatio)
        return pixmap)
        
        
        
def main(): 
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
     