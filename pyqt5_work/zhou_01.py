import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
win =QWidget()
win.resize(450,150)
win.move(0,300)
win.setWindowTitle("mxh_GUI")

win.show()

sys.exit(app.exec_())