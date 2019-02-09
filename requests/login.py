import requests as r
data = {'login:name': 'spb4305', 'login:password': 'erozikifepu'}
url = 'http://neerc.ifmo.ru/pcms2client/login.xhtml'
s = r.Session()
resp = s.post(url, data=data)
print(s.cookies)
with open('page1.html', 'wb') as f:
    f.write(resp.content)
