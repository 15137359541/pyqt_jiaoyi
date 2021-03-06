import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
################################################
#######创建主窗口
################################################
class FirstMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('主界面')

        ###### 创建界面 ######
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.Layout = QVBoxLayout(self.centralwidget)

        # 设置顶部三个按钮
        self.topwidget = QWidget()
        self.Layout.addWidget(self.topwidget)
        self.buttonLayout = QHBoxLayout(self.topwidget)

        self.pushButton1 = QPushButton()
        self.pushButton1.setText("打开主界面")
        self.buttonLayout.addWidget(self.pushButton1)

        self.pushButton2 = QPushButton()
        self.pushButton2.setText("打开对话框")
        self.buttonLayout.addWidget(self.pushButton2)

        self.pushButton3 = QPushButton()
        self.pushButton3.setText("打开提示框")
        self.buttonLayout.addWidget(self.pushButton3)



        # 设置中间文本
        self.label = QLabel()
        self.label.setText("第一个主界面")
        self.label.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Roman times", 50, QFont.Bold))
        self.Layout.addWidget(self.label)

        # 设置状态栏
        self.statusBar().showMessage("当前用户：mxh")

        # 窗口最大化
        self.showMaximized()

        ###### 三个按钮事件 ######

        self.pushButton3.clicked.connect(self.on_pushButton3_clicked)




    # 按钮三：打开提示框
    def on_pushButton3_clicked(self):
        QMessageBox.information(self, "提示", "这是information框！")
        #QMessageBox.question(self, "提示", "这是question框！")
        #QMessageBox.warning(self, "提示", "这是warning框！")
        #QMessageBox.about(self, "提示", "这是about框！")


################################################
#######程序入门
################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_mainwindow = FirstMainWindow()
    the_mainwindow.show()
    sys.exit(app.exec_())