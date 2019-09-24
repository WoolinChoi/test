import csv
# [1] 리스트 데이타를 csv 파일에 저장한다
# data = [[1, "김", "책임"], [2, "박", "선임"], [3, "주", "연구원"]]
# with open("./data/imsi.csv", "wt", encoding="utf-8") as f:
#     cout = csv.writer(f)
#     cout.writerows(data)

# [2] csv 파일을 읽어서 리스트 변수 저장 출력
data = []
with open("./data/imsi.csv", "r", encoding="utf-8") as f:
    cin = csv.reader(f)
    data = [row for row in cin if row]    # row가 있으면 출력(공백제거)
print(data)    # [[1, "김", "책임"], [2, "박", "선임"], [3, "주", "연구원"]]