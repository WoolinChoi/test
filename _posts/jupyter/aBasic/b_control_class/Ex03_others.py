str = 'HELLO'                # 문자열
li = ['a','b','c']        # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')    # 튜플
di = dict(k=5, j=6)       # 딕셔너리

# (1) unpacking
a, b, c = tpl
print(b)    # ㄴ

alist = [(1, 2), (3, 4), (5, 6)]
for (first, second) in alist:        # list안에 ()요소별로 추출 가능
    print(first + second)   # 3, 7, 11

# (2) zip()
days = ["월", "화", "수"]
doit = ["잠자기", "공부", "놀기", "먹기"]
time = [10, 12, 2, 4, 6]

for yoil, halil in zip(days, doit):
    print(yoil, halil)
print(list(zip(days, doit, time)))  # 짧은 리스트 기준

# 연습
fruit = 'apple'
if fruit == 'Apple':
    fruit = 'Apple'
elif fruit == 'fruit':
    fruit = 'fruit'
else:
    fruit = fruit
print(fruit)    # apple

# 연습2
number = ["1", 2, 3, float(4), str(5)]
if number[4] == 5:
    print(type(number[0]))
elif number[3] == 4:
    print(number[2:-1]) # [3, 4.0]

# 연습3
num = 0
i = 1
while i < 8:
    if i % 3 == 0:
        break
    i += 1
    num += i
print(num)  # 5

# 연습4
result = 0
for i in range(5, -5, -2):
    if i < -3:
        result += 1
    else:
        result -= 1
print(result)   # -5

# 연습5
num = ""
for i in range(10):
    if i <= 5 and (i % 2) == 0:
        continue
    elif i is 7 or i is 10:
        continue
    else:
        num = str(i) + num
print(num)  # 986531

# 연습6
coupon = 0
money = 20000
coffee = 3500
while money > coffee:
    if coupon < 4:
        money = money - coffee
        coupon += 1
    else:
        money += 2800
        coupon = 0
print(money)    # 1800

# 연습7
list_data_a = [1, 2]
list_data_b = [3, 4]
for i in list_data_a:
    for j in list_data_b:
        result = i + j
print(result)   # 6