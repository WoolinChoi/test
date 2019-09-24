# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행

   (3) while 문
        while 조건문 :
            문장들
"""
a = 112                  # 숫자형
b = ['1','2','3']        # 리스트
c = '987'                # 문자열
d = tuple(b)             # 튜플
e = dict(k=5, j=6)       # 딕셔너리

for entry in e: # a(집합객체x)는 반복이 안되지만 b부터 e까지는 반복된다.
    print(entry)

for entry in e.items(): # 딕셔너리의 키값을 가져오려면 items() 이용
    print(entry)

# 1 ~ 10까지의 합
sum = 0
for i in range(1, 11):
    sum += i
print(sum)

# 1 ~ 10까지의 홀수의 합
sum = 0
for i in range(1, 11, 2):
    sum += i
print(sum)

# 2단 ~ 9단까지 구구단 출력
# 출력형식 : (1) format() 이용 (2) % 이용
for i in range(2, 10):
    for j in range(1, 10):
        print("{0} * {1} = {2}".format(i, j, i * j))
    print("-" * 50)

#----------------------------------------------------
# while

a = ["z", "y", "x"]
'''
while a:
    print(a.pop())  # a를 뒤에서부터 출력
else:
    print("end")    # end를 출력
'''

while a:
    data = a.pop()
    if data == "y":
        break       # while문에 break가 있으면 else가 실행되지 않음
    print(data)     # x
else:
    print("end")