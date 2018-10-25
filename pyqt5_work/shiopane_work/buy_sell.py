# -*- coding: utf-8 -*-
import requests
import datetime
import json

#自定义异常
class MyException(Exception):
    def __init__(self,message):
        Exception.__init__(self)
        self.message = message
class shipanyiData():
    def __init__(self,json):
        self.__dict__.update(json)

    def BS(self):
        _session = requests.session()
        # response = _session.get('http://localhost:8888/positions?client=title:monijiaoy&key=maxiaohui')
        # print(response.content)
        #
        # data = {"action":"SELL","symbol":"000001","type":"LIMIT","priceType":0,"price":10.12,"amount":400}

        data ={
            "action": self.action,
            "symbol": self.symbol,
            "type": "LIMIT",
            "priceType": 0,
            "price": float(self.price),#必须是数字
            "amount": float(self.amount)
        }

        print(json.dumps(data))
        '''
        
        data数据中，数据是以json形式传入。
        '''
        seller = _session.post(url='http://localhost:8888/orders?client=title:monijiaoy&key=maxiaohui', data=json.dumps(data))
        print(seller)
        print(seller.text)
        if seller.text.startswith('未找到'):
            raise MyException('通达信或者同花顺没有打开！！！')
        else:
            return 'buy or sell success'
if __name__ == "__main__":
    spy = shipanyiData({'action': 'SELL', 'completed_at': datetime.datetime(2018, 10, 24, 9, 30), 'symbol': '000002', 'price': '22.46', 'amount': 100})

    res = spy.BS()
    print(res)

