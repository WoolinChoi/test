---
layout: post
title: beautifulSoup
category: webconn
tags: [python, webconn, beautifulSoup]
comments: false
---

# [beautifulSoup]()

## 참고
~~~
웹서버에 접속하고, 데이터를 요청하며 서버로부터 받는 데이터를 분석해서 정보를 제공할 수 있도록
파이썬의 표준 라이브러리를 사용해도 되지만
유용한 외부 라이브러리가 있다.

* requests : 웹요청을 보내고 받는 기능
* beautifulsoup4 : 서버로부터 받은 데이터를 분석하는데 사용
            - 스크래이핑 할 수 있는 라이브러리
            - 다운로드 기능은 없음 ( 다운로드는 urllib를 이용함 )
            - 추가 설치 필요

(1) 외부 라이브러리 설치
    * pip : PyPI(Python Package Index : 파이썬 패키지 인덱스)를 관리하는 시스템
    ( pip 명령어 인식 : C:\ProgramData\Anaconda3\Scripts 환경변수 PATH에 지정되어 있어야 함 )

    > pip install requests  (* 주의 : s 붙음 )
    > pip install beautifulsoup4

(2) 파이참에서 설치
    프로젝트 선택 후 메뉴 > File > Settings
    왼쪽 Project > Project Interpreter 오른쪽 + 버튼
    검색창에서 requests를 찾아서 install package
    request에 s가 붙어야 한다.

    bs4도 추가하려면 BeautifulBS4를 찾아서 패키지 인스톨 해야 한다.
~~~

## element
~~~python
"""
    bs4 라이브러리 : 웹에서 가져온 HTML코드를 파이썬에서 사용하기 편하게 해주는 라이브러리
            [참고] 웹에서 가져온 HTML코드 가져오는 방법
                - requests 모듈
                - urllib 의 request 모듈

    BeautifulSoup 모듈
        - find()
        - find_all()
    
    [참고] 파서의 종류 
        - lxml : c로 만들어져 속도 빠름
        - html5lib : 파이썬으로 만들어서 lxml보다 느림
        - html.parser (*): 파이썬 버전을 확인해서 사용
"""

from bs4 import BeautifulSoup

html = """
    <html><body>
        <h1>스크레이핑 연습</h1>
        <p>웹페이지 분석하자</p>
        <p>데이타 정제하기</p>
    </body></html>
"""

# 1. 데이터 파서하기
soup = BeautifulSoup(html, "html.parser")

# 2. 원하는 요소 접근하기
h1 = soup.html.body.h1
print(h1)
print(h1.text)    # 문자열만 출력하고 싶을땐 .text, .string을 이용하여 출력
print(h1.string)

# 3. p요소의 내용 추출하기
p = soup.find_all("p")
print(p)
for i in p:        # list형식은 for문을 이용하여 출력
    print(i.text)
~~~

## attribute
~~~python
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
~~~

## selector
~~~python
"""
    BeautifulSoup 모듈에서
    - HTML의 구조(=트리구조)에서 요소를 검색할 때 : find() / find_all()
    - CSS 선택자 검색할 때 : select() /  select_one()
"""

from bs4 import BeautifulSoup

html = """
    <html><body>
        <div id='course'>
            <h1>빅데이터 과정</h1>
        </div>
        <div id='subjects'> 
            <ul class='subs'>
                <li>머신러닝</li>
                <li>데이터 처리</li>
                <li>데이타 분석</li>
            </ul>
        </div>
    </body></html>
"""

soup = BeautifulSoup(html, "html.parser")

# id 값으로 검색
h1 = soup.select_one("#course > h1")
print(h1.text)

# class 값으로 검색 - 목록(li) 내용 출력
li = soup.select(".subs > li")
print(li)
for i in li:
    print(i.text)
~~~

## warandpeace
~~~python
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
~~~

## kma
~~~python
from bs4 import BeautifulSoup
from urllib import request as req
rssUrl = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
res = req.urlopen(rssUrl)
# print(res)

soup = BeautifulSoup(res, "html.parser")
# print(soup)

# 도시(city) / 시간대별 날씨(wf)
locations = soup.select('location')

for loc in locations:
    data = loc.select('data')
    for dt in data:
        print('도시명:', loc.city.text, '/', dt.tmef.text, dt.wf.text)
~~~

## kyobobook
~~~python
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
~~~

## hanbit
~~~python
"""
    일단 http://www.hanbit.co.kr 회원가입

    [예] 한빗출판네트워크 ( 단순 페이지 ) : 이 예문은 위키북스 출판사 교재 예문임
                                    <파이썬을 이용한 머신러닝, 딥러닝 실전개발 예문>
    로그인페이지 : http://www.hanbit.co.kr/member/login.html
    마이페이지 : http://www.hanbit.co.kr/myhanbit/membership.html

    1. 로그인 페이지에서 개발자모드에서 로그인 form 태그를 분석
        입력태그의 name='m_id' / name='m_passwd' 확인

    2. 로그인 후에 마이페이지에서 마일리지와 한빛이코인 부분
        마일리지 (.mileage_section1 > span ) / 한빛이코인 (.mileage_section2 > span )

    3. 로그인과정에 어떤 통신이 오가는지 분석
        Network > Preserve log 체크 > Doc 탭을 선택하고 다시 처음부터 로그인을 하면 서버와 통신을 오고간다
        이 때 Name 중 login_proc.php를 선택하고 Headers 부분을 확인한다
        
        Gereral : Request Mathod : POST
        Form Data : m_id와 m_passwd 값 확인
"""

import requests
from bs4 import BeautifulSoup

# 세션 시작하기(쿠키, 권한 등을 요청을 위해 사용하는 객체)
sess = requests.session()
login_info = {    # 값이 두개이상이라 딕셔너리
    "m_id": "아이디값",
    "m_passwd": "비밀번호값"
}
url_logic = "http://m.hanbit.co.kr//member/login_proc.php"
res = sess.post(url_logic, data=login_info)    # post방식으로 요청해서 응답받기
res.raise_for_status()    # 해당사이트의 오류발생시 예외를 발생

url_mypage = "http://m.hanbit.co.kr/myhanbit/myhanbit.html"
res = sess.get(url_mypage)    # get방식으로 요청해서 응답받기
res.raise_for_status()

# 결과값 파싱하여 원하는 데이터 추출하기
soup = BeautifulSoup(res.text, "html.parser")    # 넘어오는 hmtl을 text해줘야한다.
# print(soup)
span = soup.select_one(".mileage_section1 > dd > span")
print("마일리지:", span.text)
~~~

## seoul
~~~python
"""
http://www.seoul.go.kr > 청사안내 > 자치구
https://www.seoul.go.kr/seoul/autonomy.do

BeautifulSoup  : 파서를 이용해서 html 의 요소를 추출하게 해주는 모듈
        - 단점은 개행문자를 고려해야 한다
Tag : 태그
NavigableString : 원래는 tag 사이의 문자열

#  xpath를 사용하면 개행문자를 고려하지 않아도 된단다
#  https://developer.mozilla.org/ko/docs/XPath
"""

import requests
from bs4 import BeautifulSoup, NavigableString

# 웹 문서 가져오기
url = "https://www.seoul.go.kr/seoul/autonomy.do"
html = requests.get(url).text

# 구청이름 / 구청주소 / 구청전화번호 / 구청홈페이지
soup = BeautifulSoup(html, "html.parser")

tabcont = soup.select(".tabcont")
for tab in tabcont:
    li = tab.find_all("li")
    print(tab.strong.text, "/", li[0].text, "/", li[1].text, "/", li[2].a.text)
~~~