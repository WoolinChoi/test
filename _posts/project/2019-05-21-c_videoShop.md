---
layout: post
title: videoShop
category: project
tags: [java, project, videoShop]
comments: false
---

# [videoShop]()

## VideoShop extends JFrame
~~~java
import java.awt.*;
import javax.swing.*;
import view.CustomerView;
import view.RentView;
import view.VideoView;
public class VideoShop extends JFrame {
	CustomerView	customer;
	VideoView		video;
	RentView		rent;

	public VideoShop() {
		//각각의 화면을 관리하는 클래스 객체 생성
			customer	= new CustomerView();
			video		= new VideoView();
			rent		= new RentView();

			JTabbedPane  pane = new JTabbedPane();
			pane.addTab("고객관리", customer);
			pane.addTab("비디오관리", video);
			pane.addTab("대여관리", rent);

//			pane.setSelectedIndex(2);

			// 화면크기지정
			add("Center", pane);
			setSize(800,600);
			setVisible(true);

			setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);	
	}
	public static void main(String[] args) {
			new VideoShop();
	}
}
~~~

## CustomerDao
~~~java
import model.vo.Customer;
/** 고객관리 JDBC 연결 */
public interface CustomerDao {
	public void insertCustomer(Customer vo) throws Exception;		// 회원가입
	public Customer selectByTel(String tel) throws Exception;		// 전화번호로 검색
	public int updateCustomer(Customer vo) throws Exception;		// 고객정보 수정
}
~~~

## CustomerModel implements CustomerDao
~~~java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import model.CustomerDao;
import model.vo.Customer;
public class CustomerModel implements CustomerDao {
	String driver = "oracle.jdbc.driver.OracleDriver";
	String url = "jdbc:oracle:thin:@192.168.0.114:1521:orcl";
	String user = "ourjo7";
	String pass = "1234";
	Connection con = null;
	public CustomerModel() throws Exception {
	 	// 1. 드라이버로딩
		Class.forName(driver);
	}
	
	// 회원가입
	public void insertCustomer(Customer vo) throws Exception {
		// 2. Connection 연결객체 얻어오기
		con = DriverManager.getConnection(url, user, pass);
		System.out.println("연결성공");
		
		// 3. sql 문장 만들기
		String sql = "INSERT INTO customer_management(phonenumber, name, additionalnumber, address, email) "
				+ "VALUES(?, ?, ?, ?, ?)";
		System.out.println(sql);
		
		// 4. sql 전송객체 (PreparedStatement)	
		PreparedStatement st = con.prepareStatement(sql);
		st.setString(1, vo.getCustTel1());
		st.setString(2, vo.getCustName());
		st.setString(3, vo.getCustTel2());
		st.setString(4, vo.getCustAddr());
		st.setString(5, vo.getCustEmail());
		
		// 5. sql 전송
		st.executeUpdate();
		
		// 6. 닫기 
		st.close();
		con.close();
	}
	
	// 전화번호로 검색
	public Customer selectByTel(String tel) throws Exception {
		Connection con = null;
		PreparedStatement st = null;
		ResultSet rs = null;
		try {
			// 연결 객체 얻어오기
			con = DriverManager.getConnection(url, user, pass);
				
			// sql 문장 만들기
			String sql = "SELECT * FROM customer_management WHERE phonenumber = ?";
				
			// sql 전송 객체 얻어오기
			st = con.prepareStatement(sql);
			st.setString(1, tel);
			
			// sql 전송
			rs = st.executeQuery();
			
			Customer vo = new Customer();
			// 결과 처리
			if(rs.next()) {
				vo.setCustTel1(rs.getString("PHONENUMBER"));
				vo.setCustName(rs.getString("NAME"));
				vo.setCustTel2(rs.getString("ADDITIONALNUMBER"));
				vo.setCustAddr(rs.getString("ADDRESS"));
				vo.setCustEmail(rs.getString("EMAIL"));
			}
			return vo;
		}finally {
		// 닫기 : finally에 넣어준다.
		st.close();
		rs.close();
		st.close();
		con.close();
		}
	}
	
	// 회원수정	
	public int updateCustomer(Customer vo) throws Exception {
		int result = 0;
		// 2. Connection 연결객체 얻어오기
		con = DriverManager.getConnection(url, user, pass);
		System.out.println("연결성공");
			
		// 3. sql 문장 만들기
		String sql = "UPDATE customer_management "
				+ "SET phonenumber = ?, name = ?, additionalnumber = ?, address = ?, email = ? "
				+ "WHERE phonenumber = ?";
		System.out.println(sql);
		
		// 4. sql 전송객체 (PreparedStatement)	
		PreparedStatement st = con.prepareStatement(sql);
		st.setString(1, vo.getCustTel1());
		st.setString(2, vo.getCustName());
		st.setString(3, vo.getCustTel2());
		st.setString(4, vo.getCustAddr());
		st.setString(5, vo.getCustEmail());
		st.setString(6, vo.getCustTel1());
				
		// 5. sql 전송
		st.executeUpdate();
				
		// 6. 닫기 
		st.close();
		con.close();
		return result;
	}
}
~~~

