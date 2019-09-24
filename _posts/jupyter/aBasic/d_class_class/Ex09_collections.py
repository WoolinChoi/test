"""
    collections 모듈: 파이썬의 내장 모듈
    (1) deque : 스택과 큐를 모두 지원하는 모듈
    (2) OrderedDict : 순서를 가진 딕셔러니 객체
    (3) defaultdict : 딕셔너리 변수를 생성할 때 키에 대한 기본 값을 지정
                  같은 이름의 키의 값을 하나로 만들 때 사용
    (4) Counter : 시퀀스 자료형의 데이터 값의 개수를 딕셔너리 형태로 반환하는 자료구조
    (5) namedtuple : 튜플의 형태로 데이터 구조체를 저장하는 방법
"""

#-------------------------------------
# (1) deque : 스택과 큐를 모두 지원하는 모듈
#           - 리스트와 비슷한 형식으로 데이타를 저장한다.
#           - append() 함수로 기존 리스트처럼 데이터가 인덱스 번호와 저장된다
# import collections -> collections.deque.xxxx
from collections import deque    # deque.xxxx
deque_list = deque()
for i in range(5):    # 0, 1, 2, 3, 4
    deque_list.append(i)
deque_list.pop()    # 스택처럼
deque_list.pop()
deque_list.insert(1, 99)
print(deque_list)    # 결과 : deque([0, 99, 1, 2])

# -------------------------------------------
# (2) OrderedDict 모듈 : 순서를 가진 딕셔러니 객체
#                기본적인 딕셔너리는 순서를 보장하지 않는 객체이다
d = {}    # 빈 딕셔러니 생성
d["z"] = 100
d["b"] = 200
d["s"] = 300
d["a"] = 400
for k, v in d.items():    # 순서대로 보장안됨
    print(k, v)

from collections import OrderedDict
d = OrderedDict()        # 순서를 보장하는 딕셔너리
d["z"] = 100
d["b"] = 200
d["s"] = 300
d["a"] = 400
for k, v in d.items():
    print(k, v)

#----------------------------------------------
# (3) defaultdict : 딕셔너리 변수를 생성할 때 키에 대한 기본 값을 지정
#                   같은 이름의 키의 값을 하나로 만들 때 사용
"""
li = []    # 빈 리스트 생성
li = list()
d = {}    # 빈 딕셔러니 생성
d = dict()
"""
d = dict()
print(d["first"])    # Error, 생성하지 않은 키를 호출
from collections import defaultdict
d = defaultdict(lambda : 0)    # 어떤 인자가 들어와도 0으로 반환
print(d["first"])

s = [("yellow", 1), ("blue", 2), ("red", 5), ("yellow", 3), ("blue", 2)]
d = defaultdict(list)    # 초기값 형태를 list 구조로
for k, v in s:
    d[k].append(v)
print(d.items())    # dict_items([('yellow', [1, 3]), ('blue', [2, 2]), ('red', [5])])

#---------------------------------------------------
# (4) Counter 모듈 : 시퀀스 자료형의 데이터 값의 개수를 딕셔너리 형태로 반환하는 자료구조
from collections import Counter
text = list("gooooooood")
c = Counter(text)
print(c)

# 딕셔너리 형식의 초기값이 들어올 때
c = Counter({"yellow": 5, "red": 2})
print(c)
print(list(c.elements()))

#-------------------------------------------------
# (5) namedtuple : 튜플의 형태로 데이터 구조체를 저장하는 방법
from collections import namedtuple
MyPoint = namedtuple("MyPoint", ["x", "y"])
p = MyPoint(100, 200)
print(p.x, p.y)
print(p.x + p.y)

# 연습
class Person(object):
    def __init__(self, name):
        self.name = name
    def language(self):
        pass

class Earthling(Person):
    def language(self, language):
        return language

class Groot(Person):
    def language(self, language):
        return "I'm Groot!"

name = ['Gachon', 'Dr.Strange', 'Groot']
country = ['Korea', 'USA', 'Galaxy']
language = ['Korean', 'English', 'Groot']
for idx, name in enumerate(name):
    if country[idx].upper() != 'GALAXY':
        person = Earthling(name)
        print(person.language(language[idx]), end = " ")    # Korean English I'm Groot!
    else:
        groot = Groot(name)
        print(groot.language(language[idx]))

# 연습2
class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number
    def change_back_number(self, back_number):
        self.back_number = back_number

jinhyun = SoccerPlayer("jinhyun", "MF", 10)
print("현재 선수의 등번호는:", jinhyun.back_number)    # 10
jinhyun.change_back_number(5)
print("현재 선수의 등번호는:", jinhyun.back_number)    # 5

# 연습3
class Marvel(object):
    def __init__(self, name, characteristic):
        self.name = name
        self.characteristic = characteristic
    def __str__(self):
        return "My name is {0} and my weapon is {1}.".format(self.name, self.characteristic)

class Villain(Marvel):
    pass

first_villain = Villain("Thanos", "infinity gauntlet")
print(first_villain)    # My name is Thanos and my weapon is infinity gauntlet.

# 연습4
class TV(object):
    def __init__(self, size, year, company):
        self.size = size
        self.year = year
        self.company = company
    def describe(self):
        print(self.company + "에서 만든 " + self.year + "년형 " + self.size + "인치" + "TV")

class Laptop(TV):
    def describe(self):
        print(self.company + "에서 만든 " + self.year + "년형 " + self.size + "인치 " + "노트북", end = " ")
        LG_TV = TV("32", "2019", "LG")
        LG_TV.describe()

samsung_microwave = Laptop("15", "2018", "Samsung")
samsung_microwave.describe()    # Samsung에서 만든 2018년형 15인치 노트북 LG에서 만든 2019년형 32인치TV

# 연습5
class Score:
    def __init__(self, student):
        tmp = student.split(",")
        self.name = tmp[0]
        self.midterm = int(tmp[1])
        self.final = int(tmp[2])
        self.assignment = int(tmp[3])
        self.score = None
        self.grade = None

    def total_score(self):
        test_score = ((self.midterm + self.final)/2)*0.8
        if self.assignment >= 3:
            assign_score = 20
        elif self.assignment >= 2:
            assign_score = 10
        elif self.assignment >= 1:
            assign_score = 5
        else:
            assign_score = 0
        self.score = test_score + assign_score

    def total_grade(self):
        if self.assignment == 0:
            grade = "F"
        elif self.score >= 90:
            grade = "A"
        elif self.score >= 70:
            grade = "B"
        elif self.score >= 60:
            grade = "C"
        else:
            grade = "F"
        self.grade = grade
        return grade

student_john = Score("john, 90, 90, 0")
aa = student_john.total_score()
bb = student_john.total_grade()
print(aa, bb, student_john.score, student_john.grade)    # None F 72.0 F