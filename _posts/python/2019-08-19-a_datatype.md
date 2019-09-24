---
layout: post
title: datatype
category: python
tags: [python]
comments: false
---

# [datatype]()

## 학습
~~~
[파이썬은  파이썬이다]

[파이썬 특징]
1. 간단하고 배우기 쉬운 언어(읽기 쉬운 언어)
2. 인터프리터 언어(컴파일 언어가 아님)
3. 강력한 라이브러리 제공
4. 범용적인 언어(R에 비해서, R은 통계에 특화된 언어)

[파이썬 단점]
1. 하드웨어 제어같은 복잡한 프로그램 부절적
2. 반복 연산이 많은 프로그램 부절적 -> jPython, cPython으로 극복
3. GIL(Global Interpreter Lock) : 쓰레드로부터 안전하지 않은 코드를 다른 쓰레드와 공유할 때 충돌을 방지하기 위해
배타적 잠금을 하는데 이것을 GIL 한다. 즉, 멀티 쓰레드 실행 시 스레드 스케줄링할 때  GIL 적용되어 병렬처리가 안됨

유명한 개발자 마틴 파울러의 명언
    "컴퓨터가 이해할 수 있는 코드는 어느 바보나 다 짤 수 있다.
    좋은 프로그래머는 사람이 이해할 수 있는 코드를 짠다"

# 파이썬 기본 규칙
    - 들여쓰기는 4 스페이스(탭)
    - 한 줄은 최대 80자 이내로
    - 불필요한 공백은 피함

# PEP8 규칙(가능하면 지키는 코딩 방식)
    - = 연산자는 1칸 이상 띄우지 않는다
            a = 12  ->  a=12
    - 변수명에 소문자 l(엘), 대문자 O(오), 대문자 I(아이)는 금한다
            lIOO = 100  (엘아이오오)
    - 주석은 항상 갱신하고, 불필요한 주석을 지운다
    - 함수명은 소문자로 구성하고 필요하면 밑줄로 나눈다

# 파이썬은 파이써닉하게 코딩하자!
~~~

## valuable
~~~python
"""
    파이션  - 무료이지만 강력하다
        ` 만들고자 하는 대부분의 프로그램 가능
        ` 물론, 하드웨어 제어같은 복잡하고 반복 연산이 많은 프로그램은 부적절
        ` 그러나, 다른언어 프로그램을 파이썬에 포함 가능 
        
    [주의] 줄을 맞추지 않으면 실행 안됨

    [실행] Run 메뉴를 클릭하거나 단축키로 shift + alt + F10

    [도움말] ctrl + q

"""

""" 여러줄 주석 """
# 한줄 주석

# print("헬로우")
# print('hello')
# print("""안녕""")
# print('''올라''')

# 실행 : ctrl + shift + F10
# 작은 따옴표 '' 와 큰 따옴표 "" 를 구분하지 않는다.

"""
변수란
    파이션의 모든 자료형은 객체로 취급한다
    a = 7
            7을 가리키는 변수 a이다. ( 저장한다는 표현 안함 )
            변수 a는 7이라는 정수형 객체를 가리키는 레퍼런스이다.
            여기서 7은 기존 프로그램언어에 말하는 상수가 아닌 하나의 객체이다.
    
    [변수명 규칙]
    - 영문자 + 숫자 + _ 조합
    - 첫글자에 숫자는 안됨
    - 대소문자 구별
    - 길이 제한 없음
    - 예약어 사용 안됨       
"""

# 예약어 확인
import keyword
print(keyword.kwlist)


"""
a = 7   # 7 객체를 가르키는 변수 a
b = 7   # 7 객체를 가르키는 변수 b
print(type(a))  # int
print(a is 7)   # true
print(b is 7)   # true
print(a is b)   # true

print(id(a))    
print(id(b))
print(id(7))
# id 값이 동일하다 즉, a와 b와 7의 객체를 가르키는 변수명만 다르다
"""

# 여러 변수 선언
a, b = 5, 10
print('a+b=', a+b)

