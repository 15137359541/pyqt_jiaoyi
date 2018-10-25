"""
https://cloud.tencent.com/info/187f16228b5d18273ff093e57b352bb2.html
"""
import pyqtgraph as pg
import tushare as ts
import numpy as np

data = ts.get_hist_data('sh',start='2017-10-01',end='2017-12-01').sort_index()
# print(data)
xdict = dict(enumerate(data.index))

axis_1 = [(i,list(data.index)[i]) for i in range(0,len(data.index),5)]
# print(axis_1)

# print(xdict)

app = pg.QtGui.QApplication([])
win = pg.GraphicsWindow(title='州的先生zmister.com pyqtgraph数据可视化 - 绘制精美折线图')

stringaxis = pg.AxisItem(orientation='bottom')
stringaxis.setTicks([axis_1,xdict.items()])

plot = win.addPlot(axisItems={'bottom': stringaxis},title='上证指数 - zmister.com绘制')

label = pg.TextItem()
plot.addItem(label)

plot.addLegend(size=(150,80))

plot.showGrid(x=True, y=True, alpha=0.5)

print(data['open'])
plot.plot(x=list(xdict.keys()), y=data['open'].values, pen='r', name='开盘指数',symbolBrush=(255,0,0),)
plot.plot(x=list(xdict.keys()), y=data['close'].values, pen='g', name='收盘指数',symbolBrush=(0,255,0))

plot.setLabel(axis='left',text='指数')
plot.setLabel(axis='bottom',text='日期')

vLine = pg.InfiniteLine(angle=90, movable=False,)
hLine = pg.InfiniteLine(angle=0, movable=False,)
plot.addItem(vLine, ignoreBounds=True)
plot.addItem(hLine, ignoreBounds=True)
vb = plot.vb
def mouseMoved(evt):
    print('evt is:',evt)
    pos = evt[0]  ## using signal proxy turns original arguments into a tuple
    if plot.sceneBoundingRect().contains(pos):
        mousePoint = vb.mapSceneToView(pos)
        index = int(mousePoint.x())
        pos_y = int(mousePoint.y())
        print('index is:',index)
        if 0 < index < len(data.index):
            print(xdict[index],data['open'][index],data['close'][index])
            label.setHtml("<p style='color:white'>日期：{0}</p><p style='color:white'>开盘：{1}</p><p style='color:white'>收盘：{2}</p>".format(xdict[index],data['open'][index],data['close'][index]))
            label.setPos(mousePoint.x(),mousePoint.y())
        vLine.setPos(mousePoint.x())
        hLine.setPos(mousePoint.y())
proxy = pg.SignalProxy(plot.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)

app.exec_()
