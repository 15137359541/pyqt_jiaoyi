import time

raw_transactions = [{u'status': u'\u5168\u90e8\u6210\u4ea4', u'trueLimitPrice': 0, u'transaction': u'\u5356', u'gains': -18564, u'matchTime': u'2018-10-18 09:30:00', u'trueOrderAmount': u"<span class='sell'>-10200\u80a1</span>", u'price': 7.99, u'orderAmount': u"<span class='sell'>-10200\u80a1</span>", u'trueAmount': u"<span class='sell'>-10200\u80a1</span>", u'limitPrice': u'-', u'commission': 105.95, u'amount': u"<span class='sell'>-10200\u80a1</span>", u'truePrice': 7.99, u'transactionPersent': u'100%', u'time': u'09:30', u'date': u'2018-10-18', u'security': u'\u80a1\u7968', u'total': u'(81498)', u'type': u'\u5e02\u4ef7\u5355', u'stock': u'\u53f0\u6d77\u6838\u7535(002366.XSHE)'}, {u'status': u'\u5168\u90e8\u6210\u4ea4', u'trueLimitPrice': 0, u'transaction': u'\u4e70', u'gains': 0, u'matchTime': u'2018-10-18 09:30:00', u'trueOrderAmount': u"<span class='buy'>12000\u80a1</span>", u'price': 6.74, u'orderAmount': u"<span class='buy'>12000\u80a1</span>", u'trueAmount': u"<span class='buy'>12000\u80a1</span>", u'limitPrice': u'-', u'commission': 24.26, u'amount': u"<span class='buy'>12000\u80a1</span>", u'truePrice': 6.74, u'transactionPersent': u'100%', u'time': u'09:30', u'date': u'2018-10-18', u'security': u'\u80a1\u7968', u'total': 80880, u'type': u'\u5e02\u4ef7\u5355', u'stock': u'\u660a\u534e\u80fd\u6e90(601101.XSHG)'}]
from shipane_sdk.joinquant.transaction import JoinQuantTransaction
transactions = []
def dt():
    transactions = []
    for raw_transaction in raw_transactions:
        transaction = JoinQuantTransaction(raw_transaction).normalize()
        transactions.append(transaction)

    return transactions
# cons = dt()
# print(cons[0],cons[1])
# for item in cons:
#     print('-'*20)
#     print(item.action,item.completed_at,item.symbol,item.price,item.amount)


num = 1
dict1=[]
while num<=5:
    print('*****************',num)
    time.sleep(2)
    cons = dt()
    for i in range(len(cons)):
        dict2={}

        dict2['action']=cons[i].action
        dict2['completed_at']=cons[i].completed_at
        dict2['symbol']=cons[i].symbol
        dict2['price']= cons[i].price
        dict2['amount']=cons[i].amount
        if dict2 not in dict1:
            dict1.append(dict2)

        else:
            pass

    num +=1
print(dict1)

