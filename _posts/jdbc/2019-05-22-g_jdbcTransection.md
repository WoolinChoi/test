---
layout: post
title: jdbcTransection
category: jdbc
tags: [java, jdbc, jdbcTransection]
comments: false
---

# [jdbcTransection]()

## AccLogic
~~~java
import java.sql.*;
import javax.swing.JOptionPane;
public class AccLogic {
	// 연결 객체 생성시 필요한 변수 선언
	String url;
	String user;
	String pass;

	//===============================================
	// 드라이버를 드라이버매니저에 등록
	public AccLogic() throws Exception {
		/////////////////////////////////////////////////////////
		// 1. 드라이버를 드라이버 매니저에 등록
		Class.forName("oracle.jdbc.driver.OracleDriver");
		url = "jdbc:oracle:thin:@192.168.0.114:1521:orcl";
		user = "scott";
		pass = "tiger";
	}

	//====================================================
	// 보내는 계좌번호와 받는 계좌번호와 계좌금액을 넘겨받아 
	// 보내는계좌에서 계좌금액을 빼고 받는계좌에서 계좌금액을 더한다
	public int moveAccount(String sendAcc, String recvAcc, int amount) throws Exception {
		Connection con = null;
		PreparedStatement st1 = null;
		PreparedStatement st2 = null;
		try {
			///////////////////////////////////////////////////////////
			//	 1. Connection 객체 생성
			con = DriverManager.getConnection(url, user, pass);
			System.out.println("연결성공");
			
			//@@ 2. Auto-commit을 해제
			con.setAutoCommit(false);
			
			//	 3. 출금계좌에서 이체금액을 뺀다
			String sql1 = "UPDATE account SET amount = (amount - ?) WHERE account_num = ?";
			
			st1 = con.prepareStatement(sql1);
			st1.setInt(1, amount);
			st1.setString(2, sendAcc);
			
			int re1 = st1.executeUpdate();
			if(re1 != 1) {
				con.rollback();
				return -1;
			}
			
			//	 4. 입금계좌에 이체금액을 더한다
			String sql2 = "UPDATE account SET amount = (amount + ?) WHERE account_num = ?";
			
			st2 = con.prepareStatement(sql2);
			st2.setInt(1, amount);
			st2.setString(2, recvAcc);
			
			int re2 = st2.executeUpdate();
			if(re2 != 1) {
				con.rollback();
				return -1;
			}
			
			//@@ 5. commit을 전송한다
			con.commit();
			
			// 6. 객체 닫기
			st1.close();
			st2.close();
			con.close();
		
		// - 만일 정상적인 경우는 0을 리턴하고 도중에 잘못되었으면 트랜잭션을 롤백시키고 -1을 리턴 
		}catch(Exception Ex) {
			try{
				con.rollback();
			} catch(Exception ex) {}
			return -1;
		}
		return 0;
	}
~~~

## AccUI implements ActionListener
~~~java
package jdbc.transection;

/******************************************************
*  @ 트랙잭션 예제
*/
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.border.*;
public class AccUI implements ActionListener {
	//===================================================
	// 전역변수 선언
	JFrame frame;
	JButton b_moveMoney, b_cancel;
	JTextField tf_sendAccNum, tf_recvAccNum, tf_moveMoney;

	// 확인다이알로그에 필요한 변수 선언
	JDialog confirmDia;
	JLabel l_sendCust, l_recvCust, l_moveMoney, l_gainMoney;
	JButton b_diaConfirm;

	//===================================================
	// 전역 변수의 객체 생성
	public AccUI(){
		frame		= new JFrame("예금 이체 프로그램");
		b_moveMoney	= new JButton("예금이체실행");
		b_cancel	= new JButton("이체취소");
		
		tf_sendAccNum	= new JTextField(20);
		tf_recvAccNum	= new JTextField(20);
		tf_moveMoney	= new JTextField(20);

		// 확인다이알로그에 필요한 변수 선언
		confirmDia		= new JDialog(frame, "이체결과확인");
		l_sendCust		= new JLabel();
		l_recvCust		= new JLabel();
		l_moveMoney		= new JLabel();
		l_gainMoney		= new JLabel();
		b_diaConfirm	= new JButton(" 정상처리되었습니다!!! ");

	}

