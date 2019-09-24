"""
    # 패턴과 소스를 비교하는 메소드
    - match() : 패턴의 일치여부 확인
    - findall() : 일치하는 모든 문자열 리스트 반환
    - search() : 첫번째 일치하는 객체 반환
    - split() : 패턴에 맞게 소스를 분리한 후 문자열 조각의 리스트 반환
    - sub() : 대체 인자로 변환

    [참고] 파이썬 정규식 표현 : https://wikidocs.net/4308
"""
import re

# match()
msg = 'We are happy. You are happy. Happy2019 2020'

result = re.match("We", msg)
if result:
    print(result.group())
print("-" * 50)

result = re.match("happy", msg)
if result:
    print(result.group())
print("-" * 50)

result = re.match(".*happy", msg)    # 앞에 문자들이 있을때 .*찾는문자열 해준다.
if result:
    print(result.group())
print("-" * 50)

# search()
result = re.search("happy", msg)    # 문자열과 일치하는 것을 찾아준다.
if result:
    print(result.group())
print("-" * 50)

# split()
result = re.split("a", msg)
if result:
    print(result)    # 문자열 기준으로 잘라준다.
print("-" * 50)

# sub()
result = re.sub("a", "@", msg)
if result:
    print(result)    # 문자열을 @로 바꿔준다.
print("-" * 50)