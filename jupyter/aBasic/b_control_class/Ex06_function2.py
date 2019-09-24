# [추가] 함수도 객체이다
'''
def case1():
    print('case-1')


def case2():
    print('case-2')


def case3():
    print('case-3')


f = {"case1": case1, "case2": case2, "case3": case3}
print(f["case3"])
f["case3"]()

# ---------------------------------------
# 글로벌 변수와 지역변수
temp = "글로벌"


def func():
    temp = "지역"
    print("1>", temp)  # 지역


func()
print("2>", temp)  # 글로벌

temp = "글로벌"


def func():
    temp = "지역"
    print("1>", temp)  # 글로벌


func()
print("2>", temp)  # 글로벌

temp = "글로벌"


def func():
    global temp
    temp = "지역"
    print("1>", temp)  # 지역


func()
print("2>", temp)  # 지역

"""
#----------------------------------------------
# 람다함수 - 한번 사용하고 버리는 함수
# 파이션에서는 람다함수를 한 줄로 작성???

    파이썬 3.x부터는 람다를 권장하지 않는다고.
    몇몇 개발자들이 람다함수 사용시 직관적이지 않다는 이유라는데
    
    종종 사용됨
"""
f = lambda x, y: x + y
print(f(3, 2))

# -----------------------------------------------------------
"""  맵리듀스
    (1) map()
         ` 연속 데이터를 저장하는 시퀀스 자료형에서 요소마다 같은 기능을 적용할 때 사용
         ` 형식 : map(함수명, 리스트형식의 입력값)
         ` 파이썬 3.x에서는 list(map(calc, ex)) 반드시 list를 붙여야 리스트 형식으로 반환된다
           파이썬 2.x에서는 list 없이도 리스트 형식으로 반환
    (2) reduce()
         ` 리스트 같은 시퀀스 자료형에 차례대로 함수를 적용하여 모든 값을 통합하는 함수    
    
    파이썬 2.x에서는 많이 사용하던 함수이지만, 최근 문법의 복잡성으로 권장하지 않는 추세란다.
"""

ex = [1, 2, 3, 4, 5]


def calc(c):
    return c * 2


print(list(map(calc, ex)))

from functools import reduce


def calc(x, y):
    return x * y


print(reduce(calc, ex))

# lamda 적용하기
calc = lambda c: c * 2
print(list(map(calc, ex)))

from functools import reduce

calc = lambda x, y: x * y
print(reduce(calc, ex))

# 연습
# 리스트를 인자로 받아 짝수만 갖는 리스트 반환하는 함수
# [출력 결과]
# print(even_filter([1, 2, 4, 5, 8, 9, 10]))
def even_filter(li):
    result = []
    for i in li:
        if i % 2 == 0:
            result.append(i)
    return result
print(even_filter([1, 2, 4, 5, 8, 9, 10]))

# 연습2
# 주어진 수가 소수인지 아닌지 판단하는 함수
# [출력 결과]
# print(is_prime_number(60))
# print(is_prime_number(61))
def is_prime_number(num):
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                return "소수가 아닙니다."
            else:
                return "소수입니다."
    else:
        return "소수가 아닙니다."
print(is_prime_number(60))
print(is_prime_number(61))


# 연습3
# 주어진 문자열에서 모음의 개수를 출력하는 함수
# [출력 결과]
# print(count_vowel("pythonian"))
def count_vowel(sentence):
    cnt = 0
    for c in sentence:
        if c in "aeiou":
            cnt += 1    # 모음의 개수
    return cnt
print(count_vowel("pythonian"))
'''


# 연습
def test(t):
    t = 20
    print("In Function:", t)  # 20
x = 10
print("Before:", x)  # 10
test(x)
print("After:", x)  # 10

# 연습2
def sotring_function(list_value):
    return list_value.sort()
print(sotring_function([5, 4, 3, 2, 1]))    # None

# 연습3
def is_yes(your_answer):
    if your_answer.upper() == "YES" or you_answer.upper() == "Y":
        result = your_answer.lower()
print(is_yes("Yes"))    # None, return값이 없어서

# 연습4
def add_and_mul(a, b, c):
    return b + a * c + b
print(add_and_mul(3, 4, 5) == 63)   # False

# 연습5
def args_test_3(one, two, *args, three):
    print(one + two + sum(args))
    print(args)
args_test_3(3, 4, 5, 6, 7)  # TypeError

# 연습6
def rain(colors):
    colors.append("purple")
    colors = ["green", "blue"]
    return colors
rainbow = ["red", "orange"]
print(rain(rainbow))    # ['green', 'blue'], 지역변수 colors값이 출력

# 연습7
def function(value):
    print(value ** 3)   # 8
print(function(2))  # None

# 연습8
def get_apple(fruit):
    fruit = list(fruit)
    fruit.append("e")
    fruit = ["apple"]
    return fruit
fruit = "appl"
get_apple(fruit)
print(fruit)    # apple

# 연습9
def return_sentence(sentence, n):
    sentence += str(n)
    n -= 1
    if n < 0:
        return sentence
    else:
        return(return_sentence(sentence, n))
sentence = "I Love You"
print(return_sentence(sentence, 5)) # I Love You543210

# 연습10
def test(x, y):
    tmp = x # tmp = 'y'
    x = y   # x = 'x'
    y = tmp # y = 'y'
    return y.append(x)
x = ["y"]
y = ["x"]
test(x, y)
print(y)    # ['x']

# 연습11
def factorial_calculator(n):
    if n in (0, 1):
        return 1
    else:
        return n * factorial_calculator(n-1)
print(factorial_calculator(5))  # 120


