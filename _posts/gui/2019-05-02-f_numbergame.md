---
layout: post
title: numbergame
category: gui
tags: [java, gui, numbergame]
comments: false
---

# [numbergame]()

## NumberGame
~~~java
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
class MyFrame extends JFrame implements ActionListener{
	int getsu = 4;
	JButton[][] la = new JButton[getsu][getsu];
	char[][] answer = new char[getsu][getsu];
	// 첫번째 버튼
	JButton firstClick;
	int firstRow, firstCol;
	public MyFrame() {
		// 1. 객체 생성
		// 2. 화면 붙이기 및 출력
		// 4. 이벤트 등록
		setLayout(new GridLayout(getsu, getsu));
		for(int i = 0; i < la.length; i++) {
			for(int j = 0; j < la[i].length; j++) {
				la[i][j] = new JButton();
				add(la[i][j]);
				la[i][j].addActionListener(this);
				answer[i][j] = '0'; // 문자초기화
			}
		}
		setSize(400, 400);
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	// answer에 각각의 값 각 버튼을 지정
	void initChar() {
		char alpha = '0';
		DASI :
		for(int i = 0; i < getsu * getsu; ) {
			// 임의의 알파벳 만들기
			if(i % 2 == 0) {
				alpha = (char)('A' + (int)(Math.random() * 26));
				for(int row = 0; row < answer.length; row++) {
					for(int col = 0; col<answer.length; col++) {
						if(answer[row][col] == alpha) {
							continue DASI;
						}
					}
				}
			}
			// 임의의 자리에 알파벳 넣기
			boolean ok = false;
			do {
				int row = (int)(Math.random()*getsu);
				int col = (int)(Math.random()*getsu);
				if(answer[row][col] == '0') {
					answer[row][col] = alpha;
					i++;
					ok = true;
				}
			}while(!ok);
		}
	}
	void showAnswer() {
		for(int i = 0; i < answer.length; i++) {
			for(int j = 0; j < answer[i].length; j++) {
				la[i][j].setText(String.valueOf(answer[i][j]));
			}
		}
		try {
		Thread.sleep(5000);
		}catch(Exception ex) {}
		for(int i = 0; i < answer.length; i++) {
			for(int j = 0; j < answer[i].length; j++) {
				la[i][j].setText(null);
			}
		}
	}
	public void actionPerformed(ActionEvent e) {
		// 5. 이벤트 확인
//		System.out.println("버튼이벤트발생");
		JButton obj = (JButton)e.getSource(); // obj는 넣은 객체를 확인하기위하여
		for(int i = 0; i < answer.length; i++) {
			for(int j = 0; j < answer.length; j++) {
				if(obj == la[i][j]) {
					// 첫번째 버튼인지
					if(firstClick == null) {
						firstClick = obj;
						firstRow = i;
						firstCol = j;
//						firstClick.setBackground(new Color(255, 0, 0)); // red/green/blue 색깔넣고싶을때
					}else {
					// 두번째 버튼인지
						if(answer[firstRow][firstCol] == answer[i][j]) {
							la[firstRow][firstCol].setText(String.valueOf(answer[firstRow][firstCol]));
							la[i][j].setText(String.valueOf(answer[i][j]));
						}else {
							firstClick.setBackground(null);
						}
						firstClick = null;
					}
				}
			}
		}
	}
}
public class NumberGame {
	public static void main(String[] args) {
		MyFrame f = new MyFrame();
		f.initChar();
		f.showAnswer();
	}
}
~~~