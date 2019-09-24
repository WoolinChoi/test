---
layout: post
title: selenium
category: webconn
tags: [python, webconn, selenium]
comments: false
---

# [selenium]()

## 참고
~~~
1. selenium
    - 주로 웹앱을 테스트하는데 이용하는 프레임워크
    - 웹 브라우저를 원격으로 조작할 때 사용
    - 자동으로 URL을 열고 클릭, 스크롤, 문자 입력등의 동작을 조작할 수 있다.
    - webdriver라는 API를 통해 운영체제에 설치된 Chrome등의 브라우저를 제어하게 된다.

    [설치]  메뉴 > File > Settings > Project Interpreter > + 버튼
     selenium 검색 후 인스톨
        > pip install selenium

    [참고] Selenium의 버전은 자주 업데이트 되고, 브라우저의 업데이트 마다 새로운 Driver를 잡아주기 때문에
        항상 최신버전을 깔아 주는 것이 좋다.

    [매뉴얼]
    ` https://selenium-python.readthedocs.io/index.html
    ` https://docs.seleniumhq.org/docs/

2. 크롬 웹드라이버 ( Chrome WebDriver )
    [다운로드] http://chromedriver.chromium.org/downloads
        chromedirver_win32.zip 파일 다운로드 받고 압축풀기
        2019.07.24 - ChromeDriver 75.0.3770.140  ( 반드시 이 버전만 되었다 )

3. *** 셀레니움에서 지원안 할 예정
    화면없는 웹 브라우저 : PhantomJS
    - 화면없이 명령줄을 이용
    - 웹 개발시 테스트 및 성능 측정, 화면 캡쳐 등에 활용

    http://phantomjs.org
    http://phantomjs.org/download.html
    다운받아 압축푼 경로 / bin / phantomjs.exe 실행하면
    콘솔 화면> console.log('hello')  // 자바스크립트 명령어
~~~

## driver
~~~python
* Selenium은 driver객체를 통해 여러가지 메소드를 제공한다.
  - HTML을 브라우저에서 파싱해주기 때문에 굳이 Python와 BeautifulSoup을 사용하지 않아도 된다.


[ URL에 접근하는 api ]

