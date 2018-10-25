import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QLabel,QPushButton,QHBoxLayout,QVBoxLayout,QWidget,QGridLayout,QLineEdit,QMessageBox
from PyQt5.QtCore import Qt
from login_jukuan import JoinQuantClient
from trade_day import T_date
from buy_sell import shipanyiData
import datetime


class TradeDate(T_date):
    # 初始化第一次运行函数时的数据
    def __init__(self, username, password, backtest_id):
        self.username = username
        self.password = password
        self.backtest_id = backtest_id
        self._login_jukuan()
        self.startDate()

    def _login_jukuan(self):
        # 策略推送3-模拟交易
        self.user = JoinQuantClient(username=self.username, password=self.password, backtest_id=self.backtest_id)
        # 用户登陆
        self.user.login()
        # 从模拟的策略中获取数据
        self.res = self.user.query()

    # 初始化第一次运行函数时的数据,此函数也就运行一次。
    def startDate(self):
        self.balance = []
        for i in range(len(self.res)):
            dict1 = {}
            dict1['action'] = self.res[i].action
            dict1['completed_at'] = self.res[i].completed_at
            dict1['symbol'] = self.res[i].symbol
            dict1['price'] = self.res[i].price
            dict1['amount'] = self.res[i].amount
            if dict1 not in self.balance:
                self.balance.append(dict1)
            else:
                pass
        print('self.balance is ', self.balance)

    def _main(self):
        print('_main in ,self.balance is ', self.balance)
        print(datetime.datetime.now())
        # 重写_main 方法，判断是否可以在规定的时间段
        flag = self.mnTime()
        if flag:
            # 一分钟查询一次聚宽数据
            self.res = self.user.query()
            for i in range(len(self.res)):
                dict2 = {}

                dict2['action'] = self.res[i].action
                dict2['completed_at'] = self.res[i].completed_at
                dict2['symbol'] = self.res[i].symbol
                dict2['price'] = self.res[i].price
                dict2['amount'] = self.res[i].amount
                if dict2 not in self.balance:
                    self.balance.append(dict2)
                    print('new data is ', dict2)
                    res = shipanyiData(dict2).BS()
                    print(res)
                else:
                    print('no new data', dict2)


        else:
            pass
        print('final self.balance is ', self.balance)

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.iniUI()

    def iniUI(self):
        self.setWindowTitle('自动化运行程序')
        self.resize(400,300)
        self.add_menu_and_statu()
        self.grid_layout()

    def add_menu_and_statu(self):

        self.statusBar().showMessage('文本状态栏')
        #创建一个菜单栏
        menu = self.menuBar()
        #创建两个菜单
        file_menu = menu.addMenu('文件')
        file_menu.addSeparator()
        edit_menu = menu.addMenu('修改')

        #创建一个行为
        new_action = QAction('新的文件',self)
        #更新菜单栏文本
        new_action.setStatusTip('打开新的文件')
        #添加一个行为到菜单
        file_menu.addAction(new_action)

        #创建退出行为
        exit_action = QAction('退出',self)
        #退出操作
        exit_action.setStatusTip('点击退出应用程序')
        #点击关闭程序
        exit_action.triggered.connect(self.close)
        #设置退出快捷键
        exit_action.setShortcut('Ctrl+Q')
        #添加退出行为到菜单上
        file_menu.addAction(exit_action)

    # 网格布局
    def grid_layout(self):
        # 三个标签
        label_1 = QLabel('请输入账号名：')
        label_2 = QLabel('请输入密码：')
        label_3 = QLabel('请输入模拟序列号：')

        # 三个文本框
        self.Edit1 = QLineEdit()
        self.Edit2 = QLineEdit()
        self.Edit3 = QLineEdit()

        #一个提交按钮
        submitButton = QPushButton('运行')

        submitButton.clicked.connect(self.main_run)

        # 创建一个网格布局对象
        grid_layout = QGridLayout()

        # 在网格中添加窗口部件
        grid_layout.addWidget(label_1, 0, 0)  # 放置在0行0列
        grid_layout.addWidget(self.Edit1, 0, 1)  # 0行1列
        grid_layout.addWidget(label_2, 1, 0)  # 1行0列
        grid_layout.addWidget(self.Edit2, 1, 1)  # 1行1列
        grid_layout.addWidget(label_3,2,0) #二行0列
        grid_layout.addWidget(self.Edit3,2,1)#2行1列
        grid_layout.addWidget(submitButton,3,0,1,2)

        #容为Qt的AlignTop属性，表示顶部对齐
        grid_layout.setAlignment(Qt.AlignTop)

        # 创建一个窗口对象
        layout_widget = QWidget()
        # 设置窗口的布局层
        layout_widget.setLayout(grid_layout)

        self.setCentralWidget(layout_widget)

    def main_run(self):
        #获取文本框中的内容
        edit1 = self.Edit1.text()
        edit2 = self.Edit2.text()
        edit3 = self.Edit3.text()
        print(type(edit1),edit1)
        print(type(edit2),edit2)
        if edit1 == "15137359541" and edit2 =='123456':
            try:
                '''
                此时，序列号出错，直接弹出报错窗口
                '''
                trader = TradeDate(edit1,edit2,edit3)
                trader.run()
            except Exception as e:
                #捕捉错误
                if str(e).startswith('Expecting value'):
                    QMessageBox.information(self, 'Error', '模拟序列号查询无效')
                    return
                elif str(e).startswith('HTTPConnectionPool'):
                    QMessageBox.information(self, 'Error', '实盘易没有打开')
                    return
                elif str(e).startswith('通达信或者同花顺'):
                    QMessageBox.information(self, 'Error', '通达信或者同花顺没有打开！！！')
                    return
        else:

            QMessageBox.information(self, 'Error', '用户名或者密码错误')
            return

if __name__ =="__main__":
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())