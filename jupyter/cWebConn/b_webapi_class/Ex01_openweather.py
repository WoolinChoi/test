"""
    전세계날씨제공 API : http://openweathermap.org

    1. 회원가입 : 메뉴 > Sign Up > 사용용도 : Education > 대충가입 (무료는 1번에 60번 호출 가능 )
    2. 개발자모드 : Sign In > API Keys 에서 내가 발급받은 키 (추가 키 가능)
    3. 발급받고 바로 지정 안됨 (시간소요)
"""

# API 키를 지정합니다. 자신의 키로 변경해서 사용해주세요.
apikey = "e2c0b303b5954b5cb53c2126be06c61f"

# 날씨를 확인할 도시 지정하기
cities = ["Seoul, KR", "Tokyo, JP", "New York, US"]
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
import requests
import json

for cname in cities:
    url = api.format(city=cname, key=apikey)
    res = requests.get(url)
    # print(res.text)    # type이 str이기 때문에
    data = json.loads(res.text)    # json으로 만들기
    # print(data)    # type이 dict으로 바뀜
    print("도시명:", data["name"])
    print("날씨:", data["weather"][0]["main"])
    print("최저온도:", round(data["main"]["temp_min"]-273.15, 2))
    print("최고온도:", round(data["main"]["temp_min"]-273.15, 2))
    print("습도:", data["main"]["humidity"])
    print("기압:", data["main"]["pressure"])