## Customer
~~~java
public class Customer {
	String custName;		// 고객명
	String custTel1;		// 전화번호
	String custTel2;		// 보조 전화번호
	String custAddr;		// 주소
	String custEmail;		// 이메일

	public String getCustName() {
		return custName;
	}
	
	public void setCustName(String custName) {
		this.custName = custName;
	}
	
	public String getCustTel1() {
		return custTel1;
	}
	
	public void setCustTel1(String custTel1) {
		this.custTel1 = custTel1;
	}
	
	public String getCustTel2() {
		return custTel2;
	}
	
	public void setCustTel2(String custTel2) {
		this.custTel2 = custTel2;
	}
	
	public String getCustAddr() {
		return custAddr;
	}
	
	public void setCustAddr(String custAddr) {
		this.custAddr = custAddr;
	}
	
	public String getCustEmail() {
		return custEmail;
	}
	
	public void setCustEmail(String custEmail) {
		this.custEmail = custEmail;
	}
}
~~~

## CustomerView extends JPanel
~~~java
import java.awt.BorderLayout;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import model.CustomerDao;
import model.dao.CustomerModel;
import model.vo.Customer;
public class CustomerView extends JPanel {
	JTextField	tfCustName, tfCustTel,  tfCustTelAid, tfCustAddr, tfCustEmail;
	JButton		bCustRegist, bCustModify;
	
	JTextField  tfCustNameSearch,  tfCustTelSearch;
	JButton		bCustNameSearch,  bCustTelSearch;
	
	// 변수
	CustomerDao dao;

	
	public CustomerView() {
		addLayout();
		connectDB();
		eventProc();
	}
	
	public void eventProc() {
		ButtonEventHandler btnHandler = new ButtonEventHandler();
		
		// 이벤트 등록
		bCustRegist.addActionListener(btnHandler);
		bCustModify.addActionListener(btnHandler);
		bCustNameSearch.addActionListener(btnHandler);
		bCustTelSearch.addActionListener(btnHandler);
	}
	
	// 버튼 이벤트 핸들러 만들기
	class ButtonEventHandler implements ActionListener {
		public void actionPerformed(ActionEvent ev) {
			Object o = ev.getSource();
			
			if(o == bCustRegist) {  
				registCustomer();  // 회원등록
			}
			else if(o == bCustModify) {  
				updateCustomer();  // 회원정보수정
			}			
			else  if(o == bCustTelSearch) { 
				searchByTel();      // 전화번호 검색
			}
			else if(o == bCustNameSearch) {  // 이름검색
				System.out.println("이름검색");
			}
		}
	}
	
	// 회원가입하는 메소드
	public void registCustomer() {
		// 1. 화면 텍스트필드의 입력값 얻어오기			
		// 2. 1값들을 Customer 클래스의 멤버로지정			
		// 3. Model 클래스 안에 insertCustomer () 메소드 호출하여 2번 VO 객체를 넘김
		// 4. 화면 초기화
		Customer vo = new Customer();
		vo.setCustTel1(tfCustName.getText());
		vo.setCustName(tfCustTel.getText());
		vo.setCustTel2(tfCustTelAid.getText());
		vo.setCustAddr(tfCustAddr.getText());
		vo.setCustEmail(tfCustEmail.getText());
		try {
			dao.insertCustomer(vo);
			clearTextField();
		}catch (Exception ex) {
			ex.printStackTrace();
		}		
	}
	void clearTextField() {
		tfCustName.setText(null);
		tfCustTel.setText(null);
		tfCustTelAid.setText(null);
		tfCustAddr.setText(null);
		tfCustEmail.setText(null);
	}
	
	
	// 전화번호에 의한 검색
	public void searchByTel() {
		// 1. 입력한 전화번호 얻어오기
		// 2. Model의 전화번호 검색메소드 selectByTel()  호출
		// 3. 2번의 넘겨받은 Customer의 각각의 값을 화면 텍스트 필드 지정
//		JOptionPane.showMessageDialog(null, "검색");
		String tel = tfCustTelSearch.getText();
		try {
			Customer vo = dao.selectByTel(tel);
			tfCustTel.setText(vo.getCustTel1());
			tfCustName.setText(vo.getCustName());
			tfCustTelAid.setText(vo.getCustTel2());
			tfCustAddr.setText(vo.getCustAddr());
			tfCustEmail.setText(vo.getCustEmail());
		}catch (Exception ex) {
			ex.printStackTrace();
		}
	}
	
