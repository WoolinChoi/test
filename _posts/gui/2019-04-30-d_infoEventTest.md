---
layout: post
title: infoEventTest
category: git
tags: [java, gui, infoEventTest]
comments: false
---

# [infoEventTest]()

## InfoEvtTest
~~~java
/*
 * 기본창에 이벤트 넣기
 */
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import javax.swing.*;
public class InfoEvtTest {
	// 1. 멤버 변수 선언
	JFrame f;
	JButton bAdd, bShow, bSearch, bDelete, bCancel, bExit;
	JTextArea ta;
	JTextField tfName, tfId, tfTel, tfGender, tfAge, tfHome;
	ArrayList<Person> list = new ArrayList<Person>();
	// 2. 멤버 객체 생성
	InfoEvtTest() {
		f = new JFrame("DBTest");
		bAdd = new JButton("Add");
		bShow = new JButton("Show");
		bSearch = new JButton("Search");
		bDelete = new JButton("Delete");
		bCancel = new JButton("Cancel");
		bExit = new JButton("Exit");
		ta = new JTextArea();
		tfName = new JTextField(15);
		tfId = new JTextField();
		tfTel = new JTextField();
		tfGender = new JTextField();
		tfAge = new JTextField();
		tfHome = new JTextField();
	}
	// 3. 화면 붙이기 및 화면 출력
	void addLayout() {
		// South 영역
		JPanel p_south = new JPanel();
		p_south.setLayout(new GridLayout(1, 6));
		p_south.add(bAdd);
		p_south.add(bShow);
		p_south.add(bSearch);
		p_south.add(bDelete);
		p_south.add(bCancel);
		p_south.add(bExit);
		// West 영역
		JPanel p_west = new JPanel();
		p_west.setLayout(new GridLayout(6, 2));
		p_west.add(new JLabel("Name"));
		p_west.add(tfName);
		p_west.add(new JLabel("ID"));
		p_west.add(tfId);
		p_west.add(new JLabel("Tel"));
		p_west.add(tfTel);
		p_west.add(new JLabel("Gender"));
		p_west.add(tfGender);
		p_west.add(new JLabel("Age"));
		p_west.add(tfAge);
		p_west.add(new JLabel("Home"));
		p_west.add(tfHome);
		// 프레임영역에 붙이기
		f.setLayout(new BorderLayout());
		f.add(p_south, BorderLayout.SOUTH);
		f.add(p_west, BorderLayout.WEST);
		f.add(ta, BorderLayout.CENTER);
		f.setSize(900, 500);
		f.setVisible(true);
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	// 이벤트 등록
	void eventProc() {
		BtnHdlr bh = new BtnHdlr();
		// 버튼과 이벤트핸들러 연결
		bAdd.addActionListener(bh);
		bShow.addActionListener(bh);
		bSearch.addActionListener(bh);
		bDelete.addActionListener(bh);
		bCancel.addActionListener(bh);
		bExit.addActionListener(bh);
		// 전화번호 텍스트필드 엔터 이벤트
		tfTel.addActionListener(new TfHdlr());
		// 주민번호 텍스트필드 포커스 이벤트
		tfId.addFocusListener(new IdFocus());
	}
//	class IdFocus implements FocusListener {
	class IdFocus extends FocusAdapter {
		public void focusGained(FocusEvent e) {}
		public void focusLost(FocusEvent e) {
			System.out.println("포커스잃음");
			// "12345678-1234567"
			String id = tfId.getText();
			char sung = id.charAt(7);
			if(sung == '1' || sung == '3') tfGender.setText("남자");
			else tfGender.setText("여자");
			// 출신지 입력
			char h = id.charAt(8); 
			switch(h) {
			case '0' : tfHome.setText("서울"); break;
			case '1' : tfHome.setText("인천"); break;
			case '2' : tfHome.setText("경기"); break;
			default : tfHome.setText("외국인");  
			}
			// 나이 출력
			String nai1 = id.substring(0, 2);
			int nai2 = Integer.parseInt(nai1);
			int age = 0;
			Calendar cal = Calendar.getInstance();
			int year = cal.get(Calendar.YEAR);
			if(sung == '1' || sung == '2') {
				age = year - (1900 + nai2) + 1;
				tfAge.setText(String.valueOf(age));
			}else if(sung == '3' || sung == '4') {
				age = year - (2000 + nai2) + 1;
				tfAge.setText(String.valueOf(age));
			}
		}
	}
	class BtnHdlr implements ActionListener {
		public void actionPerformed(ActionEvent e) {
			System.out.println("버튼이벤트");
			Object evt = e.getSource();
			if(evt == bAdd) {
				insert();
				clearTextField();
			}else if(evt == bShow) {
				showInfo();
			}else if(evt == bSearch) {
				searchTel();
			}else if(evt == bDelete) {
				delete();
			}else if(evt == bCancel) {
				clearTextField();
			}else if(evt == bExit) {
				exit();
			}
		}
	}
	class TfHdlr implements ActionListener {
		public void actionPerformed(ActionEvent e) {
			searchTel();
		}
	}
	// 검색
	void searchTel() {
		System.out.println("전화번호이벤트");
		// (1) 사용자가 입력한 전화번호 얻어오기
		// (2) ArrayList의 각 Person의 tel과 비교해서 같은지
		// (3) 해당 Person의 멤버값들을 각각 텍스트필드에 출력
		String tel = tfTel.getText();
		for(Person p : list) {
			if(p.getTel().equals(tel)) {
				tfName.setText(p.getName());
				tfId.setText(p.getId());
				tfTel.setText(p.getTel());
				tfGender.setText(p.getGender());
				tfAge.setText(String.valueOf(p.getAge()));
				tfHome.setText(p.getHome());
			}
		}
	}
	// 삭제
	void delete() {
			System.out.println("삭제이벤트");
			// (1) 사용자가 입력한 전화번호 얻어오기
			// (2) ArrayList의 각 Person의 tel과 비교해서 같은지
			// (3) 해당 Person의 멤버값들을 삭제
			String tel = tfTel.getText();
			for(Person p : list) {
				if(p.getTel().equals(tel)) {
					list.remove(p);
				}
			}
			clearTextField();
			showInfo();
	}
	// 취소
	void clearTextField() {
		tfName.setText(null);
		tfId.setText(null);
		tfTel.setText(null);
		tfGender.setText(null);
		tfAge.setText(null);
		tfHome.setText(null);
	}
	// 전체보기
	void showInfo() {
		ta.setText("--------------전체보기--------------\n\n");
		for(Person p : list) {
			ta.append(p.toString());
		}
	}
	void exit() {
		int result = JOptionPane.showConfirmDialog(null,"정말로 나가겠습니까");
		// 종료버튼이 눌렸을 때 강제프로그램 종료(System.exit(0);)
		if(result == JOptionPane.OK_OPTION) {
			System.exit(0);	
		}
	}
	// 입력 
	void insert() {
		// (1) 각 텍스트필드의 입력값을 얻어오기
		// (2) (1)에서 얻어온 값들을 Person 멤버지정(생성자/setter)
		// (3) ArrayList에 (2)객체를 추가
		Person p = new Person();
		p.setName(tfName.getText());
		p.setId(tfId.getText());
		p.setTel(tfTel.getText());
		p.setGender(tfGender.getText());
		p.setAge(Integer.parseInt(tfAge.getText()));
		p.setHome(tfHome.getText());
		list.add(p);
	}
	public static void main(String[] args) {
		InfoEvtTest it = new InfoEvtTest();
		it.addLayout();
		it.eventProc();
	}
}
~~~

## Person extends Object
~~~java
public class Person extends Object {
	// 변수
	private String name;
	private String id;
	private String tel;
	private String gender;
	private int age;
	private String home;
	// 생성자 함수
	public Person() {}
	public Person(String name, String id, String tel, String gender, int age, String home) {
		super();
		this.name = name;
		this.id = id;
		this.tel = tel;
		this.gender = gender;
		this.age = age;
		this.home = home;
	}
	// 값만 빼주기 위해 toString
	public String toString() {
		return name + "\t" + id + "\t" + tel + "\t" + gender + "\t" + age + "\t" + home + "\n"; 
	}
	// setter/getter
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getTel() {
		return tel;
	}
	public void setTel(String tel) {
		this.tel = tel;
	}
	public String getGender() {
		return gender;
	}
	public void setGender(String gender) {
		this.gender = gender;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public String getHome() {
		return home;
	}
	public void setHome(String home) {
		this.home = home;
	}
}
~~~

## InfoEvtTest2
~~~java
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class InfoEvtTest2 {
	// 1. 멤버 변수 선언
	JFrame f;
	JButton bAdd, bShow, bSearch, bDelete, bCancel, bExit;
	JTextArea ta;
	JTextField tfName, tfId, tfTel, tfSex, tfAge, tfHome;
	// 2. 멤버 객체 생성
	InfoEvtTest3() {
		f = new JFrame("DBTest");
		bAdd = new JButton("Add");
		bShow = new JButton("Show");
		bSearch = new JButton("Search");
		bDelete = new JButton("Delete");
		bCancel = new JButton("Cancel");
		bExit = new JButton("Exit");
		ta = new JTextArea();
		tfName = new JTextField(15);
		tfId = new JTextField();
		tfTel = new JTextField();
		tfSex = new JTextField();
		tfAge = new JTextField();
		tfHome = new JTextField();
	}
	// 3. 화면 붙이기 및 화면 출력
	void addLayout() {
		// South 영역
		JPanel p_south = new JPanel();
		p_south.setLayout(new GridLayout(1, 6));
		p_south.add(bAdd);
		p_south.add(bShow);
		p_south.add(bSearch);
		p_south.add(bDelete);
		p_south.add(bCancel);
		p_south.add(bExit);
		// West 영역
		JPanel p_west = new JPanel();
		p_west.setLayout(new GridLayout(6, 2));
		p_west.add(new JLabel("Name"));
		p_west.add(tfName);
		p_west.add(new JLabel("ID"));
		p_west.add(tfId);
		p_west.add(new JLabel("Tel"));
		p_west.add(tfTel);
		p_west.add(new JLabel("Sex"));
		p_west.add(tfSex);
		p_west.add(new JLabel("Age"));
		p_west.add(tfAge);
		p_west.add(new JLabel("Home"));
		p_west.add(tfHome);
		// 프레임영역에 붙이기
		f.setLayout(new BorderLayout());
		f.add(p_south, BorderLayout.SOUTH);
		f.add(p_west, BorderLayout.WEST);
		f.add(ta, BorderLayout.CENTER);
		f.setSize(700, 500);
		f.setVisible(true);
	}
	void eventProc() {
		// 만든 이벤트 핸들러를 메모리에 올리기
		MyHdlr mh = new MyHdlr();
		// 이벤트핸들러랑 버튼 연결하기
		bExit.addMouseListener(mh);
	}
	// 이벤트 핸들러 만들기
//	class MyHdlr implements MouseListener {
	class MyHdlr extends MouseAdapter { // 메소드가 2개이상일 때 Adapter를 쓰면 편하다
		public void mouseClicked(MouseEvent e) {
			Object obj = e.getSource(); // 눌려진애
			if(obj == bExit) {
				System.exit(0);
			}
		}
	}
	public static void main(String[] args) {
		InfoEvtTest3 it = new InfoEvtTest3();
		it.addLayout();
		it.eventProc();
	}
}
~~~