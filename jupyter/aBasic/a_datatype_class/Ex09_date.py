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