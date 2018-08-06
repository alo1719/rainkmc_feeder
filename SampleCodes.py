import re
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import webbrowser

# 通过标签爬取
# html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
# soup = BeautifulSoup(html, features='lxml')
# all_href = soup.find_all('a')
# for l in all_href:
#     print(l['href'])

# 通过CSS类爬取
# html = urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode('utf-8')
# soup = BeautifulSoup(html, features='lxml')
# month = soup.find_all('li', {"class": "month"})
# for m in month:
#     print(m.get_text())

# 通过正则表达式爬取图片
# html = urlopen("http://www.soomal.com/doc/index101000_0001_00.htm").read().decode('gbk')
# soup = BeautifulSoup(html, features='lxml')
# img_links = soup.find_all("img", {"src": re.compile('.*?\.jpg')})
# for link in img_links:
#     print(link['src'])

# 爬百度百科
# base_url = "https://baike.baidu.com"
# history = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]
# url = base_url + history[-1]
# html = urlopen(url).read().decode('utf-8')
# soup = BeautifulSoup(html, features='lxml')
# print(soup.find('h1').get_text(), '        url: ', history[-1])
# # find valid urls
# sub_urls = soup.find_all("a",
#                          {
#                              "target": "_blank",
#                              "href": re.compile("/item/(%.{2})+$")
#                          })
# for i in sub_urls:
#     print(i)
# if len(sub_urls) != 0:
#     history.append(random.sample(sub_urls, 1)[0]['href'])
# else:
#     history.pop()

# post登录
# param = {"wd": "雨中小町"}
# r = requests.get('http://www.baidu.com/s', params=param)
# print(r.url)
# 查看chrome中Network-PreserveLog-Headers-FormData
# 实现登录
data = {
    'fastloginfield': 'username',
    'username': '[[your username]]',
    'cookietime': '2592000',
    'password': '[[your password]]',
    'quickforward': 'yes',
    'handlekey': 'ls'}
r = requests.post('https://rainkmc.ml/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1', data=data)
print(r.text)

# 但是持续登录需要用到Cookies
print()
print(r.cookies.get_dict())
r = requests.get('https://rainkmc.ml/forum.php?mod=forumdisplay&fid=42', cookies=r.cookies)
print(r.text)
# 把爬取到的内容写入到html
with open("rainkmc.html", 'w') as f:
    f.write(r.text)