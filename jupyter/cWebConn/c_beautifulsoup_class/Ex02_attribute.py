from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <ul>
                <li><a href='http://www.naver.com'>네이브</a></li>
                <li><a href='http://www.daum.net'>다아음</a></li>
            </ul>
        </body>
    </html>
"""

# 리스트의 내용과 해당 경로를 추출하기
# attrs["속성명"] : 해당속성값을 얻어주는 함수
''' [출력결과]
네이브 >>> http://www.naver.com
다아음 >>> http://www.daum.net
'''

soup = BeautifulSoup(html, "html.parser")

a = soup.find_all("a")
print(a)
for i in a:
    text = i.text
    href = i.attrs["href"]
    print(text, ">>>", href)
