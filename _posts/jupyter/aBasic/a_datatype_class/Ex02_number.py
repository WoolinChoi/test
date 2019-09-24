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

'''
a = 5
b = 2
# print('a++=", a++)    # 에러
print('a/b=', a/b)
print('a//b=' + a//2)   # 문자열 + 숫자는 문자열변경이 되지 않고 에러
print('a//b=' + str(a//2))
print('a//b=', a//2)
print('a%b=', a%b)
print('a**b=', a**b)
'''

""" [ 출력결과 ] 
        a / b = 2.5
        a // b = 2
        a % b = 1
        a ** b = 25
"""

# 출력 포맷
'''
y = 8.3/2.7
print(y)
print('실수: {0}, 정수: {1}'.format(y, 100))
print('실수: {}, 정수: {}'.format(y, 200))
print('실수: {1}, 정수: {0:.1f}'.format(y, 300))
'''

# 기타연산자
'''
print('Hello' is 'hello')   # false
print('Hello' is not 'Hello')   # false
print('H' in 'Hello')   # true
print('H' not in 'Hello')   # false
'''

# 연습
'''
a = 777
b = 777
print(a == b, a is b)   # true, false
'''

# 연습2
'''
a = 3.5
b = int(3.5)
print(a ** ((a // b) * 2))  # 12.25
print(((a - b) * a) // b)   # 0.0
b = (((a - b) * a) % b)
print(b)                    # 1.75
print((a * 4) % (b * 4))    # 0.0
'''

# 연습3
'''
celsius = float(input("섭씨온도를 입력하세요:"))
fahrenheit = ((9 / 5) * celsius) + 32
print("섭씨온도:", celsius, "화씨온도:", fahrenheit)
'''

# 연습4
'''
a = "True"
print(type(a))  # str
'''

# 연습5
'''
a = 10.6
b = 10.5
print(a * b)
print(type(a + b))  # float
'''

# 연습6
'''
a = "3.5"
b = 4
print(a * b)    # 3.53.53.53.5, 문자열 * 4는 문자열을 4번 출력한다
'''

# 연습7
'''
a = "3.5"
b = "1.5"
print(a + b)    # 3.51.5, 문자열 + 문자열은 붙어서 출력한다
'''

# 연습 8
'''
a = "3" # str
b = float(a)    # float로 형변환
print(b ** int(a))  # 27.0, 형변환해주면 계산가능하다
'''

# 연습9
'''
a = "20"
b = "4"
print(type(float(a / b)))   # type 에러
'''

# 연습10
'''
a = "Gachon"
b = "CS"
c = 200
c = str(c - 150)
print(a, b, c)  # Gachon CS 50
'''