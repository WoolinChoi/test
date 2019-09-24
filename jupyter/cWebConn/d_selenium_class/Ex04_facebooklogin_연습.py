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
