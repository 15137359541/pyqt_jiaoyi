# _*_ coding:utf-8 _*_
from login_jukuan import JoinQuantClient
from trade_day import T_date
from buy_sell import shipanyiData
import datetime

class TradeDate(T_date):
    # 初始化第一次运行函数时的数据
    def __init__(self,username,password,backtest_id):
        self.username = username
        self.password = password
        self.backtest_id = backtest_id
        self._login_jukuan()
        self.startDate()
        self.login_flag = 1
    def _login_jukuan(self):
        # 策略推送3-模拟交易
        self.user = JoinQuantClient(username=self.username, password=self.password, backtest_id=self.backtest_id)

        #用户登陆
        '''
        账号或者密码错误时，会报错
        '''
        try:
            self.user.login()
        except:
            self.login_flag=0
            print('账号或者密码错误')
        #从模拟的策略中获取数据

            '''
            当查询的模拟序列号不存在时，会报错simplejson.errors.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
            '''
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
        print('self.balance is ',self.balance)



    def _main(self):
        print('_main in ,self.balance is ', self.balance)
        print(datetime.datetime.now())
        # 重写_main 方法，判断是否可以在规定的时间段
        flag = self.mnTime()
        if flag:
            #一分钟查询一次聚宽数据
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
                    print('new data is ',dict2)
                    res = shipanyiData(dict2).BS()
                    print(res)
                else:
                    print('no new data', dict2)

                
        else:
            pass
        print('final self.balance is ',self.balance)
        
if __name__ =='__main__':
    username = 15137359541
    password = 123456
    backtest_id ='3dd550cf83842b505f5b3e22e081d4c6'
    trader = TradeDate(username,password,backtest_id)
    trader.run()
