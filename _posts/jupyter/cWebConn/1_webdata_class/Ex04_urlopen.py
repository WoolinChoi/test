# urlretrieve(): 파일로 바로 저장
# urlopen(): 파일로 바로 저장하기 않고 메모리에 로딩을 한다.

""" [참고] 파일저장 기본방식
    f = open('a.txt','w')
    f.write("테스트 내용")
    f.close()

    위의 과정을 with 문으로 간략하게 close 필요없음
    with open("a.txt","w") as f:
        f.write("테스트 내용")
"""

from urllib import request

url = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
imgName = "./data/google.png"

# 1. 웹에서 열기
site = request.urlopen(url)
img = site.read()

# 2. 파일 저장
with open(imgName, "wb") as f:    # 이미지는 t(텍스트)가 아닌 b(바이너리)
    f.write(img)