# 파이썬에서 두 변수의 값 바꾸기(swapping)
a, b = b, a
print('a=', a, 'b=', b)

# 변수의 삭제
del b
print(b)
~~~

## number
~~~python
"""
        숫자형 종류
            - 정수형
            - 실수형
            - 복소수형 1 + 2j, 3i  ( 많이 사용안함 )
            - 8진수   0o25
            - 16진수  0x25
"""

# 파이션의 모든 자료형은 객체로 취급한다
# 실행 : ctrl + shift + F10

""" [ 기초 연산자 ]
        + : 더하기
        - : 빼기
        * : 곱하기
        / : 나누기(실수값 결과)
        // : 나누기(정수값 결과)
        % : 나머지
        ** : 자승
    
    2. 관계연산자
        <   >   <=  >=  ==  !=
    
    3. 논리연산자
        not     or      and
        
    4. 이진(비트) 연산자
        ~   :  이진 not   
        |   :  이진 or
        &   :  이진 and
        ^   :  이진 xor
        <<  :  shift
        >>  :  shift
        
    5. 대입연산자
        =
        +=  -=  *=  /=  //= %=
        &=  |=  ^=
        >>= <<=
    
    6. 기타연산자 : 딕셔너리, 문자열, 리스트, 튜플 등의 자료형에서 사용
        is      : 비교하는 객체의 주소가 같으면 true, 다르면 false
        is not  : 비교하는 객체의 주소가 다르면 true, 같으면 false 
        in      : 요소에 포함되면 true, 없으면 false
        not in  : 요소에 포함되지 않으면 false, 없으면 true
    
    [참고] 증가/감소 연산자 없음(++ / --) 
"""

