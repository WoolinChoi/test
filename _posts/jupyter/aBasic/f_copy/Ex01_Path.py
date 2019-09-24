"""
 - import pathlib 만 선언하면
        Path클래스 사용시 pathlib.Path라고 명시해야 한다. 
"""
from pathlib import Path
# p = Path("C:\windows")
# p = Path(".")   # 현재 경로
p = Path("..")    # 부모 경로를 찾는다.
print(p)
print(p.resolve())    # 상대 경로를 찾는다.

result = []
for x in p.iterdir():    # 부모 경로를 기준으로 자식 경로를 찾는다. 하위 디렉터리와 파일도 자식으로 취급한다.
    if x.is_dir():    # 하위 파일은 취급하지 않는다.
        result.append(x)
print(result)

# 위와 동일하게 comprehension 방식
result = [x for x in p.iterdir() if x.is_dir()]
print(result)

# (2) glob() 이용
sub = list(p.glob("**/*.py"))    # 자손 디렉터리 중에서 py파일만 찾기
print(sub)

# 자손디렉터리 중에서 data 디렉터리 안에 csv 파일만 찾기
sub = list(p.glob("**/data/*.csv"))
print(sub)

