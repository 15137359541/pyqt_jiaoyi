import sys
from PyQt5.QtWidgets import QDialog,QApplication
#重点和秘诀就在这里，大家注意看
from PyQt5.uic import loadUi


class Login(QDialog):
    """登录窗口"""
    def __init__(self, *args):
        super(Login, self).__init__(*args)
        loadUi('G:\work_st\pyqt5_work/Login.ui', self)   #看到没，瞪大眼睛看
        self.labelTips.hide()
        self.pushButtonOK.clicked.connect(self.slotLogin)
        self.pushButtonCancle.clicked.connect(self.slotCancle)

    def slotLogin(self):
        if self.lineEditUser.text() != "admin" or self.lineEditPasswd.text() != "123456":
            self.labelTips.show()
            self.labelTips.setText("用户名或密码错误！")
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