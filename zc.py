# 最速度注册
#发送post请求，模拟浏览器的登录最云会员中心1
# 组件安装：
# pip install requests
# pip install beautifulsoup4
# pip install requests_html
#!/usr/bin/python
#coding=utf-8
import requests
import re
from bs4 import BeautifulSoup
import random
import string

# 注册变量
def ranstr(num):
    salt = ''.join(random.sample(string.ascii_letters + string.digits, num))
    return salt
salt = ranstr(8)
#salt = "i0PGS7TR"
em = "@gmail.com"

redata={
    'email':(salt+em),
    'name': (salt),
    'passwd':(salt),
    'repasswd':(salt),
    'code':'0'
}
# 注册变量
#访问注册页面
r0=requests.get('https://ufocloud.xyz/auth/login',headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}, )
cookies=r0.cookies.get_dict()

# 注册账号
r1=requests.post('https://ufocloud.xyz/auth/register',data=redata,headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'},cookies=cookies)
print(redata)

# 登录账号
r2=requests.post('https://ufocloud.xyz/auth/login',data={'email':(salt+em),'passwd':(salt)},headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'},cookies=cookies)
cookies2=r2.cookies.get_dict() # 获取登录页面返回的cokies信息

# 开通免费套餐
#r3=requests.post('https://ufocloud.xyz/user/buy',data={'shop':"33",'autorenew':"0",'disableothers':"1"},headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'},cookies=cookies2)
# 签到领取流量
r4=requests.post('https://ufocloud.xyz/user/checkin',headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'},cookies=cookies2)


# 访问会员中心
from requests_html import HTMLSession
session = HTMLSession()
url="https://ufocloud.xyz/user"
r4=session.get(url,cookies=cookies2)


r4.encoding = 'utf-8'
soup = BeautifulSoup(r4.text,'lxml')

soup1 = soup.select('a[class="btn btn-icon icon-left btn-primary btn-v2ray copy-text btn-lg btn-round"]')
for i in soup1:(i['data-clipboard-text'])
#print(i['data-clipboard-text']) # 获取链接
soup2 = (i['data-clipboard-text'])
print (soup2)

#将V2订阅链接写入301.php文件
php1="<?php "
php2=" ?>"
khr="("
khl=")"
header="header"
url301=soup2
message = "Location:"
neirong=php1+header+khr+  '"'+message+''+''+url301+'"'+khl+php2

# 打开一个文件将V2订阅链接写入i.php文件
fo = open("i.php", "w")
fo.write(neirong)
# 关闭打开的文件
fo.close()


# 打开一个文件将V2订阅链接写入i.html文件
br="<br"
br2=">"
fo = open("i.html", "w")
fo.write(soup2+br+br2+salt+em)
# 关闭打开的文件
fo.close()
