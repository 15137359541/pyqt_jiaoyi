5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
# coding:utf-8
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.iniUI()

    def iniUI(self):
        self.setWindowTitle("州的先生zmister.com PythonGUI教程")
        self.statusBar().showMessage("文本状态栏")
        self.resize(400, 300)

        # 创建一个菜单栏
        menu = self.menuBar()
        # 创建两个个菜单
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())