# (1) 이름 : xxxx
#     번호 : xxxx
#     직업 : xxxx
import json
# f = open("./data/temp.json", "rt", encoding="utf-8")
# json_data = f.read()
# data = json.loads(json_data)
# # print(data)
# # print(type(data))
# for item in data:
#     print("이름>", item)    # 첫번째 요소
#     for item2 in data[item]:
#         if item2 == "No":
#             print("번호>", data[item][item2])
#         if item2 == "Job":
#             print("직업>", data[item][item2])
# f.close()

# with 구문
try:
    with open("./data/temp.json", "rt", encoding="utf-8") as f:
        json_data = f.read()
        data = json.loads(json_data)
        # print(data)
        # print(type(data))
        for item in data:
            print("이름>", item)  # 첫번째 요소
            for i, item2 in enumerate(data[item]):
                print(data[item][item2], [i])
except Exception as e:
    print("예외발생:", e)
else:
    print("\n 정상종료")
