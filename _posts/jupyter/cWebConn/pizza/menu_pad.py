#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Yongwook
#
# Created:     04-05-2016
# Copyright:   (c) Yongwook 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from PIL import ImageTk
from PIL import Image
import matplotlib.pylab as plt

root = Tk()
root.geometry("1280x800+100+100")

flag = False
def hidden_button():
    global flag
    flag = True

Label(root, text=u"도민석피자", background="seashell3", font=("Helvetica", 20)).place(x=170, y=20)
Button(root, text=u"매출관리", command=lambda: sales_management()).place(x=1030, y=20)

# 피자, 사이드디시, 음료, 피클&소스 서브메뉴를 db에 가져와서 넣는다.
sel_menu1 = {1: (u"선택하지 않음", 0), 2: (u"야채 스프", 4000), 3: (u"마늘빵", 3000), 4: (u"싱싱 샐러드", 5000)}
sel_menu2 = {1: (u"선택하지 않음", 0), 2: (u"크리스피 치킨윙", 10000), 3: (u"감자 튀김", 7000), 4: (u"오븐 스파게티", 9000)}
sel_menu3 = {1: (u"선택하지 않음", 0), 2: (u"비프 스테이크", 30000), 3: (u"포크 스테이크", 25000), 4: (u"비프 스튜", 25000)}
sel_menu4 = {1: (u"선택하지 않음", 0), 2: (u"젤라또", 6000), 3: (u"마블 브라우니", 5000), 4: (u"벨기에 와플", 6000)}

# 서브메뉴
sel_menu = {u"피자": sel_menu1, u"사이드디시": sel_menu2, u"음료": sel_menu3, u"피클&소스": sel_menu4}

# 선택하지 않았을 때 0값
final_selected = {1: (u"선택하지 않음", 0), 2: (u"선택하지 않음", 0), 3: (u"선택하지 않음", 0), 4: (u"선택하지 않음", 0)}

# 주메뉴
menu_name = {1: u"피자", 2: u"사이드디시", 3: u"음료", 4: u"피클&소스"}

class menu:

    def __init__(self, number):
        self.number = number
        self.this_menu_name = menu_name.get(number)
        self.var = IntVar()
        self.var.set(1)

    # 선택
    def selected(self):
        temp = sel_menu.get(self.this_menu_name).get(self.var.get())[0]
        menu_1.destroy()
        Label(root, text=u"선택된 메뉴 :                           ", background="seashell3").place(x=1000, y=70+170*(self.number-1))
        Label(root, text=u"선택된 메뉴 : " + temp, background="seashell3").place(x=1000, y=70+170*(self.number-1))
        global final_selected
        final_selected[self.number] = sel_menu.get(self.this_menu_name).get(self.var.get())    # 최종선택

    # 서브 메뉴
    def pop_menu(self):
        global menu_1
        menu_1 = Toplevel(root)
        menu_1.title(self.this_menu_name)
        y = 170*self.number + 25
        menu_1.geometry("250x100+110+%d" % (y))
        for i in sel_menu.get(self.this_menu_name):
            Radiobutton(menu_1, text=sel_menu.get(self.this_menu_name).get(i)[0], variable=self.var, value=i, indicatoron=0, relief=RAISED, command=self.selected).pack(fill=X)

# 매출 관리, db에서 가져온 판매일자 x축, 매출 y축
def sales_management():
    plt.title("sales_management")
    plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
    plt.show()

# 주메뉴
def make_menu(number):
    global this_menu
    this_menu = menu(number)
    this_menu.pop_menu()    # 서브메뉴 호출

# 주문
def order():
    global v
    global flag
    ordering = Toplevel(root)
    cost = 0
    for i in final_selected:
        cost += final_selected[i][1]
    for i in menu_name:
        Label(ordering, text=menu_name.get(i) + ':').grid(row=i, column=1)
        Label(ordering, text=final_selected.get(i)[0]).grid(row=i, column=3)
        Label(ordering, text=final_selected.get(i)[1]).grid(row=i, column=5)
    Label(ordering, text=u"계산하실 금액은 " + str(cost) + u"원 입니다.").grid(row=7, column=3)
    Button(ordering, text=u"결제", command=lambda: pop_sales(cost)).grid(row=7, column=5)

# 결제
def pop_sales(cost):
    sales = Toplevel()
    sales.title("결제")
    sales.geometry("50x50")
    Label(sales, text="결제되었습니다.").place(x=10, y=10)

# 메인 화면을 띄운다.
mymenu = menu(root)

# 4가지 주메뉴 버튼을 생성 후 make_menu() 호출
Button(root, text=u"피자", command=lambda: make_menu(1)).place(x=10, y=70)
Button(root, text=u"사이드디시", command=lambda: make_menu(2)).place(x=10, y=240)
Button(root, text=u"음료", command=lambda: make_menu(3)).place(x=10, y=410)
Button(root, text = u"피클&소스", command=lambda: make_menu(4)).place(x=10, y=580)

Button(root, text=u"주문하기", command=order).place(x=1030, y=760)

# 주메뉴 이미지 붙이기
images = [(1, "pizza.png"), (2, "side_dish.png"), (3, "beverage.png"), (4, "pickle&sauce.png")]
for i, image in images:
    img = Image.open(image)
    this_image = ImageTk.PhotoImage(img)
    mylabel = Label(image=this_image)
    mylabel.image = this_image
    mylabel.place(x=100, y=70+(i-1)*170)

v = StringVar()

root.config(width=600, height=800, background="seashell3")

root.title(u"도민석피자")
root.mainloop()