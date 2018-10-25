# _*_ coding:utf-8 _*_
import urllib,urllib2

url = 'http://www.baidu.com/s'
headers = {'UserAgent':'Mozilla'}
keyword = raw_input('请输入关键字:')
wd = urllib.urlencode({'wd':keyword})
fullurl = url + '?' + wd
print fullurl
request = urllib2.Request(fullurl,headers=headers)
response = urllib2.urlopen(request)
print response.read()