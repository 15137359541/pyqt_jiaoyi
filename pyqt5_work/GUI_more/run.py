# coding:utf-8
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqt5_work.GUI_more.main_window import FirstMainWindow
from pyqt5_work.GUI_more.Ui_one import Ui_Dialog1
from pyqt5_work.GUI_more.Ui_two import Ui_Dialog2

# part 1
# 实例化启动qt应用
app = QtWidgets.QApplication(sys.argv)
#  取得UI class 的实例
the_mainwindow = FirstMainWindow()

# part 2 登录mysql
Dialog1 = QtWidgets.QDialog()
ui1 = Ui_Dialog1()
ui1.setupUi1(Dialog1)
# part 3 关于界面
Dialog2 = QtWidgets.QDialog()
ui2 = Ui_Dialog2()
ui2.setupUi2(Dialog2)

# part 4
# 设计信号-槽点
# 建立对象实例化的访问
bttn = the_mainwindow.pushButton1
bttn.clicked.connect(Dialog1.show)

bttn2 = the_mainwindow.pushButton2
bttn2.clicked.connect(Dialog2.show)

if __name__ == "__main__":
    # 展示主窗口 chenSpider
    the_mainwindow.show()
    sys.exit(app.exec_())