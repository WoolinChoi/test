"""
    [ 리스트 ]
      1- 임의의 객체를 순차적으로 저장하는 집합 자료형
      2- 각 값에 대해 인덱스 부여
      3- 변경가능 (**)
      4- 대괄호 [ ] 사용

      [참고]
      배열은 연속적으로 공간을 저장하는 것이니깐 파이션은 없다
      파이션에서는 리스트를 사용한다
      배열은 생성시 크기를 지정하지만 리스트트 크기 제한이 없다
"""

# --------------------------------------------------------------------
# (1) 리스트 인덱스
#   arr[i] : i번째 요소 추출
#   arr.append("가") : 가 요소를 리스트에 추가

'''
arr = []                # 비워져 있는 리스트 생성
arr = [1, 2, 3, 4, 5]
arr.append(10)
print(arr)
arr.append("hello")
print(arr)
print(arr[0])
print(arr[5])
print(arr[6].upper())
print(arr[6][0])
'''

""" [출력결과]
    [1, 2, 3, 4, 5, 10]
    [1, 2, 3, 4, 5, 10, 'hello']
    1
    10
    HELLO
    h
"""

'''
# 이중 리스트 만들고 인덱싱하기
arr.append([])
print(arr)

# 빈 리스트에 'korea'를 추가
arr[-1].append("korea")
print(arr)

# 'korea'안에 'a'를 추출
print(arr[-1][0][-1])
'''

""" [ 연습 ] 아래에서
    a = ['인천','부산',['전라','경상',['판교','부천']]]
    (1) '경상' 요소 추출
    (2) '부천' 요소 추출
    (3) '판'이라는 글자만 추출
"""

'''
a = ["인천", "부산", ["전라", "경상", ["판교", "부천"]]]
print(a[-1][1])
print(a[-1][-1][-1])
print(a[-1][-1][0][0])
'''

""" [ 연습 ] 아래에서
    a = ['인천','부산',['전라','경상'],['대전','광주','대구'], '서울','제주']
    (1) '부산'부터 '대구'까지 추출
    (2) '대전'부터 '제주'까지 추출
    (3) '인천'부터 '서울'까지 추출
    (4) '광주'부터 '대구'까지 추출
"""

'''
a = ["인천", "부산", ["전라", "경상"], ["대전", "광주", "대구"], "서울", "제주"]
print(a[1:4])
print(a[3:])
print(a[:5])
print(a[3][1:])
'''

# --------------------------------------------------------------------
# (2) 리스트 연산자

'''
a = ["독", "도", "는"]
b = ["대한민국", "섬"]
print(a + b)
print(a * 3)
'''

# --------------------------------------------------------------------
# (3) 리스트 관련 함수들
#           append()    : 요소 추가
#           sort()      : 리스트 정렬
#           reverse()   : 역순으로 뒤집기
#           index()     : 위치 반환
#           insert()    : 리스트에 요소 삽입
#           remove()    : 요소 제거
#           pop()       : 맨 마지막 요소를 꺼내기
#           count()     : 요소 개수 세기
#           extend()    : 리스트에 리스트를 더하기\
#           clear()     : 모든 요소를 제거

"""
    (1) 리스트 a에 0 요소 추가
    (2) 리스트 a에 9를 추가하여 출력 (a요소에는 추가하는 것은 아님)
    (3) 0번째 요소로 1을 추가
    (4) 3번째 요소로 1을 추가
    (5) 리스트 맨 마지막 요소를 꺼낸다
    (6) 요소 1을 삭제 ( 1이 여러개인 경우 맨 앞에 하나만 삭제됨 )
    (7) 리스트 모든 요소를 삭제
"""

'''
a = [7, 2, 3, 5, 6] 
a.append(0)
print(a)
print(a+[9])
a.insert(0, 1)
print(a)
a.insert(3, 1)
print(a)
pop_a = a.pop()
print(pop_a)
a.remove(1)
print(a)
a.clear()
print(a)
'''

# [참고] 리스트에 리스트 구조에서 clear() 하는 경우
'''
a1 = [1]
b1 = [7, 6, 5, 4, 3, a1]
print(a1)
print(b1)
b1.clear()  # 종속관계로 되어 있기에 b1의 내용만 삭제되고 a1은 유지된다
print(b1)
print(a1)
'''

