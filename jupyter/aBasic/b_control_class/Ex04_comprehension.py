"""
    @ 컴프리핸션 (comprehension)
    ` 하나 이상의 이터레이터로부터 파이썬 자료구조를 만드는 컴팩트한 방법
    ` 비교적 간단한 구문으로 반복문과 조건 테스트를 결합

    * 리스트 컨프리핸션
        [ 표현식 for 항목 in 순회가능객체 ]
        [ 표현식 for 항목 in 순회가능객체 if 조건 ]

    * 딕셔러리 컨프리핸션
        { 키_표현식: 값_표현식 for 표현식 in 순회가능객체 }

    * 셋 컨프리핸션
        { 표현식 for 표현식 in 순회가능객체 }
"""

# 컨프리핸션 사용하지 않은 리스트 생성
'''
alist = []
alist.append(1)
alist.append(2)
alist.append(3)
alist.append(4)
alist.append(5)
alist.append(6)
print(alist)

alist = []
for n in range(1,6):
    alist.append(n)
print(alist)

alist = list(range(1,6))
print(alist)
'''

#------------------------------------------------
# 리스트 컨프리핸션
# [예] [1, 2, 3, 4, 5, 6]
blist = [n ** 2 for n in range(1, 7)]
print(blist)

clist = [n for n in range(1, 11) if n % 2 == 0]
print(clist)

rows = range(1, 4)      # 1, 2, 3
cols = range(1, 6, 2)   # 1, 3, 5
dlist = [(r, c) for r in rows for c in cols]
print(dlist)

# dlist에서 각 요소 추출하여 출력
for data in dlist:
    print(data)

for (frist, second) in dlist:
    print(frist, second)

#-------------------------------------------
# 딕셔러니 컨프리핸션
# {키 : 값}
a = {x : x**2 for x in (2, 3, 4)}
print(a)    # {2: 4, 3: 9, 4: 16}

word = "LOVE LOL"
wcnt = {letter: word.count(letter) for letter in word}
print(wcnt) # {'L': 3, 'O': 2, 'V': 1, 'E': 1, ' ': 1}, 값은 문자는 같은 키값을 가진다.

#-------------------------------------------
# 셋 컨프리핸션
#   {1, 2, 3, 4, 5, 6}

data = [1, 2, 3, 1, 3, 5, 6, 2]
alist = [n for n in data if n % 2 == 1]    # 리스트
print(alist)

aset = {n for n in range(1, 7)}     # 셋
print(aset)

"""
@ 리스트 컨프리핸션과 셋 컨프리핸션의 차이는?
    리스트 : 인덱스 / 중복허용 / 변경가능
    튜플 : 인덱스 / 중복허용 / 변경불가
    셋 : 인덱스 X / 중복 X / 변경가능
    딕셔너리 : 키와 값 / 키는 중복 X / 인덱스 X
"""

#-------------------------------------------
# [참고] 제너레이터 컨프리핸션
# ()를 사용하면 튜플이라 생각하지만 튜플은 컨프리핸션이 없다.
# 제너레이터 컨프리핸션은 한 번만 실행
# 즉석에서 그 값을 생성하고 이터레이터를 통해 한 번에 값을 하나씩 처리하고 저장하지 않음
data = [1, 2, 3, 1, 3, 5, 6, 2]
alist = (n for n in data if n % 2 == 1) # 제너레이터 컨프리핸션(절대로 튜플이 아님)
print(alist)
print(type(alist))
print(list(alist))

print(list(alist))

'''
# 연습
# BMI(Body Mass Index)는 체중(kg)을 신장(m)의 제곱(**2)으로나눈 값으로 체지방 축적을 잘 반영하기 때문에 비만도 판정에
# 많이 사용한다. 사용자로부터 신장과 체중을입력 받아서 BMI 값에 따라서 다음과 같은 메시지를 출력하는 프로그램을 작성하여 보자.
kg = float(input("체중을입력하세요:"))
m = float(input("신장을입력하세요:"))

bmi = kg / m ** 2
print("당신의 BMI: %.2f" % bmi)

if 20 <= bmi >= 24.9:
    print("정상입니다.")
elif 25 <= bmi <= 29.9:
    print("과체중입니다.")
elif bmi >= 30:
    print("비만입니다.")
# 연습2
# 1부터 99까지 2자리의 정수로 이루어진 복권이 있다고 하자. 2자리가 전부 일치하면 1등상 100만원을 받는다.
# 2자리중에서 하나만 일치하면 50만원을 받고 하나도 일치하지 않으면 상금은 없다.
# 1에서 100 사이의 난수가 발생된다.
num = int(input('복권 번호(1-99)를 입력하시오 '))
import random

number = random.randint(1, 100)
print('입력번호 : ', num)
print('당첨번호 : ', number)

num_sp = list(str(num))
if len(num_sp) != 2:
    num_sp = ['0'] + num_sp
# print(num_sp)
number_sp = list(str(number))
if len(number_sp) != 2:
    number_sp = ['0'] + number_sp

aa = list(zip(num_sp, number_sp))
print(aa) # [('0', '6'), ('3', '8')]

score = 0
for a, b in aa:
    if a == b:
        score += 50
print(score, "만원")
'''