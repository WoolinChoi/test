'''
 [과제] 교보문고에서 파이썬 책 검색하여
    - csv 파일로 저장
    - mysql 테이블에 저장
'''


from urllib.request import urlopen
from bs4 import BeautifulSoup

# 교보문고 > '파이썬' 검색 > 국내도서
html = urlopen("http://www.kyobobook.co.kr/search/SearchKorbookMain.jsp?vPstrCategory=KOR&vPstrKeyWord=python&vPplace=top")

# BeautifulSoup을 이용해서 책의 제목들, 총 책의 권수를 출력하기
soup = BeautifulSoup(html, "html.parser")

strong = soup.select("div .title > a > strong")
count = len(strong)
print("총 ", count, "권의 책을 조회하였습니다.")
for i, st in enumerate(strong):
    print(i + 1, ">>>", st.text)