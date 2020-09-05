#/usr/bin/python3
#encoding:utf-8
from bs4 import BeautifulSoup
from urllib import request
import requests
import bs4
chengshi=input("请输入您要查询城市的拼音写法（例如:昆明，输入:kunming）:\n")
url = "http://www.tianqi.com/{}".format(chengshi)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

page = request.Request(url, headers=headers)

page_info = request.urlopen(page).read().decode('utf-8') 

soup = BeautifulSoup(page_info, 'html.parser')
titles = soup.find_all('h1')  
for data in soup.find_all('ul','week'):
    datas=data('b')
for high in soup.find_all('div','zxt_shuju'):
    highs=high('span')
for low in soup.find_all('div','zxt_shuju'):
    lows=low('b')
    

for weather in soup.find_all('ul','txt txt2'):
    weathers=weather('li')
    

tplt = "{0:^10}\t{1:^10}\t{2:^10}\t{3:^10}"
print('您查询到的是',titles[0].string[0:2],"一周内的天气情况")
print(tplt.format("日期","天气","最高温度","最低温度",chr(12288)))
for i in range(7):
    d=datas[i].string
    w=weathers[i].string
    h=highs[i].string
    l=lows[i].string
    print(tplt.format(d,w,h,l,chr(12288)))
a=input("感谢使用，请按回车键退出...")