"""
    (8) 리스트 a의 모든 요소를 역순으로 뒤집기
    (9) 리스트 a 정렬하기
    (10) 리스트 a에 리스트 b를 더하기
    (11) 리스트 a에서 0번째부터 1번째 요소까지 삭제
"""

'''
a = [3, 5, 4, 8, 0]
b = [1, 2]
a.reverse()
print(a)
a.sort()
print(a)
print(a + b)
del a[:2]
print(a)
'''

# --------------------------------------------------------------
#  (4) 리스트 요소 변경
#       - 2번째 요소를 'z'로 변경
#       - 0번째부터 1번째 요소를 'k'와 'o'로 변경

'''
a = [3, 5, 4, 8, 0]
a[2] = "z"
print(a)
a[0:2] = ["k", "o"]
print(a)
'''

# --------------------------------------------------------------
# (5) 리스트 복사
'''
a = [3, 5, 4, 8, 0]
b = a                   # a의 주소값만 복사(얕은 복사)
print(a is b)
b[0] = "A"
print(a)
print(b)

print("-" * 50)

a = [3, 5, 4, 8, 0]
b = a[:]                # a의 모든 요소를 복사(깊은 복사)
print(a is b)
b[0] = "A"
print(a)
print(b)

print("-" * 50)

from copy import copy
b = copy(a)             # 깊은 복사
print(a is b)
b[0] = "가"
print(a)
print(b)
'''

# 연습
a = [0, 1, 2, 3, 4]
print(a[:3], a[-3])     # [0, 1, 2] 2

# 연습2
print(a[::-1])      # [4, 3, 2, 1, 0]

# 연습3
first = ["egg", "salad", "bread", "soup", "canafe"]
second = ["fish", "lamb", "pork", "beef", "chicken"]
third = ["apple", "banana", "orange", "grape", "mango"]
order = [first, second, third]
john = [order[0][:-2], second[1::3], third[0]]
print(john)                                     # [['egg', 'salad', 'bread'], ['lamb', 'chicken'], ['apple']]
del john[2]
print(john)                                     # [['egg', 'salad', 'bread'], ['lamb', 'chicken']]
john.extend([order[2][0:1]])
print(john)                                     # [['egg', 'salad', 'bread'], ['lamb', 'chicken'], ['apple']]

# 연습4
list_a = [3, 2, 1, 4]
list_b = list_a.sort()
print(list_a, list_b)   # [1, 2, 3, 4] None

# 연습5
fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry', 'melon']
print(fruits[-3:], fruits[1::3])    # [['orange', 'strawberry', 'melon'], ['banana', 'orange']]

# 연습6
num = [1, 2, 3, 4]
print(num * 2)  # [1, 2, 3, 4, 1, 2, 3, 4]

# 연습7
a = [1, 2, 3, 5]
b = ['a', 'b', 'c', 'd', 'e']
a.append('g')
b.append(6)
print('g' in b, len(b)) # False 6

# 연습8
list_a = ['Hankook', 'University', 'is', 'an', 'academic', 'institute', 'located', 'in', 'South Korea']
list_b=[ ]
for i in range(len(list_a)):
    if i % 2 != 1:
        list_b.append(list_a[i])
print(list_b)   # ['Hankook', 'is', 'academic', 'located', 'South Korea']

# 연습9
'''
admission_year = input("입학 연도를 입력하세요: ")
print(type(admission_year)) # <class 'str'>
'''

# 연습10
country = ["Korea", "Japan", "China"]
capital = ["Seoul", "Tokyo", "Beijing"]
index = [1, 2, 3]
country.append(capital)
country[3][1] = index[1:]
print(country)  # ['Korea', 'Japan', 'China', ['Seoul', [2, 3], 'Beijing']]

# 연습11
a = [5, 4, 3, 2, 1]
b = a
c = [5, 4, 3, 2, 1]
print(a is b)   # True
print(a is c)   # False

# 연습12
a = 1
b = 1
print(a is b)   # True
a = 300
b = 300
print(a is b)   # True

# 연습13
list_1 = [[1, 2], [3], [4, 5, 6]]
a, b, c = list_1
list_2 = a + b + c
print(list_2)   # [1, 2, 3, 4, 5, 6