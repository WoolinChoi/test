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
    "m_id": "woolin06",
    "m_passwd": "qlalfqjsgh1!"
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