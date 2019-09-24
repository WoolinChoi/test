"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int() / float() / str() 함수 이용 권장
"""

'''
name = input("이름은?")
print("당신은 {0}입니다".format(name))
print("당신은 %s이다." % name)

# 나이를 입력받아서 한 살을 더해서 출력
# age = eval(input("나이는?"))
age = int(input("나이는?"))
print("당신의 나이는 {0}살 입니다.".format(age + 1))
'''

'''
print("1+2")        # 1+2
print(eval("1+2"))  # 3, str -> int 또는 float 변환
'''

#----------------------------------
# 단을 입력받아 구구단을 구하기
'''
dan = int(input("몇단?"))
for i in range(1, 10):
    sum = dan * i
    print("{0} * {1} = {2}".format(dan, i, sum))
'''

#-----------------------------------------
# print() 함수

'''
print("안녕" "친구")
print("안녕" + "친구")
print("안녕", "친구")   # 띄어쓰기 됨

for i in range(5):
    print(i, end="")   # 개행
'''

# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python a_datatype_class/Ex10_stdio.py ourserver scott tiger
#                              0           1       2      3

'''
import sys
args = sys.argv[2:]
for i in args:
    print("정보:", i)
'''

# 연습
# 사용자로부터 5개의 숫자를 읽어서 리스트에 저장하고 숫자들의 평균을 계산하여 출력한다.
# 또 숫자 중에서 평균을 상회하는 숫자가 몇개나 되는지 출력하여 보자.
'''
num = int(input("정수를 입력하세요:"))
num2 = int(input("정수를 입력하세요:"))
num3 = int(input("정수를 입력하세요:"))
num4 = int(input("정수를 입력하세요:"))
num5 = int(input("정수를 입력하세요:"))

num_list = [num, num2, num3, num4, num5]
avg = sum(num_list, 0.0) / len(num_list)
print("평균:", avg)
count = 0
for i in range(0, len(num_list)):
    if num_list[i] > avg:
        count += 1
print("평균을 상회하는 수:", count)
'''

# 연습2
# 정수 리스트를 읽어서 역순으로 반환하는 reverseList() 함수를 작성하고
# 이것을 이용하여서 정수 리스트를 역순으로 출력한느 프로그램을 작성해보자.
'''
num = int(input("정수를 입력하세요:"))
num2 = int(input("정수를 입력하세요:"))
num3 = int(input("정수를 입력하세요:"))
num4 = int(input("정수를 입력하세요:"))
num5 = int(input("정수를 입력하세요:"))

num_list = [num, num2, num3, num4, num5]
num_list.reverse()
print(num_list)
'''

# 연습3
# 사용자에게 받은 정수들의 평균과 표준 퍈차를 계산하여 출력한다.
# 평균과 표준 편차를 계산하는 함수를 작성한 후에 이들 함수들을 호출하도록 하라.
'''
num = int(input("정수를 입력하세요:"))
num2 = int(input("정수를 입력하세요:"))
num3 = int(input("정수를 입력하세요:"))
num4 = int(input("정수를 입력하세요:"))
num5 = int(input("정수를 입력하세요:"))

num_list = [num, num2, num3, num4, num5]
avg = sum(num_list, 0.0) / len(num_list)
print("평균:", avg)

import numpy
print("표준편차:", numpy.std(num_list))
'''

# 연습4
# 전화 키패드에는 각 숫자키마다 3개의 문자가 적혀있다. 사용자가 입력한
# 문자열을 전화기의 숫자키로 변환하는 프로그램을 작성해보자.

'''
# 숫자키가 values 일 때
keypad = {"ABC":2, "DEF":3, "GHI":4, "JKL":5,
          "MNO":6, "PQRS":7, "TUV":8, "WXYZ":9}
str_input = str(input("문자열을 입력하시오:"))
for i in str_input:
    for j in keypad.keys():
        if j.__contains__(i):
            print(keypad.get(j), end="")


# 숫자키가 keys 일 때
keypad = {2:"ABC", 3:"DEF", 4:"GHI", 5:"JKL",
          6:"MNO", 7:"PQRS", 8:"TUV", 9:"WXYZ"}
str_input = str(input("문자열을 입력하시오:"))
for i in str_input:
    for j in keypad.keys():
        if keypad[j].__contains__(i):
            print(j, end="")
'''