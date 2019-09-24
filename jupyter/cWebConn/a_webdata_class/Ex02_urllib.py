# import urllib.request
from urllib import request as req

url = "http://www.google.com"
site = req.urlopen(url)
# print(site)
page = site.read()
print("page:", page)
print("status:", site.status)
headers = site.getheaders()
print("headers:", headers)
# 헤더정보의 이름과 값으로 출력
for name, values in headers:
    print("name:", name)
    print("values:", values)