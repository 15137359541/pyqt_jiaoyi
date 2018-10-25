
# coding:utf-8
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget,QGridLayout
from PyQt5.QtCore import Qt



class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.iniUI()

    def iniUI(self):
        self.setWindowTitle("州的先生zmister.com PythonGUI教程")
        self.resize(400, 300)
        self.add_menu_and_statu()
        #垂直布局
        self.horizontal_vertical_box_layout()
        #栅格布局
        self.grid_layout()#会将垂直布局覆盖，即，只显示栅格布局

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

    # 水平垂直布局
    def horizontal_vertical_box_layout(self):
        # 两个标签
        label_1 = QLabel('第一个标签')
        label_2 = QLabel('第二个标签')

        # 两个按钮
        button_1 = QPushButton('第一个按钮')
        button_2 = QPushButton('第二个按钮')

        # 创建两个水平盒子
        hbox_1 = QHBoxLayout()
        hbox_2 = QHBoxLayout()

        # 在水平盒子1中添加一个标签和一个按钮
        hbox_1.addWidget(label_1)
        hbox_1.addWidget(button_1)

        # 在水平盒子2中添加标签2和按钮2
        hbox_2.addWidget(label_2)
        hbox_2.addWidget(button_2)

        # 创建一个垂直盒子，包含两个水平盒子
        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)

        # 创建一个窗口部件，设置布局为垂直盒子
        layout_widget = QWidget()
        layout_widget.setLayout(vbox)

        self.setCentralWidget(layout_widget)
        # 网格布局

    def grid_layout(self):
        # 两个标签
        label_1 = QLabel('第一个标签')
        label_2 = QLabel('第二个标签')

        # 两个按钮
        button_1 = QPushButton('第一个按钮')
        button_2 = QPushButton('第二个按钮')
        button_3 = QPushButton("第三个按钮")

        # 创建一个网格布局对象
        grid_layout = QGridLayout()

        # 在网格中添加窗口部件
        grid_layout.addWidget(label_1, 0, 0)  # 放置在0行0列
        grid_layout.addWidget(button_1, 0, 1)  # 0行1列
        grid_layout.addWidget(label_2, 1, 0)  # 1行0列
        grid_layout.addWidget(button_2, 1, 1)  # 1行1列

        grid_layout.addWidget(button_3, 2, 0, 1, 5)#在2行0列的位置，跨越1行5列，让其占1行和5列

        # 对齐方式
        grid_layout.setAlignment(Qt.AlignTop)
        #对窗口小部件单独设置对齐方式
        grid_layout.setAlignment(label_1, Qt.AlignRight)

        # 创建一个窗口对象
        layout_widget = QWidget()
        # 设置窗口的布局层
        layout_widget.setLayout(grid_layout)

        self.setCentralWidget(layout_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())