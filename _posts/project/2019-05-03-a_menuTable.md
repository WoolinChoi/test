---
layout: post
title: menuTable
category: git
tags: [java, project, menuTable]
comments: false
---

# [menuTable]()

## menuTable
~~~java
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class MenuTable {
	
    JFrame f;
    
    String[] menu;
    String[] hamburger_list;
    String[] chicken_list;
    String[] dessert_list;
    String[] drink_list;
    
    int[] hamburger_price;
    int[] chicken_price;
    int[] dessert_price;
    int[] drink_price;
    
    JButton[] bmenu;
    JButton[] bhamburger;
    JButton[] bchicken;
    JButton[] bdessert;
    JButton[] bdrink;
    
    JButton pay;
    
    JTextField name_cat;
    JTextField name_good;
    JTextField name_price;
    JTextField name_sum;
    
    JTextArea sel_cat;
    JTextArea sel_good;
    JTextArea sel_price;
    JTextArea sum;
    
    String save_cat;
    String save_good;
    String save_price;
    
    int save_sum;
    
    MenuTable() {
        f = new JFrame("패스트푸드 메뉴판");
 
        menu = new String[] {"햄버거", "치킨", "디저트", "드링크"};
        bmenu = new JButton[menu.length];
        
        for (int i = 0; i < menu.length; i++) {
            bmenu[i] = new JButton(menu[i]);
        }
        hamburger_list = new String[] {"불고기버거", "치킨버거",
                "새우버거", "와규",
                "한우불고기", "AZ버거", "핫크리스피버거",
                "T-Rex", "비프바베큐버거"}; 
        chicken_list = new String[] {"치킨휠레(4조각)",
                "화이어윙(2조각)", "화이어윙(4조각)",
                "치킨1조각", "치킨휠레(2조각)", "패밀리팩",
                "치킨풀팩", "치킨하프팩", "순살치킨하프팩"};
        dessert_list = new String[] {"치킨너켓", "롱치즈스틱",
                "해쉬브라운", "콘셀러드",
                "선데아이스크림", "쉑쉑치킨",
                "양념감자", "오징어링", "포테이토"};
        drink_list = new String[] {"아이스아메리카노",
                "핫아메리카노", "콜라", "사이다",
                "오렌지주스", "우유", "레몬에이드",
                "초코밀크쉐이크", "딸기밀크쉐이크"};
        
        hamburger_price = new int[] {3800, 2700, 3800, 7800,
                6900, 6500, 4800, 3600, 2000};
        chicken_price = new int[] {4400, 2400, 4400, 2300,
                2400, 13600, 18800, 9300, 8900};      
        dessert_price = new int[] {1000, 1700, 1000, 1500,
                1500, 2500, 2000, 2000, 2000}; 
        drink_price = new int[] {2000, 1500, 1000, 1000,
                2500, 1000, 2500, 2100, 2100};
        
        bhamburger = new JButton[hamburger_list.length];
        bchicken = new JButton[chicken_list.length];
        bdessert = new JButton[dessert_list.length];  
        bdrink = new JButton[drink_list.length];
        
        save_cat = "";
        save_good = "";
        save_price = "";
        save_sum = 0;
    }
    /**
     * 전체적인 레이아웃을 만드는 함수
     * 카테고리(햄버거, 치킨, 디저트, 드링크)별 세부 레이아웃은
     * smenu 카테고리 구분 오브젝트를 인자로 받아,
     * selectMenu(smenu, p_center) 함수를 호출하여 만든다.
     */
    void addLayout(Object smenu) {
    	// 프레임 객체 선언
        name_cat = new JTextField("카테고리", 11);
        name_good = new JTextField("상품", 12);
        name_price = new JTextField("가격", 12);
        name_sum = new JTextField("결제금액", 12);
        name_cat.setHorizontalAlignment(JTextField.CENTER);
        name_good.setHorizontalAlignment(JTextField.CENTER);
        name_price.setHorizontalAlignment(JTextField.CENTER);
        name_sum.setHorizontalAlignment(JTextField.CENTER);
        sel_cat = new JTextArea(10, 11);
        sel_good = new JTextArea(10, 12);
        sel_price = new JTextArea(10, 12);
        sum = new JTextArea(10, 12);
        pay = new JButton("결제하기");
        
        // 왼쪽 패널 설정
        JPanel p_left = new JPanel();
        p_left.setLayout(new GridLayout(4, 1));
        for (int i = 0; i < menu.length; i++) {
            p_left.add(bmenu[i]);
            bmenu[i].setPreferredSize(new Dimension(270, 45));
            bmenu[i].setFont(new Font("san-serif", Font.PLAIN, 40));
        }
        
        // 밑 패널 설정
        JPanel p_bottom = new JPanel();
        p_bottom.setLayout(new BorderLayout());
        JPanel nametext = new JPanel();
        nametext.setLayout(new BorderLayout());
        JPanel name = new JPanel();
        name.setLayout(new GridLayout(1, 4));
        name.add(name_cat);
        name.add(name_good);
        name.add(name_price);
        name.add(name_sum);
        JPanel text = new JPanel();
        text.setLayout(new GridLayout(1, 4));
        text.add(sel_cat);
        text.add(sel_good);
        text.add(sel_price);
        text.add(sum);
        nametext.add(name, BorderLayout.NORTH);
        nametext.add(text, BorderLayout.SOUTH);
        p_bottom.add(nametext, BorderLayout.CENTER);
        p_bottom.add(pay, BorderLayout.EAST);
        
        // 가운데 패널 설정
        JPanel p_center = new JPanel();
        p_center.setLayout(new GridLayout(3, 4));
        // selectMenu 함수를 실행하여 사용자가 선택한 카테고리의 레이아웃을 불러온다.
        selectMenu(smenu, p_center);
        
        // 글꼴 설정
        name_cat.setFont(new Font("san-serif", Font.PLAIN, 30));
        name_good.setFont(new Font("san-serif", Font.PLAIN, 30));
        name_price.setFont(new Font("san-serif", Font.PLAIN, 30));
        name_sum.setFont(new Font("san-serif", Font.PLAIN, 30));
        
        sel_cat.setFont(new Font("san-serif", Font.PLAIN, 25));
        sel_good.setFont(new Font("san-serif", Font.PLAIN, 25));
        sel_price.setFont(new Font("san-serif", Font.PLAIN, 25));
        sum.setFont(new Font("san-serif", Font.PLAIN, 25));
        pay.setFont(new Font("san-serif", Font.PLAIN, 50));
        
        // 프레임 영역
        f.setLayout(new BorderLayout());
        f.add(p_left, BorderLayout.WEST);
        f.add(p_center, BorderLayout.CENTER);
        f.add(p_bottom, BorderLayout.SOUTH);
        f.setSize(1650, 1000);
        f.setVisible(true);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    /**
     * addLayout() 함수로부터 호출된다.
     * 카테고리(햄버거, 치킨, 디저트, 드링크)별 세부 레이아웃을 구성하는 역할을 한다.
     */
    void selectMenu(Object smenu, JPanel p_center) {
        // 햄버거 카테고리에서 각각의 상품을 선택할 수 있는 버튼 생성
        for (int i = 0; i < hamburger_list.length; i++) {
            bhamburger[i] = new JButton("선택");
        }
        // 치킨 카테고리에서 각각의 상품을 선택할 수 있는 버튼 생성
        for (int i = 0; i < chicken_list.length; i++) {
            bchicken[i] = new JButton("선택");
        }
        // 디저트 카테고리에서 각각의 상품을 선택할 수 있는 버튼 생성
        for (int i = 0; i < dessert_list.length; i++) {
            bdessert[i] = new JButton("선택");
        }
        // 드링크 카테고리에서 각각의 상품을 선택할 수 있는 버튼 생성
        for (int i = 0; i < drink_list.length; i++) {
            bdrink[i] = new JButton("선택");
        }
        // 햄버거 카테고리 레이아웃 생성
        if (smenu == bmenu[0]) {
            for (int i = 0; i < hamburger_list.length; i++) {
                p_center.add(new JLabel(new ImageIcon("img/hamburger/h" + i + ".jpg")));
                JPanel j = new JPanel(new GridLayout(2,1));
                j.add(new JLabel(String.valueOf(hamburger_list[i]),
                        JLabel.CENTER)).setFont(new Font("san-serif",
                        Font.PLAIN, 23));
                j.add(new JLabel(String.valueOf(hamburger_price[i]),
                        JLabel.CENTER)).setFont(new Font("san-serif",
                        Font.PLAIN, 20));
                p_center.add(j);
                p_center.add(bhamburger[i]).setFont(new Font("san-serif",
                        Font.PLAIN, 20));
            }
            
        // 치킨 카테고리 레이아웃 생성
        } else if (smenu == bmenu[1]) {
            for (int i = 0; i < chicken_list.length; i++) {
                p_center.add(new JLabel(new ImageIcon("img/chicken/c" + i + ".jpg")));
                JPanel j = new JPanel(new GridLayout(2, 1));
                j.add(new JLabel(String.valueOf(chicken_list[i]),
                        JLabel.CENTER)).setFont(new Font("san-serif",
                        Font.PLAIN, 23));
                j.add(new JLabel(String.valueOf(chicken_price[i]),
                        JLabel.CENTER)).setFont(new Font("san-serif",
                        Font.PLAIN, 20));
                p_center.add(j);
                p_center.add(bchicken[i]).setFont(new Font("san-serif",
                        Font.PLAIN, 20));
            }
            
        // 디저트 카테고리 레이아웃 생성
        } else if (smenu == bmenu[2]) {
            for (int i = 0; i < dessert_list.length; i++) {
                p_center.add(new JLabel(new ImageIcon("img/dessert/d" + i + ".jpg")));
                JPanel j = new JPanel(new GridLayout(2,1));
                j.add(new JLabel(String.valueOf(dessert_list[i]),
                        JLabel.CENTER)).setFont(new Font("san-serif",
                        Font.PLAIN, 23));
                j.add(new JLabel(String.valueOf(dessert_price[i]),
                        JLabel.CENTER)).setFont(new Font("san-serif",
                        Font.PLAIN, 20));
                p_center.add(j);
                p_center.add(bdessert[i]).setFont(new Font("san-serif",
                        Font.PLAIN, 20));
            }
            
        // 드링크 카테고리 레이아웃 생성
        } else {
            for (int i = 0; i < drink_list.length; i++) {
                p_center.add(new JLabel(new ImageIcon("img/drink/k" + i + ".jpg")));
                JPanel j = new JPanel(new GridLayout(2,1));
                j.add(new JLabel(String.valueOf(drink_list[i]),
                        JLabel.CENTER)).setFont(new Font("san-serif",
                        Font.PLAIN, 23));
                j.add(new JLabel(String.valueOf(drink_price[i]),
                        JLabel.CENTER)).setFont(new Font("san-serif",
                        Font.PLAIN, 20));
                p_center.add(j);
                p_center.add(bdrink[i]).setFont(new Font("san-serif",
                        Font.PLAIN, 20));
            }
        }
    }
    
    void eventProc() {
        BtnHdlr bh = new BtnHdlr();
        // 카테고리(햄버거, 치킨, 디저트, 드링크) 선택 버튼 ActionListener 연결
        for (int i = 0; i < menu.length; i++) {
            bmenu[i].addActionListener(bh);
        }
        // 햄버거 카테고리의 각각의 상품 선택하는 버튼 ActionListener 연결
        for (int i = 0; i < hamburger_list.length; i++) {
            bhamburger[i].addActionListener(bh);
        }
        // 치킨 카테고리의 각각의 상품 선택하는 버튼 ActionListener 연결
        for (int i = 0; i < chicken_list.length; i++) {
            bchicken[i].addActionListener(bh);
        }
        // 디저트 카테고리의 각각의 상품 선택하는 버튼 ActionListener 연결
        for (int i = 0; i < dessert_list.length; i++) {
            bdessert[i].addActionListener(bh);
        }
        // 드링크 카테고리의 각각의 상품 선택하는 버튼 ActionListener 연결
        for (int i = 0; i < drink_list.length; i++) {
            bdrink[i].addActionListener(bh);
        }
        // 결제하기 버튼 ActionListener 연결
        pay.addActionListener(bh);
    }
    
    class BtnHdlr implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            Object evt = e.getSource();
            /*
             카테고리(햄버거, 치킨, 디저트, 드링크) 선택 버튼이 눌렸을 때,
             해당 카테고리 레이아웃을 불러온다.
             */
            if (evt.equals(bmenu[0]) | evt.equals(bmenu[1]) |
                    evt.equals(bmenu[2]) | evt.equals(bmenu[3])) {
                addLayout(evt);
                sel_cat.setText(save_cat);
                sel_good.setText(save_good);
                sel_price.setText(save_price);
                sum.setText(String.valueOf(save_sum) + " 원");
            }
            /*
             결제하기 버튼이 눌렸을 때 최종 결제금액이 맞는지 확인하는 메시지 창이 뜬 후,
             사용자가 확인버튼을 누르면 상품선택 상세 내용이 리셋된다.
             */
            if (evt.toString().equals(pay.toString())) {
                JOptionPane.showMessageDialog(null,
                        save_sum + "원 결제하시겠습니까?");
                save_cat = "";
                save_good = "";
                save_price = "";
                save_sum = 0;
                sel_cat.setText(save_cat);
                sel_good.setText(save_good);
                sel_price.setText(save_price);
                sum.setText("");
            }
            /*
             햄버거 카테고리의 각각의 상품 선택하는 버튼이 눌렸을 때,
             해당 카테고리, 상품명, 가격, 누적 결제금액을 TextArea에 출력한다.
             */
            for (int i = 0; i < bhamburger.length; i++) {
                if (evt.toString().equals(bhamburger[i].toString())) {
                    save_cat += "햄버거\n";
                    save_good += hamburger_list[i] + "\n";
                    save_price += String.valueOf(hamburger_price[i]) + " 원\n";
                    save_sum += hamburger_price[i];
                    sel_cat.setText(save_cat);
                    sel_good.setText(save_good);
                    sel_price.setText(save_price);
                    sum.setText(String.valueOf(save_sum) + " 원");
                }
            }
            /*
             치킨 카테고리의 각각의 상품 선택하는 버튼이 눌렸을 때,
             해당 카테고리, 상품명, 가격, 누적 결제금액을 TextArea에 출력한다.
             */
            for (int i = 0; i < bchicken.length; i++) {
                if (evt.toString().equals(bchicken[i].toString())) {
                    save_cat += "치킨\n";
                    save_good += chicken_list[i] + "\n";
                    save_price += String.valueOf(chicken_price[i]) + " 원\n";
                    save_sum += chicken_price[i];
                    sel_cat.setText(save_cat);
                    sel_good.setText(save_good);
                    sel_price.setText(save_price);
                    sum.setText(String.valueOf(save_sum) + " 원");
                }
            }
            /*
             디저트 카테고리의 각각의 상품 선택하는 버튼이 눌렸을 때,
             해당 카테고리, 상품명, 가격, 누적 결제금액을 TextArea에 출력한다.
             */
            for (int i = 0; i < bdessert.length; i++) {
                if (evt.toString().equals(bdessert[i].toString())) {
                    save_cat += "디저트\n";
                    save_good += dessert_list[i] + "\n";
                    save_price += String.valueOf(dessert_price[i]) + " 원\n";
                    save_sum += dessert_price[i];
                    sel_cat.setText(save_cat);
                    sel_good.setText(save_good);
                    sel_price.setText(save_price);
                    sum.setText(String.valueOf(save_sum) + " 원");
                }
            }
            /*
             드링크 카테고리의 각각의 상품 선택하는 버튼이 눌렸을 때,
             해당 카테고리, 상품명, 가격, 누적 결제금액을 TextArea에 출력한다.
             */
            for (int i = 0; i < bdrink.length; i++) {
                if (evt.toString().equals(bdrink[i].toString())) {
                    save_cat += "드링크\n";
                    save_good += drink_list[i] + "\n";
                    save_price += String.valueOf(drink_price[i]) + " 원\n";
                    save_sum += drink_price[i];
                    sel_cat.setText(save_cat);
                    sel_good.setText(save_good);
                    sel_price.setText(save_price);
                    sum.setText(String.valueOf(save_sum) + " 원");
                }
            }
        }
    }
    
    public static void main(String[] args) {
        MenuTable table = new MenuTable();
        table.addLayout("drink");
        table.eventProc();
    }
}
~~~