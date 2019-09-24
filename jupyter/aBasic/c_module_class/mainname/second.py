import first  # fist 모듈을 가져옴 -> 에러나지만 관계없음
print('second.py __name__:', __name__)  # __name__ 변수 출력(__main__)

# import로 모듈 가져오면 __name__ 변수에 모듈명(=파일명) 들어가고
# import 하지 않는 상태라면 __name__ 변수에 __main__ 이름이 들어감