from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
#QWidget是PyQt5中所有用户界面对象的基类，因此您要创建一个继承自基类QWidget的新Form类
class Form(QWidget):
    def __init__(self,parent = None):
        super(Form,self).__init__(parent)

        #这里我们添加一个标签，一个文本编辑框和一个提交按钮
        nameLabel = QLabel('Name:')
        self.nameLine = QLineEdit()
        self.submitButton = QPushButton(" Submit ")

        #我们添加了一个QVBoxLayout。QVBoxLayout类垂直排列我们的小部件
        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addWidget(nameLabel)
        buttonLayout1.addWidget(self.nameLine)
        buttonLayout1.addWidget(self.submitButton)

        self.submitButton.clicked.connect(self.submitContact)

        #创建一个栅格布局,QGridLayout将小部件放在网格中。可以使用笛卡尔坐标如图所示定位窗口小部件。
        mainLayout = QGridLayout()
        mainLayout.addLayout(buttonLayout1,0,1)


        #将QGridLayout设置为窗口的主布局。之后我们设置它的标题。
        self.setLayout(mainLayout)
        self.setWindowTitle('hello QT')

    def submitContact(self):
        name = self.nameLine.text()

        if name == '':
            QMessageBox.information(self,'Empty FIled','please enter a name and address')
            return
        else:
            QMessageBox.information(self,'Success!','helos %s' %name)

if __name__=='__main__':
    import sys
    app = QApplication(sys.argv)

    screen = Form()
    screen.show()

    sys.exit(app.exec_())