import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import seaborn as sns

tmp = pd.read_excel("지역_위치별(주유소).xls" )
data = tmp[   tmp["고급휘발유"]   != '-' ]  # 고급휘발유 데이터가 '-' 인 행을 제외
data["고급휘발유"] = [  float(value1)  for value1 in data["고급휘발유"] ]

#한글 폰트 등록
font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

sns.pairplot(data,hue="셀프여부")
plt.show()

