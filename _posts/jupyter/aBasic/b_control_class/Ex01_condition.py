"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록을 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자

    [ex]
    if a>b:
        print(a)
            print(b)  => 에러발생

    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            문장들
        else :
            문장들

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass
        ` 파이썬은 switch 문 없음
"""

# 거짓(False)의 값
i = 0
i2 = 0.0
i3 = ""
i4 = str()
i5 = list()
i6 = tuple()
i7 = set()
i8 = dict()
i9 = {}
i10 = None

# (1) 간단한 if문
a = -1
if a:
    print("True-1") # True
else:
    print("False-1")

if not a:
    print("True-2") # 출력 안됨

# (2) 논리연산자 이용한 조건
a = 10
b = 0               # -1 : True
if a and b:
    print("True-3") # 출력 안됨

if a or b:
    print("True-4") # True

print(a and b)  # 0, a이고 b일때 a가 True이고 b값에 결정권을 주기때문에 b값을 출력
print(a or b)   # 10, a이거나 b일때 이미 a가 True이기 때문에 a값을 출력

# (3) find() - 해당글자를 찾으면 그 글자의 인덱스 반환
#              해당글자를 못 찾으면 -1 리턴
word = "korea"
if word.find("k"):  # 해당글자를 찾으면 0이기 때문에
    print("1>")     # 출력 안됨

if word.find("z"):  # 해당글자를 못찾으면 -1이기 때문에
    print("2>")     # 출력

# 해당하는 문자가 있는 경우만 조건문 안에서 실행(3> 실행)
if word.find("k") > -1: # 해당글자를 찾으면 0인데 > -1보다 크므로
    print("3>")         # 출력

# (4) 변수
a, b = 0, 1
if a:       # False
    c = 2
elif b:     # True
    c = 4
else:
    c = 8
print(c)    # 4

