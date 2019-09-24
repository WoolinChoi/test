import re

# findall(검색어, 문자열) : 문자열에서 검색어와 일하는 내용들을 리스트로 반환
msg = 'We_are_happy!! You are happy?? Happy2019-2020 안녕'

result = re.findall("happy", msg)    # search와 다르게 문자열을 모두 찾는다.
print("happy:", result)

# 소문자 모두 찾기
result = re.findall("[a-z]", msg)
print("모든 소문자:", result)

# 소문자가 아닌 모두 찾기
result = re.findall("[^a-z]", msg)
print("소문자가 아닌 모두:", result)

# 소문자(반복) 모두 찾기
result = re.findall("[a-z]+", msg)
print("소문자(반복) 모두:", result)

# 소문자와 대문자 찾기
result = re.findall("[a-zA-Z]+", msg)
print("소문자와 대문자:", result)

# 숫자 찾기
result = re.findall("[0-9]+", msg)
print("숫자:", result)

# 소문자/대문자/숫자 아닌 거찾기
result = re.findall("[^a-zA-Z0-9]+", msg)
print("소문자/대문자/숫자가 아닌:", result)

# 영문자 숫자 _를 검색
result = re.findall("[\w]+", msg)
print("영문자 숫자 _:", result)

# 영문자 숫자 _가 아닌 검색
result = re.findall("[\W]+", msg)
print("영문자 숫자 _가 아닌:", result)