a = 5
b = 2
# print('a++=", a++)    # Error
print('a/b=', a/b)
print('a//b=' + a//2)   # 문자열 + 숫자는 문자열변경이 되지 않고 에러
print('a//b=' + str(a//2))
print('a//b=', a//2)
print('a%b=', a%b)
print('a**b=', a**b)

""" [ 출력결과 ] 
        a / b = 2.5
        a // b = 2
        a % b = 1
        a ** b = 25
"""

# 출력 포맷
y = 8.3/2.7
print(y)
print('실수: {0}, 정수: {1}'.format(y, 100))
print('실수: {}, 정수: {}'.format(y, 200))
print('실수: {1}, 정수: {0:.1f}'.format(y, 300))

# 기타연산자
print('Hello' is 'hello')   # False
print('Hello' is not 'Hello')   # False
print('H' in 'Hello')   # True
print('H' not in 'Hello')   # False

# 연습
a = 777
b = 777
print(a == b, a is b)   # True, False

# 연습2
a = 3.5
b = int(3.5)
print(a ** ((a // b) * 2))  # 12.25
print(((a - b) * a) // b)   # 0.0
b = (((a - b) * a) % b)
print(b)                    # 1.75
print((a * 4) % (b * 4))    # 0.0

# 연습3
celsius = float(input("섭씨온도를 입력하세요:"))
fahrenheit = ((9 / 5) * celsius) + 32
print("섭씨온도:", celsius, "화씨온도:", fahrenheit)

# 연습4
a = "True"
print(type(a))  # str

# 연습5
a = 10.6
b = 10.5
print(a * b)
print(type(a + b))  # float

# 연습6
a = "3.5"
b = 4
print(a * b)    # 3.53.53.53.5, 문자열 * 4는 문자열을 4번 출력한다

# 연습7
a = "3.5"
b = "1.5"
print(a + b)    # 3.51.5, 문자열 + 문자열은 붙어서 출력한다

# 연습 8
a = "3" # str
b = float(a)    # float로 형변환
print(b ** int(a))  # 27.0, 형변환해주면 계산가능하다

# 연습9
a = "20"
b = "4"
print(type(float(a / b)))   # TypeError

# 연습10
a = "Gachon"
b = "CS"
c = 200
c = str(c - 150)
print(a, b, c)  # Gachon CS 50
~~~

## string
~~~python
# (0) 문자열을 "" 이나 '' 으로 표현

# -----------------------------------------
# (1) 개행을 포함한 문자열

msg = """
    안녕하세요.
    저는 성이 파이이고,
    이름은 썬입니다.
    잘 부탁합니다.
"""
print(msg)

msg = """
    행복합시다
    즐깁시다
    오늘도
"""
print(msg)

# -----------------------------------------
#  (2) 문자열 연산
#       문자열 합치기 : 문자열 + 문자열
#       문자열 반복 : 문자열 * 숫자

a = "독도는 "
b = "한국이다. "
print("-" * 50)
print(a + b)
print((a + b) * 3)
print("=" * 50)

""" [ 출력결과 ] 
        --------------------------------------------------
        독도는 한국이다. 
        독도는 한국이다. 독도는 한국이다. 독도는 한국이다. 
        ==================================================
"""

# 문자열 + 숫자
# c = a + 100   # Error
c = a + str(100)
print(c)    # 예상은 "독도는 100"

# -----------------------------------------
#  (3) 문자열의 인덱싱과 슬라이싱
#       - 인덱스는 0부터 시작한다
#       - s[i] : s 문자열에서 i번째 문자 추출
#       - s[i:j] : s 문자열에서 i번째에서 j번째 전까지의 문자 추출
#       - s[i:j:k] : s 문자열에서 i번째에서 j번째 전까지에서 k개씩 건너뛰어 문자 추출
#       - s[-i] : s 문자열에서 뒤에서부터 i번째 문자 추출
#                 ( 뒤에서 인덱스는 1부터 센다 )

msg = "오늘도 행복도 하다"
print(msg[0])
print(msg[0:2])
print(msg[1:6])
print(msg[0:6:2])
print(msg[-1])
print(msg[-0])      # 오
print(msg[:])       # 오늘도 행복도 하다
print(msg[5:-1])    # 복도 하

""" [ 출력결과 ]
        오
        오늘
        늘도 행복
        오도행
        다
"""

""" [ 참고 ] 
       ` msg[0] == msg[-0] 같은 값을 추출
       ` msg[:] 전체 추출
       ` msg[i:-j] i번째부터 뒤에서 j번째 전까지 추출
"""

""" [ 확인 ]
    1- 문자열 끝까지라면 두번째 숫자 생략 가능
    2- 처음부터 시작하는 것이라면 첫번째 숫자 생략 가능
"""

# 1) 5번째부터
print(msg[5:])

# 2) 5번째 전의 문자까지
print(msg[:5])

# 3) 5번째 전의 문자까지에서 2개씩 건너뛰어
print(msg[:5:2])

# 4) 문자열 전체에서 2개씩 건너뛰어
print(msg[::2])

""" [ 연습-1 ]
    날짜와 시간을 표현하는 문자열에서 '2020-02-22 : 12:05:12'
    '2020년 2월 22일' 출력
    '12시 5분' 출력
"""

date = "2020-02-22 : 12:05:12"
print(date[0:4], "년 ", date[6], "월 ", date[8:10], "일");
print(date[-8:-6], "시 ", date[-4], "분")

# -----------------------------------------
#  (4-1) 문자열 관련 함수
#       s.count('글') : s 문자열에서 '글'이라는 문자 개수 세기
#       s.index('글') : s 문자열에서 문자 '글' 위치 알려주기
#       s.find('글') : s 문자열에서 문자 '글' 위치 알려주기
#       s.rfind('글') : s 문자열에서 문자 '글' 오른쪽에서 왼쪽으로 찾아서 위치 알려주기
#       s.len() : s 문자열 길이

msg = '오늘도 행복도 하다'
print("행복위치:", msg.find("행복"))
print("가자:", msg.find("가자"))    # 없으면 -1
print("찾기:", msg.rfind("행복"));  # 오른쪽부터 찾아서 앞에서부터 센 인덱스를 반환
print("문자열길이:", len(msg))
print("도 갯수:", msg.count("도"));

""" [ 출력결과 ]
    1) '행복'이라는 글자 위치 찾기
    2) '가자'라는 글자 위치 찾기
    3) '행복'이라는 글자를 오른쪽에서 왼쪽으로 찾기
    4) 문자열 전체 길이 구하기
    5) '도'라는 단어의 갯수 구하기
"""

# -----------------------------------------
#  (4-2) 문자열 관련 함수
#   s.upper() : 소문자를 대문자로
#   s.lower() : 대문자를 소문자로
#   s.lstrip() : 왼쪽 공백 지우기
#   s.rstrip() : 오른쪽 공백 지우기
#   s.strip() : 양쪽 공백 지우기

msg = '  This is My Life  '
print(msg)
print(msg.strip())

# 문자열에서 모든 공백 제거하기
print(msg.replace(" ", ""))

# -----------------------------------------
#  (4-3) 문자열 관련 함수
#   s.replace("a","b")  :  s 문자열에서 단어 a를 단어 b로 바꾸기
#   s.split() : s 문자열을 공백으로 나누기
#   s.split('z') : s 문자열을 z 기호로 나누기
#   d.join(s) : d 단어를 s 문자열에 삽입

msg = "우리는 독도를 지킨다"
print(msg.replace("독도를", "대한민국을"))    # 우리는 대한민국을 지킨다
print(msg)                                  # replace는 원본을 변경하지 않는다
print(",".join(msg))                        # msg.join(",") 아님

# -----------------------------------------
#  (5) 문자열 포맷
#       (1) format() 이용
#       (2) % 이용
#   %를 이용하는 것이 format()보다 속도가 빠르지만 코드가 깔끔하지 않다.

msg = '{}님 오늘도 행복하세요 -{}으로부터'
print(msg.format("홍길동", "홍길자"))

# msg = '{0}님 오늘도 행복하세요- {1}으로부터'
msg = '{1}님 오늘도 행복하세요 -{0}으로부터'
print(msg.format("홍길자", "홍길동"))

msg = '{name}님 오늘도 행복하세요 -{group}으로부터'
print(msg.format(group="홍길자", name="홍길동"))

name = "홍길자"
age = 25
height = 160.9
print("%s님은 %d살이고, 키는 %.1f cm입니다" % (name, age, height))

# 연습
a = 11
b = 9
print("a" + "b")    # ab

# 연습2
fact = "Python is funny"
print(str(fact.count("n") + fact.find("n") + fact.rfind("n")))  # 3 + 13 + 5 = 21

# 연습3
text = "Gachon CS50 - programming with python"
text2 = " Human cs50 knowledge belongs to the world "
text.lower()
print(text[:5] + text[-1] + text[6] + text2.split()[0]) # Gacho + n +  + Human

# 연습4
class_name = "introduction programming with python"
for i in class_name:
    if i == "python":
        i = i.upper()
print(class_name)   # introduction programming with python, 수정안됨

# 연습5
a = "10"
b = "5-2".split("-")[1]
print(a * 3 + b)    # 1010102

# 연습6
a = "abcd e f g"
b = a.split()
c = (a[:3][0])      # a
c_1 = (a[:3])       # abc
d = (b[:3][0][0])   # a
d_1 = (b[:3])       # ["abcd" "e" "f"]
print(c + d)        # aa

# 연습7
result = "CODE2018"
print("{0}, {1}".format(result[-1], result[-2]))    # 8, 1

# [참고] http://pyformat.info
~~~

## list
~~~python
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

""" [출력결과]
    [1, 2, 3, 4, 5, 10]
    [1, 2, 3, 4, 5, 10, 'hello']
    1
    10
    HELLO
    h
"""

# 이중 리스트 만들고 인덱싱하기
arr.append([])
print(arr)

# 빈 리스트에 'korea'를 추가
arr[-1].append("korea")
print(arr)

# 'korea'안에 'a'를 추출
print(arr[-1][0][-1])

""" [ 연습 ] 아래에서
    a = ['인천','부산',['전라','경상',['판교','부천']]]
    (1) '경상' 요소 추출
    (2) '부천' 요소 추출
    (3) '판'이라는 글자만 추출
"""

a = ["인천", "부산", ["전라", "경상", ["판교", "부천"]]]
print(a[-1][1])
print(a[-1][-1][-1])
print(a[-1][-1][0][0])

""" [ 연습 ] 아래에서
    a = ['인천','부산',['전라','경상'],['대전','광주','대구'], '서울','제주']
    (1) '부산'부터 '대구'까지 추출
    (2) '대전'부터 '제주'까지 추출
    (3) '인천'부터 '서울'까지 추출
    (4) '광주'부터 '대구'까지 추출
"""

a = ["인천", "부산", ["전라", "경상"], ["대전", "광주", "대구"], "서울", "제주"]
print(a[1:4])
print(a[3:])
print(a[:5])
print(a[3][1:])

# --------------------------------------------------------------------
# (2) 리스트 연산자
a = ["독", "도", "는"]
b = ["대한민국", "섬"]
print(a + b)
print(a * 3)

# --------------------------------------------------------------------
# (3) 리스트 관련 함수들
#           append()    : 요소 추가
#           sort()      : 리스트 정렬 -> 원본변경
#           reverse()   : 역순으로 뒤집기 -> 원본변경
#           index()     : 위치 반환
#           insert()    : 리스트에 요소 삽입
#           remove()    : 요소 제거
#           pop()       : 맨 마지막 요소를 꺼내기
#           count()     : 요소 개수 세기
#           extend()    : 리스트에 리스트를 더하기 -> 원본변경
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

# [참고] 리스트에 리스트 구조에서 clear() 하는 경우
a1 = [1]
b1 = [7, 6, 5, 4, 3, a1]
print(a1)
print(b1)
b1.clear()  # 종속관계로 되어 있기에 b1의 내용만 삭제되고 a1은 유지된다
print(b1)
print(a1)

"""
    (8) 리스트 a의 모든 요소를 역순으로 뒤집기
    (9) 리스트 a 정렬하기
    (10) 리스트 a에 리스트 b를 더하기
    (11) 리스트 a에서 0번째부터 1번째 요소까지 삭제
"""

a = [3, 5, 4, 8, 0]
b = [1, 2]
a.reverse()
print(a)
a.sort()
print(a)
print(a + b)
del a[:2]
print(a)

# --------------------------------------------------------------
#  (4) 리스트 요소 변경
#       - 2번째 요소를 'z'로 변경
#       - 0번째부터 1번째 요소를 'k'와 'o'로 변경
a = [3, 5, 4, 8, 0]
a[2] = "z"
print(a)
a[0:2] = ["k", "o"]
print(a)

# --------------------------------------------------------------
# (5) 리스트 복사
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

# 연습
a = [0, 1, 2, 3, 4]
print(a[:3], a[-3]) # [0, 1, 2] 2

# 연습2
print(a[::-1])  # [4, 3, 2, 1, 0]

# 연습3
first = ["egg", "salad", "bread", "soup", "canafe"]
second = ["fish", "lamb", "pork", "beef", "chicken"]
third = ["apple", "banana", "orange", "grape", "mango"]
order = [first, second, third]
john = [order[0][:-2], second[1::3], third[0]]
print(john)                                     # [['egg', 'salad', 'bread'], ['lamb', 'chicken'], 'apple']
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
list_b = []
for i in range(len(list_a)):
    if i % 2 != 1:
        list_b.append(list_a[i])
print(list_b)   # ['Hankook', 'is', 'academic', 'located', 'South Korea']

# 연습9
admission_year = input("입학 연도를 입력하세요: ")
print(type(admission_year)) # <class 'str'>

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
print(a is b)   # False, 256 초과부터는 다른 주소값을 가진다

# 연습13
list_1 = [[1, 2], [3], [4, 5, 6]]
a, b, c = list_1
list_2 = a + b + c
print(list_2)   # [1, 2, 3, 4, 5, 6]
~~~

## tuple
~~~python
"""
#----------------------------------------------------------
[튜플 자료형]
    1- 리스트와 유사하지만 튜플은 값을 변경 못한다.
    2- 각 값에 대해 인덱스가 부여
    3- 변경 불가능 (*****)
    4- 소괄호 () 사용
"""

# (1) 튜플 생성
t = (1, 2, 3)
print(t)
print(t[0])

t2 = 1, 2, 3    # 권장하지 않음
print(t)
print(t[-1])

# 빈 튜플 생성
a = tuple()
print(a)
print(type(a))

# (2) 튜플은 요소를 변경하거나 삭제 안됨
'''
t[1] = 0;  # 블럭이 생기면서 실행 안됨
del t[1]   # 에러 발생
'''

print('------------------------------------')
# (3) "A"의 요소를 가진 튜플 t3를 선언하고 출력
t3 = ("A")          # () 우선순위를 위한 () 인식
print(t3)
print(type(t3))

t3 = ("A", )        # , 을 해줘야 튜플로 인식
print(t3)
print(type(t3))

print('------------------------------------')
# (4) 인덱싱과 연산자
print(t[2])
print(t[2:])
print(t * 3)
print(t + t2)

# (5) 튜플 요소 풀기
t5 = (1, 2, 3)
a, b, c = t5    # 반복문 없이 요소 풀기
print(a + b + c)
~~~

## dictionary
~~~python
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
# print(dt2[3])             # 존재하지않는 3 키값으로 추출 -> 에러발생
print(dt2.get(3))           # None
print(dt2.get(1, "없음"))    # 키값 1있으면 1값, 키값 1없으면 없음 출력

# Key와 Value만 따로 검색
print(dt2.keys())
print(dt2.values())
print(dt2.items())
~~~

## set
~~~python
# -----------------------------------------------
#  집합
#       - 집합에 관련된 자료형
#       - 순서를 지정하지 않는다
#       - 중복을 허용하지 않는다

s = set()   # 빈 집합을 생성
s = set([1, 2, 3, 1, 1])
print(s)
s3 = {3, 4, 5, 6}

print(s & s3)   # 교집합 : 3
print(s | s3)   # 합집합 : 1, 2, 3, 4, 5, 6
print(s - s3)   # 차집합 : 1, 2
~~~

## boolean
~~~python
 부울형 - 첫글자는 반드시 대문자 True, False, None 여야 한다

t = True
f = False
n = None    # 다른 언어의  Null 값과 유사

hungry = True
sleepy = False
print(hungry and sleepy)    # False
print(hungry or sleepy)     # True
print(hungry & sleepy)      # False

"""
        자료형         값           부울형
    -----------------------------------------------------
        문자형       "문자"          True
                    ""                     False
        리스트       [1,2,3]         True       
                    []                     False
        튜플         ()                     False
        딕셔너리     {}                     False
        숫자형       0이아닌 숫자     True
                    0                      False
                    None                   False
"""

if("아"):
    print("True")
else:
    print("False")  # True

if([]):
    print("True")
else:
    print("False")  # False

if(0):
    print("True")
else:
    print("False")  # False

if(-1):
    print("True")
else:
    print("False")  # True
~~~

## date
~~~python
"""
import datetime
today = datetime.date.today();
print("today is", today)
"""

from datetime import date, datetime, timedelta
today = date.today();
print("today is", today)

# 년, 월, 일 따로 출력
print(today.year, "년")
print(today.month, "월")
print(today.day, "일")

# 현재의 날짜와 시간 구하기
current_time = datetime.today()
print(current_time)

# 날짜 계산
today = date.today()
print("어제:", today+timedelta(days=-1))
print("내일:", today+timedelta(days=+1))
print("일주일전:", today+timedelta(days=-7))

print("-" * 50)
# 데이트형과 문자형 간에 변환
# 날짜 출력 형식(strftime() 이용)
today = datetime.today()
print(today)
print(today.strftime("%Y-%m-%d"))
print(today.strftime("%m/%d/%Y %H:%M"))

# 문자열로 날짜형식 변환(strptime() 이용)
str = "2020-08-20 12:25:33"
mydate = datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
print(mydate)
print(type(mydate))
~~~

## stdio
~~~python
"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int() / float() / str() 함수 이용 권장
"""

name = input("이름은?")
print("당신은 {0}입니다".format(name))
print("당신은 %s이다." % name)

# 나이를 입력받아서 한 살을 더해서 출력
# age = eval(input("나이는?"))
age = int(input("나이는?"))
print("당신의 나이는 {0}살 입니다.".format(age + 1))


print("1+2")        # 1+2
print(eval("1+2"))  # 3, str -> int 또는 float 변환


#----------------------------------
# 단을 입력받아 구구단을 구하기
dan = int(input("몇단?"))
for i in range(1, 10):
    print("{0} * {1} = {2}".format(dan, i, dan * i))


#-----------------------------------------
# print() 함수
print("안녕" "친구")
print("안녕" + "친구")
print("안녕", "친구")   # 띄어쓰기 됨

for i in range(5):
    print(i, end="")   # 개행

# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python a_datatype_class/Ex10_stdio.py ourserver scott tiger
#                              0           1       2      3

import sys
args = sys.argv[2:]
for i in args:
    print("정보:", i)

# 연습
# 사용자로부터 5개의 숫자를 읽어서 리스트에 저장하고 숫자들의 평균을 계산하여 출력한다.
# 또 숫자 중에서 평균을 상회하는 숫자가 몇개나 되는지 출력하여 보자.
li = []
cnt = 0

for i in range(5):
    li.append(int(input(str(i+1)+'번째 학생의 점수를 입력해주세요: ')))

avg = sum(li, 0.0) / len(li)
print("\n평균 = {0}".format(avg))

for x in li:
    if x > avg:
    cnt = cnt + 1
print("평균을 상회하는 개수 = {0}".format(cnt))

# 연습2
# 정수 리스트를 읽어서 역순으로 반환하는 reverseList() 함수를 작성하고
# 이것을 이용하여서 정수 리스트를 역순으로 출력한느 프로그램을 작성해보자.
parent_li = list(input('아무 글자나 입력하시면 역순으로 리스트를 출력해드립니다.'
+'\n아무 글자나 입력해보세요: '))
son_li = [None] * len(parent_li)
for i in range(len(parent_li)):
    son_li[i] = parent_li[-(i+1)]
print(son_li)


# 연습3
# 사용자에게 받은 정수들의 평균과 표준 퍈차를 계산하여 출력한다.
# 평균과 표준 편차를 계산하는 함수를 작성한 후에 이들 함수들을 호출하도록 하라.
import numpy
li = [int(s) for s in input("정수들을 '공백' 단위로 입력하시면"
+ ' 평균과 표준편차를 구해드립니다.'
+ '\n정수들을 입력해보세요: ').split()]

print('평균: {0}'.format(numpy.mean(li)))
print('분산: {0}'.format(numpy.var(li)))
print('표준편차: {0}'.format(numpy.std(li)))

# 연습4
# 전화 키패드에는 각 숫자키마다 3개의 문자가 적혀있다. 사용자가 입력한
# 문자열을 전화기의 숫자키로 변환하는 프로그램을 작성해보자.
# 숫자키가 keys 일 때
keypad = {2:"ABC", 3:"DEF", 4:"GHI", 5:"JKL",
          6:"MNO", 7:"PQRS", 8:"TUV", 9:"WXYZ"}
str_input = str(input("문자열을 입력하시오:"))
for i in str_input:
    for j in keypad.keys():
        if keypad[j].__contains__(i):
            print(j, end="")

# 숫자키가 values 일 때
keypad = {"ABC":2, "DEF":3, "GHI":4, "JKL":5,
          "MNO":6, "PQRS":7, "TUV":8, "WXYZ":9}
str_input = str(input("문자열을 입력하시오:"))
for i in str_input:
    for j in keypad.keys():
        if j.__contains__(i):
            print(keypad.get(j), end="")
~~~