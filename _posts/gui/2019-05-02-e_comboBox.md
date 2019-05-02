---
layout: post
title: comboBox
category: gui
tags: [java, gui, comboBox]
comments: false
---

# [comboBox]()

## CalendarEx
~~~java
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;
public class CalendarEx {
	// 1. 멤버 변수 선언
	JFrame f;
	JComboBox cbY, cbM, cbD;
	JButton b;
	JLabel la;
	int[] lastDays = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	// 2. 멤버 변수 객체 선언
	CalendarEx() {
		f = new JFrame("콤보박스");
		// 년 : 2015 ~ 2025
		// 월 : 1 ~ 12
		Integer[] ysu = new Integer[11];
		for(int i = 0, year = 2015; i < ysu.length; i++, year++) {
			ysu[i] = year;
 		}
		Integer[] msu = new Integer[12];
		for(int i = 0; i < msu.length; i++) {
			msu[i] = i + 1;
		}
		
		cbY = new JComboBox(ysu);
		cbM = new JComboBox(msu);
		cbD = new JComboBox();
		b = new JButton("▶");
		la = new JLabel("요일");
	}
	// 3. 화면 붙이기 및 화면보이기
	void addLayout() {
		f.setLayout(new FlowLayout());
		f.add(cbY);
		f.add(new JLabel("년"));
		f.add(cbM);
		f.add(new JLabel("월"));
		f.add(cbD);
		f.add(new JLabel("일"));
		f.add(b);
		f.add(la);
		// 프레임 영역
		f.setSize(400, 280);
		f.setVisible(true);
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	void initDate() {
		Calendar c = Calendar.getInstance();
		int y = c.get(Calendar.YEAR);
		int m = c.get(Calendar.MONTH) + 1;
		int d = c.get(Calendar.DATE);
		cbY.setSelectedItem(y);
		cbM.setSelectedItem(m);
		setDay(); // 일
		cbD.setSelectedItem(d);
		setDate(); // 요일
		
	}
	// 4. 이벤트 등록 및 처리
	void eventProc() {
		CbHdlr cb = new CbHdlr();
		cbY.addActionListener(cb);
		cbM.addActionListener(cb);
		b.addActionListener(cb);
	}
	class CbHdlr implements ActionListener{
		public void actionPerformed(ActionEvent e) {
			Object obj = e.getSource(); // 눌려진것의 객체값
			if(obj == cbY | obj == cbM) setDay();
			else if(obj == b) setDate();
		}
	}
	void setDay() {
//		System.out.println("콤보박스이벤트");
		// 윤년이라면 lastDays[1] = 29로 지정
		// 평년이라면 lastDays[1] = 28일로 지정
		// [확인] 2016 - 2 윤년입니다
		int year = (Integer)cbY.getSelectedItem();
		if((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
			lastDays[1] = 29;
		}else{
			lastDays[1] = 28;
		}
		// 월 마다 일 수 변경
		int month = cbM.getSelectedIndex();
		cbD.removeAllItems();
		for(int i = 1; i <= lastDays[month]; i++) {
			cbD.addItem(i);
		}
	}
	void setDate() {
//		System.out.println("버튼이벤트");
		// (1) 버튼을 누르면 해당 요일출력
		// (2) 처음화면 뜰때 오늘 날짜로 지정
		// 사용자가 선택한 년/월/일 값 얻어오기
		int y = (Integer)cbY.getSelectedItem();
		int m = (Integer)cbM.getSelectedItem(); // 5월
		int d = (Integer)cbD.getSelectedItem();
		Calendar c = Calendar.getInstance();
		c.set(y, m - 1, d); // 월은 1을 빼줘야 한다
		int date = c.get(Calendar.DAY_OF_WEEK);
		String[] strDate = {"일", "월", "화", "수", "목", "금", "토"};
		la.setText(strDate[date - 1]);
	}
	public static void main(String[] args) {
		CalendarEx c = new CalendarEx();
		c.addLayout(); // 화면 붙이기 및 출력
		c.initDate(); // 날짜 초기화
		c.eventProc(); // 이벤트 처리
	}
}
~~~