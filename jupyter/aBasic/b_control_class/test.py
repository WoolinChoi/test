import re
def email_check(email):
    e_ch = email.split('@')
    print(e_ch)
    id = e_ch[0]
    addr = e_ch[1]
    if len(e_ch) == 2 and re.search('\.{1,1}',addr):
        result = '올바른 이메일입니다.'
    if re.findall('[\W]',id):
        result = '잘못된 이메일입니다.'
    else:
        result = '잘못된 이메일입니다.'
    print(result)

email_check('kim@encore.com') # 올바른 이메일
email_check('kim@encore') # 잘못된 이메일 (. 하나 없어서 )
email_check('k!m_@encore.com') # 잘못된 이메일 ( 특수문자 안됨 )