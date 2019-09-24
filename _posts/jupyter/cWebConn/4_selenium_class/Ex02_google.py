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