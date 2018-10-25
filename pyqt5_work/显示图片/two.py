# coding:utf-8

from PyQt5 import QtGui, QtWidgets, QtCore
import sys


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("动画使用-zmister.com")  # 设置窗口标题
        self.resize(400, 200)  # 规定窗口大小
        self.main_widget = QtWidgets.QWidget()  # 创建一个widget部件

        self.grapview = QtWidgets.QGraphicsView(self.main_widget)  # 创建一个图形视图，继承自main_widget
        self.grapview.setGeometry(QtCore.QRect(10, 10, 380, 180))  # 设置图形视图的矩形区域
        self.scene = QtWidgets.QGraphicsScene()  # 创建一个图形管理场景
        self.grapview.setScene(self.scene)
        png = QtGui.QPixmap()  # 创建一个绘图类
        png.load("one.png")  # 从png中加载一个图片
        item = QtWidgets.QGraphicsPixmapItem(png)  #
        self.scene.addItem(item)

        self.setCentralWidget(self.main_widget)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())