"""
    이메일 주소의 적합성 체크
        kim@encore.com   : 올바른 이메일
        kim@encore       : 잘못된 이메일 ( . 하나 없어서 )
        kim_@encore.com  : 잘못된 이메일 ( 특수문자 안됨 )

     [참고]
        ^[]: 시작
        [^] : not
        {2,9} : 최소 2개 최대 9개
        {2,} : 최소 2개만 지정하고 최대는 지정하지 않음
        $ 끝
        문자(.) : \. 으로 표시
"""
import re
# compile
def email_check(email):
    p = re.compile("^[a-zA-Z0-9+-_.] + @[a-zA-Z0-9-] + \.[a-zA-Z0-9-.]+$")
    if p.match(email) != None:
        print("올바른 이메일입니다")
    else:
        print("잘못된 이메일입니다")

email_check('kim@encore.com')       # 올바른 이메일
email_check('kim@encore')           # 잘못된 이메일 (. 하나 없어서)
email_check('k!!m_@encore.com')     # 잘못된 이메일 (특수문자 안됨)

