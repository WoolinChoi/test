from bs4 import BeautifulSoup
import requests
req = requests.get('http://www.pythonscraping.com/pages/warandpeace.html')

## HTML 소스 가져오기
html = req.text

soup = BeautifulSoup(html, "html.parser")

# 녹색 글자만 추출하여 출력
span = soup.select(".green")
print(list(span))
for i in span:
    print(i.text)