from bs4 import BeautifulSoup
from urllib import request as req
rssUrl = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
res = req.urlopen(rssUrl)
# print(res)

soup = BeautifulSoup(res, "html.parser")
# print(soup)

# 도시(city) / 시간대별 날씨(wf)
locations = soup.select('location')

for l in locations:
    data = l.select('data')
    for dt in data:
        print('도시명:', l.city.text, '|', dt.tmef.text, dt.wf.text)