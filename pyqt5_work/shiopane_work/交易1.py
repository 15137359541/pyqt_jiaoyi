# -*- coding: utf-8 -*-
import requests

_session = requests.session()
# response = _session.get('http://localhost:8888/positions?client=title:monijiaoy&key=maxiaohui')
# print(response.content)
#
# data = {"action":"SELL","symbol":"000001","type":"LIMIT","priceType":0,"price":10.12,"amount":400}

'''
data数据中，数据是以字典形式的字符串
'''
seller = requests.post(url='http://localhost:8888/orders?client=title:monijiaoy&key=maxiaohui', data='''{
  "action": "SELL",
  "symbol" : "000001",
  "type": "LIMIT",
  "priceType" : 0,
  "price" : 10.12,
  "amount" : 400
}''')
print(seller.content)