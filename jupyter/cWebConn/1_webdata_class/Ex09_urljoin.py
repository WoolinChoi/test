"""
 urllib.parse.urljoin() : 상대경로를 절대경로로 변화하는 함수
"""

from urllib import parse
baseUrl = "http://www.example.com/html/a.html"

# url 부분 경로로를 바꾼다.
print(parse.urljoin(baseUrl, "b.html"))    # http://www.example.com/html/b.html
print(parse.urljoin(baseUrl, "/c.html"))    # http://www.example.com/c.html
print(parse.urljoin(baseUrl, "../sub/b.html"))    # http://www.example.com/sub/b.html
print(parse.urljoin(baseUrl, "/sub/e.html"))    # http://www.example.com/sub/e.html

# url 전체 경로를 바꾼다
print(parse.urljoin(baseUrl, "http://www.mysite.com/mypage.jsp"))    # http://www.mysite.com/mypage.jsp