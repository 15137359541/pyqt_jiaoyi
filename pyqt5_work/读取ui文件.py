# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QDialog,QApplication
from ui_Login import Ui_MainWindow

class Login(QDialog):
    """登录窗口"""
    def __init__(self, parent = None):
        super(Login, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.labelTips.hide()
        # 连接槽函数登录按钮
        self.ui.pushButtonOK.clicked.connect(self.slotLogin)
        # 连接槽函数退出按钮
        self.ui.pushButtonCancel.clicked.connect(self.slotCancle)

    def slotLogin(self):
        if self.ui.lineEditUser.text() != "admin" or self.ui.lineEditPassword.text() != "123456":
            self.ui.labelTips.show()
            self.ui.labelTips.setText("用户名或密码错误！")
        else:
            self.accept()

    def slotCancle(self):
        self.reject()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    if login.exec():
        print('登录成功')
    else:
        print('登录退出')
    sys.exit(app.exec())