	// 회원정보수정
	public void updateCustomer() {
//		JOptionPane.showMessageDialog(null, "수정");
		Customer vo = new Customer();
		vo.setCustTel1(tfCustName.getText());
		vo.setCustName(tfCustTel.getText());
		vo.setCustTel2(tfCustTelAid.getText());
		vo.setCustAddr(tfCustAddr.getText());
		vo.setCustEmail(tfCustEmail.getText());
		try {
			dao.updateCustomer(vo);
		}catch (Exception ex) {
			ex.printStackTrace();
		}

	}
	
	public void connectDB() {
		try {
			dao = new CustomerModel();
		}catch (Exception ex) {
			JOptionPane.showMessageDialog(null, "드라이버 오류 : " + ex.getMessage());
		}
	}
	
	public void addLayout() {
		
		tfCustName			= new JTextField(20);
		tfCustTel			= new JTextField(20);
		tfCustTelAid		= new JTextField(20);
		tfCustAddr			= new JTextField(20);
		tfCustEmail			= new JTextField(20);


		tfCustNameSearch	= new JTextField(20);
		tfCustTelSearch		= new JTextField(20);

		bCustRegist			= new JButton("회원가입");
		bCustModify			= new JButton("회원수정");
		bCustNameSearch		= new JButton("이름검색");
		bCustTelSearch		= new JButton("번호검색");

		// 회원가입 부분 붙이기 
		// ( 그 복잡하다던 GridBagLayout을 사용해서 복잡해 보임..다른 쉬운것으로...대치 가능 )
		JPanel			pRegist = new JPanel();
		pRegist.setLayout(new GridBagLayout());
		GridBagConstraints cbc = new GridBagConstraints();
		cbc.weightx	= 1.0;
		cbc.weighty	= 1.0;
		cbc.fill = GridBagConstraints.BOTH;
		
		cbc.gridx = 0; 
		cbc.gridy = 0; 
		cbc.gridwidth = 1; 
		cbc.gridheight = 1;
		pRegist.add(new JLabel("	이	름	"),	cbc);
		
		cbc.gridx = 1;	 			
		cbc.gridy = 0;			
		cbc.gridwidth = 1;			
		cbc.gridheight = 1;
		pRegist.add(tfCustName , cbc);
		
		cbc.gridx = 2;	 			
		cbc.gridy = 0;			
		cbc.gridwidth = 1;			
		cbc.gridheight = 1;
		pRegist.add(bCustModify, cbc);
		
		cbc.gridx = 3;	 			
		cbc.gridy = 0;			
		cbc.gridwidth = 1;			
		cbc.gridheight = 1;
		pRegist.add(bCustRegist, cbc);

		cbc.gridx = 0;	 			
		cbc.gridy = 1;			
		cbc.gridwidth = 1;			
		cbc.gridheight = 1;
		pRegist.add(new JLabel("	전	화	"),	cbc);
		
		cbc.gridx = 1;	 			
		cbc.gridy = 1;			
		cbc.gridwidth = 1;			
		cbc.gridheight = 1;
		pRegist.add(tfCustTel,	cbc);
		
		cbc.gridx = 2;	 			
		cbc.gridy = 1;			
		cbc.gridwidth = 1;			
		cbc.gridheight = 1;
		pRegist.add(new JLabel(" 추가전화  "),	cbc);
		
		cbc.gridx = 3;	 			
		cbc.gridy = 1;			
		cbc.gridwidth = 1;			
		cbc.gridheight = 1;
		pRegist.add(tfCustTelAid,	cbc);

		cbc.gridx = 0;	 			
		cbc.gridy = 2;			
		cbc.gridwidth = 1;			
		cbc.gridheight = 1;
		pRegist.add(new JLabel("	주	소	"),	cbc);
		
		cbc.gridx = 1;	 			
		cbc.gridy = 2;			
		cbc.gridwidth = 3;			
		cbc.gridheight = 1;
		pRegist.add(tfCustAddr,	cbc);

		cbc.gridx =	0;	 			
		cbc.gridy = 3;			
		cbc.gridwidth =	1;			
		cbc.gridheight = 1;
		pRegist.add(new JLabel("	이메일	"),	cbc);
		
		cbc.gridx =	1;	 			
		cbc.gridy = 3;			
		cbc.gridwidth =	3;			
		cbc.gridheight = 1;
		pRegist.add(tfCustEmail, cbc);

		// 회원검색 부분 붙이기
		JPanel pSearch = new JPanel();
		pSearch.setLayout(new GridLayout(2, 1));
				JPanel pSearchName = new JPanel();
				pSearchName.add(new JLabel("	이 	름	"));
				pSearchName.add(tfCustNameSearch);
				pSearchName.add(bCustNameSearch);
				JPanel pSearchTel = new JPanel();
				pSearchTel.add(new JLabel("	전화번호	"));
				pSearchTel.add(tfCustTelSearch);
				pSearchTel.add(bCustTelSearch);
		pSearch.add(pSearchName);
		pSearch.add(pSearchTel);

		// 전체 패널에 붙이기
		setLayout(new BorderLayout());
		add("Center", pRegist);
		add("South", pSearch);	
	}
}			 	
~~~