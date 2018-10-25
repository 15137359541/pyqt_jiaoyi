import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore
from PyQt5.QtCore import *

# 声明窗口
class Window(QWidget):
    # 初始化
    def __init__(self):
        super().__init__()
        self.initUI()
    # 设置窗口的参数
    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setFixedWidth(300)
        self.setFixedHeight(200)
        self.setWindowTitle('按键检测')
        self.show()

    # 检测键盘回车按键，函数名字不要改，这是重写键盘事件
    def keyPressEvent(self, event):
        #这里event.key（）显示的是按键的编码
        print("按下：" + str(event.key()))
        # 举例，这里Qt.Key_A注意虽然字母大写，但按键事件对大小写不敏感
        if (event.key() == Qt.Key_Escape):
            print('测试：ESC')
        if (event.key() == Qt.Key_A):
            print('测试：A')
        if (event.key() == Qt.Key_1):
            print('测试：1')
        if (event.key() == Qt.Key_Enter):
            print('测试：Enter')
        if (event.key() == Qt.Key_Space):
            print('测试：Space')
        # 当需要组合键时，要很多种方式，这里举例为“shift+单个按键”，也可以采用shortcut、或者pressSequence的方法。
        if (event.key() == Qt.Key_P):
            if QApplication.keyboardModifiers() == Qt.ShiftModifier:
                print("shift + p")
            else :
                print("p")

        if (event.key() == Qt.Key_O) and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            print("shift + o")

    # 响应鼠标事件
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("鼠标左键点击")
        elif event.button() == Qt.RightButton:
            print("鼠标右键点击")
        elif event.button() == Qt.MidButton:
            print("鼠标中键点击")
        # elif event.button() ==  Qt.LeftButton | Qt.RightButton:
        #     print("鼠标左右点击")
        # elif event.button() ==  Qt.LeftButton | Qt.MidButton:
        #     print("鼠标左中键点击")
        # elif event.button() == Qt.LeftButton | Qt.MidButton | Qt.RightButton:
        #     print("鼠标中左中右键点击")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())