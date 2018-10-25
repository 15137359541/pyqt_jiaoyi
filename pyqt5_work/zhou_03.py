# coding:utf-8
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel,QPushButton


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.iniUI()

    def iniUI(self):
        self.setWindowTitle("州的先生zmister.com PythonGUI教程")
        self.resize(400, 300)
        self.add_menu_and_statu()
        self.add_position_layout()

    # 添加菜单栏和状态栏
    def add_menu_and_statu(self):
        self.statusBar().showMessage("文本状态栏")
        # 创建一个菜单栏
        menu = self.menuBar()
        # 创建两个菜单
        file_menu = menu.addMenu("文件")
        file_menu.addSeparator()
        edit_menu = menu.addMenu('修改')

        # 创建一个行为
        new_action = QAction('新的文件', self)
        # 更新状态栏文本
        new_action.setStatusTip('打开新的文件')
        # 添加一个行为到菜单
        file_menu.addAction(new_action)

        # 创建退出行为
        exit_action = QAction('退出', self)
        # 退出操作
        exit_action.setStatusTip("点击退出应用程序")
        # 点击关闭程序
        exit_action.triggered.connect(self.close)
        # 设置退出快捷键
        exit_action.setShortcut('Ctrl+Q')
        # 添加退出行为到菜单上
        file_menu.addAction(exit_action)

    # 添加布局部件
    def add_position_layout(self):
        # 使用部件的size()方法获取部件的宽和高，使用height()方法获取部件的高度，使用width()方法获取到部件的宽度
        mbar_height = self.menuBar().height()
        print(mbar_height)
        print(self.menuBar().size())
        # 第一个标签
        label_1 = QLabel("第一个标签", self)
        #右移动10个像素，向下移动20个像素
        label_1.move(10, mbar_height)
        # 第二个标签
        label_2 = QLabel('第二个标签', self)
        label_2.move(10, mbar_height * 2)

        # 第一个按钮
        button_1 = QPushButton("按钮1", self)
        button_1.move(label_1.width(), mbar_height)
        # 第二个按钮
        button_2 = QPushButton("按钮2", self)
        button_2.move(label_2.width(), mbar_height * 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())