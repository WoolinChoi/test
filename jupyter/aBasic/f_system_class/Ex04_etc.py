"""
경로 이동은  Path 모듈로 안되어 os 모듈이 필요하다
"""
from pathlib import Path
import os

# print(Path.cwd())
# os.chdir("C:\Windows")
# print(Path.cwd())    # os 모듈로 디렉터리를 바꿀 수 있다.


# 리눅스에서 주로 사용
print(os.environ["HOMEPATH"])    # 윈도우경우 \Users\Playdata
sub = Path("hadoop/myproject/myjob")
p = Path(os.environ["HOMEPATH"], sub)
print(p)

#------------------------------------------------------------
import shutil
# shutil.rmtree("imsi")    # 비어있지 않은 디렉터리도 지워버림
# shutil.copy("Ex00.txt", Path("copy.txt"))    # 디렉터리가 존재했을때 파일 copy가 가능
shutil.copytree(".", "../f_copy")    # 디렉터리까지 copy가 가능