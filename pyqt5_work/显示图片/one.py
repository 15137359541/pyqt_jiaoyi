'''
– 实例化一个QLable()部件；
– 实例化一个QPixmap()图形类；
– 通过QLabel()部件的setPixmap()方法设置QLabel()部件的图形；

'''
from PyQt5 import QtGui,QtWidgets
import sys

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('mxh-动画使用')
        self.resize(400,200)
        self.main_widget = QtWidgets.QWidget()
        self.label = QtWidgets.QLabel(self.main_widget)

        png = QtGui.QPixmap()
        png.load('one.png')
        self.label.setPixmap(png)
        self.setCentralWidget(self.main_widget)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())