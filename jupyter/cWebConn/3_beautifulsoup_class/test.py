from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://web.dominos.co.kr/goods/list?dsp_ctgr=C0102")

soup = BeautifulSoup(html, "html.parser")

ul = soup.select(".lst_prd_type > ul")
# print(ul)
for u in ul:
    for li in u:
        img = li[0].select_one("a > div .prd_img_view > img")
        print(img["src"])