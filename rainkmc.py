from bs4 import BeautifulSoup
import requests
import webbrowser

data = {
    'fastloginfield': 'username',
    'username': '[[your user name]]',
    'cookietime': '2592000',
    'password': '[[your password]]',
    'quickforward': 'yes',
    'handlekey': 'ls'}
r = requests.post('https://rainkmc.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1', data=data)

r = requests.get('https://rainkmc.com/forum.php?mod=forumdisplay&fid=42', cookies=r.cookies)
with open("rainkmc.html", 'w') as f:
    f.write(r.text)