	//===================================================
	// 컴포넌트 붙이고 프레임 출력
	public void setup() {
		// 가운데 영역 (라벨과 텍스트필드 붙인 영역 )
		JPanel p_center1 = new JPanel();
		p_center1.setLayout(new FlowLayout(FlowLayout.RIGHT));
		p_center1.add(new JLabel("보내는분 계좌번호"));
		p_center1.add(tf_sendAccNum);

		JPanel p_center2 = new JPanel();
		p_center2.setLayout(new FlowLayout(FlowLayout.RIGHT));
		p_center2.add(new JLabel("받는분 계좌번호"));
		p_center2.add(tf_recvAccNum);

		JPanel p_center3 = new JPanel();
		p_center3.setLayout(new FlowLayout(FlowLayout.RIGHT));
		p_center3.add(new JLabel("이체 금액"));
		p_center3.add(tf_moveMoney);

		JPanel p_center = new JPanel();
		p_center.setLayout(new GridLayout(3, 1));
		p_center.add(p_center1);
		p_center.add(p_center2);
		p_center.add(p_center3);

		// South 영역 (버튼 붙인 영역)
		JPanel p_south = new JPanel();
		p_south.add(b_moveMoney);
		p_south.add(b_cancel);

		// 프레임에 붙이기
		frame.getContentPane().setLayout(new BorderLayout(20, 20));
		frame.getContentPane().add("Center", p_center);
		frame.getContentPane().add("South", p_south);

		frame.pack();
		frame.setVisible(true);

		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		//---------------------------------------------------
		// 다이알로그 붙이기
		//---------------------------------------------------
		l_sendCust.setBorder(new BevelBorder(BevelBorder.RAISED));
		l_recvCust.setBorder(new BevelBorder(BevelBorder.RAISED));
		l_moveMoney.setBorder(new BevelBorder(BevelBorder.RAISED));
		l_gainMoney.setBorder(new BevelBorder(BevelBorder.RAISED));

		JPanel p_diaCenter = new JPanel();
		p_diaCenter.setLayout(new GridLayout(4, 2, 20, 20));
		p_diaCenter.add(new JLabel(" 보내는 고객 "));
		p_diaCenter.add(l_sendCust);
		p_diaCenter.add(new JLabel(" 받 는 고 객"));
		p_diaCenter.add(l_recvCust );
		p_diaCenter.add(new JLabel(" 이 체 금 액 "));
		p_diaCenter.add(l_moveMoney );
		p_diaCenter.add(new JLabel(" 계좌남은금액 "));
		p_diaCenter.add(l_gainMoney );

		JPanel p_diaSouth = new JPanel();
		p_diaSouth.add(b_diaConfirm);

		confirmDia.getContentPane().setLayout(new BorderLayout(20, 20));
		confirmDia.getContentPane().add("Center", p_diaCenter);
		confirmDia.getContentPane().add("South", p_diaSouth);


	}

	// 이벤트처리 할 컴포넌트을 등록
	public void eventProc() {
		b_moveMoney.addActionListener(this);
		b_cancel.addActionListener(this);
	}

	public void actionPerformed(ActionEvent ev) {
		Object o = ev.getSource();

		// "이체실행" 버튼이 눌렸을 때
		if (o == b_moveMoney) {
			try {
			////////////////////////////////////////////////////////
			// 1. 화면에서 입력값 얻어오기
			// 2. Business Logic 객체 생성 (ex.AccLogic)
			// 3. BL객체에서 계좌 이체하는 함수 호출 (ex.moveAccount())
			//		- 1번의 입력값을 인자로 넘김
			//		- 호출 후 넘겨받는 리턴값으로는 0이면 정상처리이고 
			//		- 1이면 잘못된 경우이므로 메세지박스 출력 
				String sendNum = tf_sendAccNum.getText();
				String recvNum = tf_recvAccNum.getText();
				int money = Integer.parseInt(tf_moveMoney.getText());
				
				AccLogic logic = new AccLogic();
				int result = logic.moveAccount(sendNum, recvNum, money);
				
				if(result == 0) {
					JOptionPane.showMessageDialog(null, "이체성공");
				}else if(result == -1) {
					JOptionPane.showMessageDialog(null, "이체실패");
					return;
				}


			/******************************************************
			* 계좌 이체를 확인한 후에 결과를 다이알로그에 출력
			1. BL객체에서 레코드 검색하는 함수호출 ( ex. confirmAccount() )
			2. 1번의 결과로 받은 객체의 각각의 값을 다이알로그의 라벨에 출력
			3. 다이알로그 화면 출력
			*/


			}catch(Exception ex) {
				System.out.println("이체처리시 : " + ex.getMessage());
				JOptionPane.showMessageDialog(frame, "이체하는 도중 에러가 발생하였습니다!! 이를 워쩌");
				return;
			}

		}

		// "이체취소" 버튼이 눌렸을 때
		else if (o == b_cancel) {
			frame.setVisible(false);
			frame.dispose();
			System.exit(0);
		}

	}

	//===================================================
	// 프로그램 시작
	public static void main(String[] args) {
		
		AccUI acc = new AccUI();
		acc.setup();
		acc.eventProc();
	}
}
~~~

## ConfirmData
~~~java
public class  ConfirmData {
	String sendCust;
	String recvCust;
	int gainMoney;

	public ConfirmData() {

	}

	public void setSendCust( String sendCust ) {
		this.sendCust = sendCust;
	}

	public String getSendCust() {
		return sendCust;
	}

	public void setRecvCust( String recvCust ) {
		this.recvCust = recvCust;
	}

	public String getRecvCust() {
		return recvCust;
	}

	public void setGainMoney( int gainMoney ) {
		this.gainMoney = gainMoney;
	}

	public int getGainMoney() {
		return gainMoney;
	}
}
~~~