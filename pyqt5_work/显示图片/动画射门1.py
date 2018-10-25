# coding:utf-8
from PyQt5 import QtGui, QtWidgets, QtCore
import sys


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("动画使用-州的先生zmister.com")  # 设置窗口标题
        self.resize(400, 200)  # 规定窗口大小
        self.main_widget = QtWidgets.QWidget()  # 创建一个widget部件
        self.button = QtWidgets.QPushButton('射门', self.main_widget)  # 创建一个按钮
        self.button.setGeometry(10, 10, 60, 30)  # 设置按钮位置
        self.button.clicked.connect(self.shoot)

        self.label = QtWidgets.QLabel(self.main_widget)  # 创建一个文本标签部件用于显示足球
        self.label.setGeometry(50, 150, 50, 50)  # 设置足球位置
        png = QtGui.QPixmap()  # 创建一个绘图类
        png.load("足球.png")  # 从png中加载一个图片
        self.label.setPixmap(png)  # 设置文本标签的图形
        self.label.setScaledContents(True)  # 图片随文本部件的大小变动

        self.qiumen = QtWidgets.QLabel(self.main_widget)  # 创建一个文本标签部件用于显示球门
        self.qiumen.setGeometry(345, 75, 50, 50)  # 设置球门位置
        pngqiumen = QtGui.QPixmap()  # 创建一个绘图类
        pngqiumen.load("球门.png")  # 从png中加载一个图片
        self.qiumen.setPixmap(pngqiumen)  # 设置文本标签的图形

        self.path = QtGui.QPainterPath()  # 实例化一个绘制类，用于绘制动作
        self.path.moveTo(50, 150)
        self.path.cubicTo(50, 150, 50, 20, 370, 90)

        self.setCentralWidget(self.main_widget)

    # 重写patintEvent()方法
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.drawPath(self.path)  # 在图形界面上根据self.path绘制一条线条
        qp.end()


    def shoot(self):
        self.anim_x = QtCore.QPropertyAnimation(self.label, b'geometry')
        self.anim_x.setDuration(3000)
        self.anim_x.setStartValue(QtCore.QRect(50, 150, 50, 50))  # 设置动画对象的起始属性
        positionValues = [n / 10 for n in range(0, 10)]
        for n, i in enumerate(positionValues):
            x = self.path.pointAtPercent(i).x()
            y = self.path.pointAtPercent(i).y()
            z = 50 - n * 3.5
            self.anim_x.setKeyValueAt(i, QtCore.QRect(x, y, z, z))
            self.anim_x.setEndValue(QtCore.QRect(360, 90, 10, 10))
            self.anim_x.start()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())