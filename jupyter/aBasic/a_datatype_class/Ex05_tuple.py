"""
#----------------------------------------------------------
[튜플 자료형]
    1- 리스트와 유사하지만 튜플은 값을 변경 못한다.
    2- 각 값에 대해 인덱스가 부여
    3- 변경 불가능 (*****)
    4- 소괄호 () 사용
"""
print('----------------- 1 -------------------')
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

print('----------------- 2 -------------------')
# (2) 튜플은 요소를 변경하거나 삭제 안됨
'''
t[1] = 0;  # 블럭이 생기면서 실행 안됨
del t[1]   # 에러 발생
'''

print('----------------- 3 -------------------')
# (3) "A"의 요소를 가진 튜플 t3를 선언하고 출력
t3 = ("A")          # () 우선순위를 위한 () 인식
print(t3)
print(type(t3))

t3 = ("A", )        # , 을 해줘야 튜플로 인식
print(t3)
print(type(t3))

print('----------------- 4 -------------------')
# (4) 인덱싱과 연산자
print(t[2])
print(t[2:])
print(t * 3)
print(t + t2)

# (5) 튜플 요소 풀기
t5 = (1, 2, 3)
a, b, c = t5    # 반복문 없이 요소 풀기
print(a + b + c)