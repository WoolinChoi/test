"""
    파일을 다운받고 저장하는 함수

     [참고] 파이썬 정규식 표현 : https://wikidocs.net/4308
"""
from bs4 import BeautifulSoup
from urllib import parse
from urllib import request
import os, time, re  # re : 정규식

def download_file(url):
    p = parse.urlparse(url)
    print("1 >>>", p)
    savepath = "./" + p.netloc + p.path
    print("2 >>>", savepath)

    # "/"로 끝나서 파일일명이 는 경우는 index.html을 붙여줌
    if re.search("/$", savepath):    # /로 끝나는지 확인
        savepath += "index.html"
        print("3 >>>", savepath)

    # 해당경로에 파일이 없으면 다운로드 받지 않고 retrun
    if os.path.exists(savepath):    # 디렉터리안에 파일이 유무 확인, 없으면 return
        return

    # 해당경로의 디렉터리가 없으면 디렉터리 생성
    savedir = os.path.dirname(savepath)
    if not os.path.exists(savedir):    # savedir이 없으면
        os.makedirs(savedir)    # makedirs: 하위폴더까지 생성

    # 웹페이지 다운받기
    try:    # 예외처리해주기
        request.urlretrieve(url, savepath)    # url을 바로 savepath으로 다운로드
        time.sleep(1)    # 1초의 시간 여유
        return savepath
    except:
        print("download falled:", url)
        return None

if __name__ == '__main__':
    url = 'https://docs.python.org/3.6/library/'
    result = download_file(url)
    print(result)



