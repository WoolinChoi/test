"""
    exfile2.py
    mypackage 패키지 안에 있는 mymodule을 import하여 사용하고자 함
"""

import mypackage.mymodule

today = mypackage.mymodule.get_weather()
print(today)


from mypackage import mymodule
# get_weather() 호출하여 출력
today = mymodule.get_weather()
print(today)

import module_ex
