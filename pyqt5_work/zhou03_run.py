from PyQt5 import QtCore,QtWidgets,QtGui
from pyqt5_work import zhou03
import sys
import pyqtgraph as pg
import datetime
import tushare as ts
from matplotlib.pylab import date2num



class MainWindow(object):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = zhou03.Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.update_date()
        self.update_calendar()
        self.set_lcd()
        self.set_dial()
        self.zero_process()
        self.update_process()
        self.click_radio3()
        self.set_font()
        self.ui.verticalLayout_3.addWidget(chart())
        MainWindow.show()
        sys.exit(app.exec_())

    # 修改日期修改器数值
    def update_date(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())

    # 日历信号槽
    def update_calendar(self):
        self.ui.calendarWidget.selectionChanged.connect(self.update_date)



    # 设置LCD数字
    def set_lcd(self):
        self.ui.lcdNumber.display(self.ui.dial.value())

    # 刻度盘信号槽
    def set_dial(self):
        self.ui.dial.valueChanged['int'].connect(self.set_lcd)
        print(self.ui.dial.value())

    #第二个按钮清零进度栏
    def zero_process(self):
        self.ui.radioButton_2.clicked.connect(self.ui.progressBar.reset)

    # 更新进度栏
    def update_process(self):
        value = self.ui.lcdNumber.value()
        self.ui.progressBar.setValue(value)

        # 点击按钮3

    def click_radio3(self):
        self.ui.radioButton_3.clicked.connect(self.update_process)

    def set_font(self):
        self.ui.fontComboBox.activated['QString'].connect(self.ui.label.setText)



class CandlestickItem(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        self.data = data  ## data must have fields: time, open, close, min, max
        self.generatePicture()

    def generatePicture(self):
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        w = (self.data[1][0] - self.data[0][0]) / 3.
        for (t, open, close, min, max) in self.data:
            p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
            if open > close:
                p.setBrush(pg.mkBrush('g'))
            else:
                p.setBrush(pg.mkBrush('r'))
            p.drawRect(QtCore.QRectF(t - w, open, w * 2, close - open))
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())


def chart():
    hist_data = ts.get_hist_data('600519',start='2017-05-01',end='2017-11-24')
    data_list = []
    for dates,row in hist_data.iterrows():
        # 将时间转换为数字
        date_time = datetime.datetime.strptime(dates,'%Y-%m-%d')
        print(date_time)
        t = date2num(date_time)
        print(t)
        # t = dict(enumerate(datetime))
        open,high,close,low = row[:4]
        datas = (t,open,close,low,high)
        data_list.append(datas)
    # axis_dict = dict(enumerate(axis))
    item = CandlestickItem(data_list)
    plt = pg.PlotWidget()
    plt.addItem(item)
    plt.showGrid(x=True,y=True)



    return plt
if __name__ == "__main__":
    MainWindow()