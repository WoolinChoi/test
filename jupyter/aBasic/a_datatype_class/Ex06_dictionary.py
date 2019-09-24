"""
    [ dictionary 형 ]

    1- 키와 값으로 구성 ( 자바의 map 와 유사 )
    2- 저장된 자료의 순서는 의미 없음
    3- 중괄호 {} 사용
    4- 변경가능

    ` 사전.keys() : key만 추출 (임의의 순서)
    ` 사전.values() : value만 추출 (임의의 순서)
    ` 사전.items() : key와 value를 튜플로 추출 (임의의 순서)
"""

print('--------- 1. 딕셔너리 요소 --------------- ')
dt = {1:"one", 2:"two", "3":"three", 1:"again"}
print(dt)
print(dt[1])        # 1이라는 키값 추출(마지막 1)
# print(dt[3])      # 키값 에러
print(dt["3"])

# 키는 숫자와 문자 그리고 튜플이여야 한다. 즉 리스트는 안된다.
# 리스트의 값이 변경 가능하다. 그러나 키값을 변경하면 안되므로 리스트는 안된다
dt2 = {1:"one", 2:"two", (3, 4):"turple"}
print(dt2[3,4])     # 키모양을 그대로 찾아야한다.

print('--------- 2. 딕셔너리 추가 및 수정  --------------- ')
dt2["korea"] = "seoul"      # 없으면 키가 새로 추가
print(dt2)
dt2["korea"] = "incheon"    # 있으면 키 값이 수정
print(dt2)

# 여러개를 추가(update() 이용)
dt2.update([["a", 10], ["b", 20]])
print(dt2)
dt2.update(zip([5, 6], ["a", "b"]))
print(dt2)
dt2.update({7:"c", 8:"d"})
print(dt2)

print('--------- 3. Key로 Value값 찾기  --------------- ')
# print(dt2[3])             # 존재하지않ㄴ는 3 키값으로 추출 -> 에러발생
print(dt2.get(3))           # None
print(dt2.get(1, "없음"))    # 키값 1있으면 1값, 키값 1없으면 없음 출력

# Key와 Value만 따로 검색
print(dt2.keys())
print(dt2.values())
print(dt2.items())
