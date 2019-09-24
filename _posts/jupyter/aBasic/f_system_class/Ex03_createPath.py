from pathlib import Path

# ------------------------------------------------
# 1. 경로의 상태보기
print(Path.cwd())    # 현재 경로
print(Path.home())   # Home 경로, windows C:/users/계정명, 리눅스(hadoop) : /home/hadoop/

p = Path("Ex03_createPath.py")
print(p.stat())    # 리눅스 스타일

# ----------------------------------------------------
# 2. 경로(파일) 생성시간 알아보기
import stat
import datetime
p = Path("Ex03_createPath.py")
print(p.stat()[stat.ST_CTIME])
print(datetime.datetime.fromtimestamp(p.stat()[stat.ST_CTIME]))

# ------------------------------------------------
# 3. 디렉토리 생성
p2 = Path("imsi")
p2.mkdir(exist_ok=True)
p3 = Path("imsi2/myclass/python")
p3.mkdir(parents=True)

# ------------------------------------------------
# 4. 파일 생성
# imsi / a.txt  파일에 "홍길동 화이팅" 생성
p = Path("imsi/a.txt")
with open(p, "wt", encoding="utf-8") as f:
    f.write("홍길동 화이팅")

# touch()
p = Path("imsi/z.txt")
p.touch()

# a.txt 파일명을 test.txt 파일명으로 변경
p = Path("imsi/test.txt")
# p.rename("imsi/test.txt")
p.replace("imsi/test.txt")

# ------------------------------------------------
#  5. 경로 제거
f = Path("imsi")
f.rmdir()    # 빈 디렉터리가 아니면 Error

# 파일 지우기(imsi/z.txt 지우기)
f = Path("imsi/z.txt")
f.unlink()

# os 모듈
import os
f = Path("imsi/z.txt")
os.remove(f)