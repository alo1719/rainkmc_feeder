from bs4 import BeautifulSoup
import requests
import webbrowser
import time
import codecs

data = {
    'fastloginfield': 'username',
    'username': '[[your user name]]',
    'cookietime': '2592000',
    'password': '[[your password]]',
    'quickforward': 'yes',
    'handlekey': 'ls'}
r = requests.post('https://rainkmc.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1', data=data)

r = requests.get('https://rainkmc.com/forum.php?mod=forumdisplay&fid=42', cookies=r.cookies)
f = codecs.open('rainkmc.html', 'w', 'gbk')
f.write(r.text)
f.close()

time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
with open("rainkmc_log.txt", "a+") as f:
    f.write(time_str + "\n")