get(‘http://url.com’)


1. DOM 내부에 있는 여러 요소 중 첫 번째 요소(element) 찾는다.

find_element_by_name(‘HTML_name’)
find_element_by_id(‘HTML_id’)
find_element_by_css_selector(‘#css > div.selector’)
find_element_by_class_name(‘some_class_name’)
find_element_by_tag_name(‘h1’)
find_element_by_xpath(‘/html/body/some/xpath’) : xpath 지정하여 해당 요소 추출
find_element_by_link_text(‘text’) : 링크 텍스트로 요소 추출

2. DOM에서 모든 요소 추출
find_elemens_by_css_selector(‘#css > div.selector’)
find_elements_by_class_name(‘some_class_name’)
find_elements_by_tag_name(‘h1’)

3. DOM 요소에 적용할 수 있는 메소드와 속성
clear()             : 글자를 지움
click()             : 클릭
get_attribute(name) : 요소의 속성 name에 해당하는 값을 추출
is_displayed()      : 요소가 화면에 출력되는지 확인
is_enabled()
is_selected()
save_screenshot(filename)
submit()

외에도 많은 속성과 메소드가 있습니다.

또한 각 브라우저 드라이버 객체의 속성도 있습니다.
~~~

## test
~~~python
"""
 간단하게 크롬 브라우저를 실행하여 페이지 열기
"""

from selenium import webdriver
# 1. webdriver 객체생성
driver = webdriver.Chrome("./webdriver/chromedriver.exe")

# 2. 페이지 접근
driver.get("http://www.naver.com")

# 3. 화면을 캡처해서 저장하기
driver.save_screenshot("WebSite.png")
~~~

## google
~~~python
'''
1. 크롬웹드라이버로 구글 사이트 열기

2. 실제 크롬창에서 '플레이데이터'라고 검색버튼을 누른다.
    개발자모드(F12)에서 이 부분을 보면
    <input name='q' value='플레이데이터'~~ >
    그리고 'google검색' 버튼이 type='submit' 인거 확인
'''

from selenium import webdriver
driver = webdriver.Chrome("./webdriver/chromedriver.exe")

driver.get("http://www.google.com")

# selenium이 입력을 해줌
bt = driver.find_element_by_name("q")
bt.send_keys("플레이데이터")
bt.submit()
~~~

## naver
~~~python
"""
네이버 로그인 페이지를 실행하기
    크롬에서 네이버 로그인 페이지를 개발자모드에서 확인하여
    로그인 폼의 아이디와 비밀번호 입력 name 확인
    아이디 : id
    비밀번호 : pw
"""

from selenium import webdriver

# 0. 네이버 로그인 정보
myID = '아이디값'
myPW = '비밀번호값'

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3)    # 암묵적으로 자원로드될 때까지 3초 기다림

# 네이버로그인 하기 -[결론] 네이버 보안에 걸림
# 보안에 안걸렸으면 로그인된 상태로 많은 정보를 가져올 수 있다
driver.get('https://nid.naver.com/nidlogin.login')
driver.find_element_by_name('id').send_keys(myID)
driver.find_element_by_name('pw').send_keys(myPW)
# 로그인 버튼을 눌러주자.
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()


""" 보안에 걸리지 않으면 Naver 페이 들어가기 - 어차피 안됨
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.p_inr > div.p_info > a > span')

for n in notices:
    print(n.text.strip())
"""
~~~

## facebook
~~~python
"""
    [연습] 페이스북에 접속해서 로그인 하기

        로그인 후에 보안창은 없는데 안 넘어가서

        from selenium.webdriver.common.keys import Keys

        아이디와 패스워드 지정후에
        elem.send_keys(Keys.RETURN)

"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 0. 페이스북 로그인 정보
myID = '아이디값'
myPW = '비밀번호값'

driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3)

driver.get('https://ko-kr.facebook.com/')
elem = driver.find_element_by_name('email')
elem.send_keys(myID)
elem = driver.find_element_by_name('pass')
elem.send_keys(myPW)
elem.send_keys(Keys.RETURN)
~~~

## Goobne
~~~python
"""
    [ 굽네치킨 매장 주소 가져오기 ]

    굽네치킨 http://www.goobne.co.kr > 매장찾기 > 매장찾기
                  http://www.goobne.co.kr/store/search_store.jsp

    개발자모드( F12 ) 열고 페이지 번호를 누르면
    <tbody> 부분이 교체되는 것을 볼 수 있다

    또한 2번 페이지 번호에 <a href="javascript:store.getList('2');">2</a>로 자바스트립트 함수를 호출한다.

    이 때 WebDriver 라는 특정 웹 브라우저의 원격 제어 인터페이스를 이용하고
    selenium 패키지를 이용하여  DOM  요소를 가져오거나 자바스크립트에서 제어하는 동작을 할 수 있도록 한다.
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time

#-------------------------------1. 웹 페이지 접근
# 웹드라이버 객체 생성
driver = webdriver.Chrome('./webdriver/chromedriver')
driver.implicitly_wait(3)

# 페이지 접근
driver.get('http://www.goobne.co.kr/store/search_store.jsp')

# 웹페이지에서 소스 가져오기
for page_idx in range(1, 11):
    driver.execute_script('store.getList("%s")' % str(page_idx))
    time.sleep(5)
    html = driver.page_source

    # 필요한 요소만 추출(파싱)
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    for store_list in soup.findAll('tbody', attrs={'id':'store_list'}):
        # 지점명 - 전화번호 - 주소 만 추출
        name = soup.select('tr > td:first-child')
        tel = soup.select('.store_phone > a')
        addr = soup.select('.t_left > a')
        for n, t, a in zip(name, tel, addr):
            print(n.text, '-', t.text, '-', a.text)
~~~