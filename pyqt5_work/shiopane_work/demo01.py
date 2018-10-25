# -*- coding: utf-8 -*-
'''
实盘易超级简易版小白安装教程

1、安装python

2、安装实盘易，安装通达信客户端

3、运行通达信客户端登录自己的股票账户，然后，在实盘易图标上右键选择“以管理员身份运行”运行实盘易，可以在本地，也可以在服务器上运行。
（通达信和实盘易必须在同一机器上运行，该机器就是一个服务器或者可以理解成一个网站，我们需要用python程序作为客户端去访问这个“网站”，
以实现下单和交易的各种操作）

4、编写实盘python程序
实盘python程序由两部分构成：1、交易接口，2、策略逻辑
其中，策略逻辑部分需要各位程序化交易者们自己摸索，交易接口部分分享在下面的代码中
（本文件可以直接作为python脚本运行）

5、部署运行实盘程序，人工监控或守护程序监控
'''

import json,urllib2,urllib,time

#若想请求远程服务器上的实盘易，请将ip_dizhi改成服务器ip
ip_dizhi = "localhost"

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    page.close()
    return html

#交易函数（交易方向买1卖-1，股票代码，下单价格，下单数量）
def trade(direction,code,price,lots):
    try:
        url = "http://"+ ip_dizhi +":8888/orders"
        #判断带入的价格和量是否均不为零
        if price==0 or price=='0' or lots==0 or lots=='0' or code=='':
            return -1
        if direction>0:
            action = "BUY"
        else:
            action = "SELL"

        postdata = {
            "action": action,
            "symbol" : str(code),
            "type":"LIMIT",
            "priceType":0,
            "price" : price,
            "amount" : lots
        }
        postdata = json.dumps(postdata)
        request = urllib2.Request(url,postdata)
        request.add_header('Content-Type', 'application/json')
        response=urllib2.urlopen(request)
        response = response.read()
        print response
        return 1
    except:
        return -1


#更新balance账户资金字典
#更新position持仓字典（键名：持有的股票代码，键值：[持有总量，可用总量]），遍历position即可得到账户内所有股票的持有仓位信息
def get_position_balance():
    global position,balance
    try:
        url = "http://"+ ip_dizhi +":8888/positions"
        i = json.loads(getHtml(url))
        balance['current_balance'] = i['subAccounts'][u'人民币'][u'参考总资产']
        balance['enable_balance'] = i['subAccounts'][u'人民币'][u'可取']
        balance['fetch_balance'] = i['subAccounts'][u'人民币'][u'可用']
        b = i['dataTable']['rows']
        for i in b:
            position[i[0]] = [int(float(i[2])),int(float(i[3]))]
        return 1
    except:
        return -1


#撤掉所有挂单
def chesuoyoudan():
    try:
        url = "http://"+ ip_dizhi +":8888/orders"
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(url)
        request.get_method = lambda:'DELETE'
        request = opener.open(request)
        return 1
    except:
        return -1

#所有函数正确请求即返回1，期间发生任何错误即返回-1
#以下为测试代码，实盘程序使用请更换为策略代码

#初始化position，balance变量
position = {}
balance = {'current_balance':0,'enable_balance':0,'fetch_balance':0}

#更新并输出账户资金，持仓，没有持仓则输出{}
get_position_balance()
print balance
print position

#以99元的价格买入1手华宝添益货币ETF（需要您的账户里有1W元可用资金才能下单成功）
print trade(1,'511990',99,100)
#等待5秒
time.sleep(5)
#把刚才下的单撤了
chesuoyoudan()



