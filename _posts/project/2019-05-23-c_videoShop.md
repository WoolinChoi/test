---
layout: post
title: videoShop
category: project
tags: [java, project, videoShop]
comments: false
---

# [videoShop]()

## VideoShop
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

			pane.setSelectedIndex(0);

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

## OracleCon
~~~java
public class OracleCon {
	static OracleCon con = null;
	
	private OracleCon() throws Exception {
		// 1. 드라이버 로딩
		Class.forName("oracle.jdbc.driver.OracleDriver");
		System.out.println("단 한번");
	}
	
	public static void getInstance() throws Exception {
		// 첫번째 부를때는 null이기때문에 호출되지만 나머지는 null이 아니기때문에 호출이 안된다. 
		if(con == null) {
			con = new OracleCon();
		}
	}
}
~~~

## CustomerModel
~~~java
import java.sql.*;
import model.dao.CustomerDao;
import model.vo.Customer;
public class CustomerModel implements CustomerDao {
	String driver = "oracle.jdbc.driver.OracleDriver";
	String url = "jdbc:oracle:thin:@safesoo7.iptime.org:1521:XE";
	String user = "oracle";
	String pass = "oracle";
	Connection con = null;
	public CustomerModel() throws Exception {
	 	// 1. 드라이버로딩
		Class.forName(driver);
		OracleCon.getInstance();
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

## VideoModel
~~~java
import java.sql.*;
import java.util.ArrayList;
import model.dao.VideoDao;
import model.vo.Video;
public class VideoModel implements VideoDao{
	String driver = "oracle.jdbc.driver.OracleDriver";
	String url = "jdbc:oracle:thin:@safesoo7.iptime.org:1521:XE";
	String user = "oracle";
	String pass = "oracle";
	Connection con = null;
	
	public VideoModel() throws Exception{
		// 1. 드라이버로딩
		Class.forName(driver);
		OracleCon.getInstance();
	}
	
	// 입력했을 때 
	public int insertVideo(Video vo, int count) throws Exception {

		ResultSet rs = null;
		PreparedStatement st = null;
		PreparedStatement st2 = null;
		PreparedStatement st3 = null;

		String video_num = null;

		try {
			con = DriverManager.getConnection(url, user, pass);

			String sql = "INSERT INTO " +
					"video(VideoNumber," +
					" Title, Genre, Director," +
					" Actor, Description)" +
					" VALUES (seq_video_number.nextval, ?, ?, ?, ?, ?)";

			st = con.prepareStatement(sql);

			st.setString(1, vo.getVideoName());
			st.setString(2, vo.getGenre());
			st.setString(3, vo.getDirector());
			st.setString(4, vo.getActor());
			st.setString(5, vo.getExp());

			int res1 = st.executeUpdate();

			if (res1 != 1) {
				con.rollback();
				return -1;
			}

			String sql2 = "SELECT seq_video_number.currval AS cur FROM dual";
			st2 = con.prepareStatement(sql2);
			System.out.println(sql2);
			rs = st2.executeQuery();

			if (rs.next()) {
				video_num = rs.getString("cur");
			}

			System.out.println(video_num);

			for (int i = 0; i < count; i++) {
				String sql3 = "INSERT INTO " +
						"video_management(ItemNumber, VideoNumber)" +
						" VALUES (seq_item_number.nextval, ?)";
				st3 = con.prepareStatement(sql3);

				st3.setString(1, video_num);

				int res2 = st3.executeUpdate();

				if (res2 != 1) {
					con.rollback();
					return -1;
				}
			}
			con.commit();
		}catch(Exception ex) {
			try {
				con.rollback();
			}catch(Exception e) {}
			return -1;
		}finally {
			if (rs != null) try {rs.close();} catch (SQLException ex) {}
			if (con != null) try {con.close();} catch (SQLException ex) {}
		}
		return 0;
	}
	
	// 비디오 검색했을 때
	public ArrayList searchVideo(int sel, String word) throws Exception {

		ResultSet rs = null;
		PreparedStatement st = null;

		try {
			con = DriverManager.getConnection(url, user, pass);

			String[] cols = {"Title", "Director"};

			String sql = "SELECT VideoNumber, Title , Genre, Director, Actor FROM video " +
					" WHERE " + cols[sel] + " LIKE  '%" + word + "%' ";

			ArrayList list = new ArrayList();

			st = con.prepareStatement(sql);
			rs = st.executeQuery();

			// 6. 결과처리
			while (rs.next()) {
				ArrayList data = new ArrayList();

				data.add(rs.getInt("VideoNumber"));
				data.add(rs.getString("Title"));
				data.add(rs.getString("Genre"));
				data.add(rs.getString("Director"));
				data.add(rs.getString("Actor"));

				list.add(data);
			}
			return list;
		} finally {
			st.close();
			con.close();
		}
	}
	
	// 검색해서 나온 값을 눌렀을 때
	public Video selectByPK(int vNum) throws Exception {
		ResultSet rs = null;
		PreparedStatement st = null;
		Video vo = new Video();

		try {
			con = DriverManager.getConnection(url, user, pass);

			String sql = "SELECT VideoNumber, Title , Genre, Director, Actor, Description FROM video " 
					+ " WHERE VideoNumber = ?";

			st = con.prepareStatement(sql);
			st.setInt(1, vNum);
			
			rs = st.executeQuery();
			
			// 6. 결과처리
			while (rs.next()) {
				vo.setVideoNo(rs.getInt("VideoNumber"));
				vo.setVideoName(rs.getString("Title"));
				vo.setGenre(rs.getString("Genre"));
				vo.setDirector(rs.getString("Director"));
				vo.setActor(rs.getString("Actor"));
				vo.setExp(rs.getString("Description"));
			}
			return vo;
		} finally {
			st.close();
			con.close();
		}	
	}
	
	// 수정하기
	public void modifyVideo(Video vo) throws Exception{
		con = DriverManager.getConnection(url, user, pass);

		String sql = "Update video SET " +
				" VideoNumber = ?, " +
				" Title = ?, " +
				" Genre = ?, " +
				" Director = ?, " +
				" Actor = ?, " +
				" Description = ? " +
				" WHERE VideoNumber = ? ";

		PreparedStatement st = con.prepareStatement(sql);

		st.setInt(1, vo.getVideoNo());
		st.setString(2, vo.getVideoName());
		st.setString(3, vo.getGenre());
		st.setString(4, vo.getDirector());
		st.setString(5, vo.getActor());
		st.setString(6, vo.getExp());
		st.setInt(7, vo.getVideoNo());

		int result = st.executeUpdate();

		st.close();
		con.close();
	}
	
	// 삭제하기
	public void deleteVideo(Video vo) throws Exception{
		con = DriverManager.getConnection(url, user, pass);

		String sql = "DELETE FROM video WHERE VideoNumber = ? ";

		PreparedStatement st = con.prepareStatement(sql);
		st.setInt(1, vo.getVideoNo());

		int result = st.executeUpdate();

		st.close();
		con.close();
	}
}
~~~

## RentModel
~~~java
import java.sql.*;
import java.util.ArrayList;
import model.dao.RentDao;
import model.vo.Customer;
public class RentModel implements RentDao {
	String driver = "oracle.jdbc.driver.OracleDriver";
	String url = "jdbc:oracle:thin:@safesoo7.iptime.org:1521:XE";
	String user = "oracle";
	String pass = "oracle";
	Connection con = null;
	
	public RentModel() throws Exception {
		// 1. 드라이버로딩
		Class.forName(driver);
		OracleCon.getInstance();
	}
	
	// 대여 메소드
	public void rentVideo(String tel, int vNum) throws Exception {
			// 2. Connection 연결객체 얻어오기
			con = DriverManager.getConnection(url, user, pass);
			PreparedStatement st = null;

			try {
				// 3. sql 문장
				String sql = "INSERT INTO rental_management(RentalNumber, PhoneNumber, ItemNumber, RentalDate) " + 
						"VALUES (seq_rental_number.nextval, ?, ?, sysdate)";
				
				// 4. 전송 객체
				st = con.prepareStatement(sql);
				st.setString(1, tel);
				st.setInt(2, vNum);
				
				// 5. 전송
				int rs = st.executeUpdate();
				System.out.println("완료");
			} finally {
				// 6. 닫기
				st.close();
				con.close();
			}
	}
	
	// 반납 메소드
	public void returnVideo(int vNum) throws Exception {
		// 2. Connection 연결객체 얻어오기
		con = DriverManager.getConnection(url, user, pass);
		PreparedStatement st = null;
		int rs = 0; 
		
		try {
			// 3. sql 문장
			String sql = "UPDATE rental_management SET returnconfirm = 1, " + 
					" overduedays = CASE WHEN sysdate - rentaldate - 3 <= 0 THEN 0 " + 
					" WHEN sysdate - rentaldate - 3 > 0 THEN sysdate - rentaldate - 3 " + 
					" END " + 
					" WHERE itemnumber = ? AND returnconfirm = 0";
			
			// 4. 전송 객체
			st = con.prepareStatement(sql);
			st.setInt(1, vNum);
			
			// 5. 전송
			rs = st.executeUpdate();
			System.out.println("완료");
		}finally {
			st.close();
			con.close();			
		}
	}
	
	// 미납정보 검색 메소드 
	public ArrayList selectList() throws Exception {
		// 2. Connection 연결객체 얻어오기
		con = DriverManager.getConnection(url, user, pass);
		ArrayList list = new ArrayList();
		PreparedStatement st = null;
		ResultSet rs = null;
		
		try {
			// 3. sql 문장
			String sql = "SELECT rm.itemnumber itemnumber, rm.phonenumber phonenumber, vm.videonumber videonumber, " +
					" rm.rentaldate rentaldate, rm.rentaldate+3 as returndate, rm.returnconfirm returnconfirm" + 
					" FROM video_management vm INNER JOIN rental_management rm" + 
					" ON vm.itemnumber = rm.itemnumber" + 
					" INNER JOIN video v" + 
					" ON v.videonumber = vm.videonumber" + 
					" INNER JOIN customer c " + 
					" ON rm.phonenumber = c.phone_number"+
					" WHERE rm.returnconfirm = 1 ";
				
			// 4. 전송 객체
			st  = con.prepareStatement(sql);
			
			// 5. 전송
			rs = st.executeQuery();
			
			while(rs.next()) {
				ArrayList data = new ArrayList();
				data.add(rs.getString("ITEMNUMBER"));
				data.add(rs.getString("PHONENUMBER"));
				data.add(rs.getString("VIDEONUMBER"));
				data.add(rs.getString("RENTALDATE"));
				data.add(rs.getString("RETURNDATE"));
				data.add(rs.getString("RETURNCONFIRM"));
				
				list.add(data);
			}
			return list;
		}finally {
			st.close();
			con.close();
		}
	}
	
	// 전화입력 후 엔터치면 고객명을 출력하는 메소드
	public Customer insertSelectName(String mNum) throws Exception {
		// 2. Connection 연결객체 얻어오기
		con = DriverManager.getConnection(url, user, pass);
		PreparedStatement st = null;
		ResultSet rs = null;
					
		try {
			// 3. sql 문장
			String sql = "SELECT name FROM customer_management WHERE phonenumber LIKE '%' || ? || '%'";
			
			// 4. 전송 객체
			st = con.prepareStatement(sql);
			st.setString(1, mNum);
						
			// 5. 전송
			rs = st.executeQuery();
			Customer vo = new Customer();
			if(rs.next()) {
				vo.setCustName(rs.getString("NAME"));
			}
			return vo;
		}finally {
			// 6. 닫기
			st.close();
			con.close();
		}		
	}	
}
~~~

## CustomerDao
~~~java
import model.vo.Customer;
/** 고객관리 JDBC 연결 */
public interface CustomerDao {
	// 회원가입
	public void insertCustomer(Customer vo) throws Exception;
	// 전화번호로 검색
	public Customer selectByTel(String tel) throws Exception;
	// 고객정보 수정
	public int updateCustomer(Customer vo) throws Exception;
}
~~~

## VideoDao
~~~java
import java.util.ArrayList;
import model.vo.Video;
public interface VideoDao {
	// 비디오 입력
	public int insertVideo(Video vo, int count) throws Exception;
	// 비디오 내용 검색
	public ArrayList searchVideo(int sel, String word) throws Exception;
	// 비디오 번호 검색
	public Video selectByPK(int vNum) throws Exception;
}
~~~

## RentDao
~~~java
import java.util.ArrayList;
public interface RentDao {
	// 대여 메소드
	public void rentVideo(String tel, int vNum) throws Exception;
	// 반납 메소드
	public void returnVideo(int vNum) throws Exception;
	// 미납정보 검색 메소드
	public ArrayList selectList() throws Exception;
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

## Video
~~~java
public class Video {
	int videoNo;				// 비디오번호
	String genre;				// 장르
	String videoName;			// 비디오명
	String director;			// 감독
	String actor;				// 배우
	String exp;					// 설명
	
	public int getVideoNo() {
		return videoNo;
	}
	public void setVideoNo(int videoNo) {
		this.videoNo = videoNo;
	}
	public String getGenre() {
		return genre;
	}
	public void setGenre(String genre) {
		this.genre = genre;
	}
	public String getVideoName() {
		return videoName;
	}
	public void setVideoName(String videoName) {
		this.videoName = videoName;
	}
	public String getDirector() {
		return director;
	}
	public void setDirector(String director) {
		this.director = director;
	}
	public String getActor() {
		return actor;
	}
	public void setActor(String actor) {
		this.actor = actor;
	}
	public String getExp() {
		return exp;
	}
	public void setExp(String exp) {
		this.exp = exp;
	}
}
~~~

## CustomerView
~~~java
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import model.CustomerModel;
import model.dao.CustomerDao;
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
		JPanel pRegist = new JPanel();
		pRegist.setLayout(new GridBagLayout());
		GridBagConstraints cbc = new GridBagConstraints();
		cbc.weightx	= 1.0;
		cbc.weighty	= 1.0;
		cbc.fill = GridBagConstraints.BOTH;
		
		cbc.gridx = 0; 
		cbc.gridy = 0; 
		cbc.gridwidth = 1; 
		cbc.gridheight = 1;
		pRegist.add(new JLabel(" 이 름 "),	cbc);
		
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
		pRegist.add(new JLabel(" 전 화 "),	cbc);
		
		cbc.gridx = 1;	 			
		cbc.gridy = 1;			
		cbc.gridwidth = 1;			
		cbc.gridheight = 1;
		pRegist.add(tfCustTel, cbc);
		
		cbc.gridx = 2;	 			
		cbc.gridy = 1;			
		cbc.gridwidth = 1;			
		cbc.gridheight = 1;
		pRegist.add(new JLabel(" 추가전화 "), cbc);
		
		cbc.gridx = 3;	 			
		cbc.gridy = 1;			
		cbc.gridwidth = 1;			
		cbc.gridheight = 1;
		pRegist.add(tfCustTelAid, cbc);

		cbc.gridx = 0;	 			
		cbc.gridy = 2;			
		cbc.gridwidth = 1;			
		cbc.gridheight = 1;
		pRegist.add(new JLabel(" 주 소 "), cbc);
		
		cbc.gridx = 1;	 			
		cbc.gridy = 2;			
		cbc.gridwidth = 3;			
		cbc.gridheight = 1;
		pRegist.add(tfCustAddr,	cbc);

		cbc.gridx =	0;	 			
		cbc.gridy = 3;			
		cbc.gridwidth =	1;			
		cbc.gridheight = 1;
		pRegist.add(new JLabel(" 이메일 "), cbc);
		
		cbc.gridx =	1;	 			
		cbc.gridy = 3;			
		cbc.gridwidth =	3;			
		cbc.gridheight = 1;
		pRegist.add(tfCustEmail, cbc);

		// 회원검색 부분 붙이기
		JPanel pSearch = new JPanel();
		pSearch.setLayout(new GridLayout(2, 1));
				JPanel pSearchName = new JPanel();
				pSearchName.add(new JLabel(" 이 름 "));
				pSearchName.add(tfCustNameSearch);
				pSearchName.add(bCustNameSearch);
				JPanel pSearchTel = new JPanel();
				pSearchTel.add(new JLabel(" 전화번호 "));
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

## VideoView
~~~java
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import javax.swing.*;
import javax.swing.border.TitledBorder;
import javax.swing.table.AbstractTableModel;
import model.VideoModel;
import model.vo.Video;
public class VideoView extends JPanel {	
	// member field
	JTextField		tfVideoNum, tfVideoTitle, tfVideoDirector, tfVideoActor;
	JComboBox		comVideoJanre;
	JTextArea		taVideoContent;

	JCheckBox		cbMultiInsert;
	JTextField		tfInsertCount;

	JButton			bVideoInsert, bVideoModify, bVideoDelete;

	JComboBox		comVideoSearch;
	JTextField		tfVideoSearch;
	
	JTable			tableVideo; // view 역할
	
	VideoTableModel tbModelVideo; // model 역할
	
	// 비지니스 로직 : 모델 클래스 변수 선언
	VideoModel db;

	// constructor method
	public VideoView() {
		addLayout(); 	// 화면설계
		initStyle();
		eventProc();
		connectDB();	// DB연결
	}
	
	public void connectDB() {	// DB연결
		try {
			db = new VideoModel();
		}catch (Exception ex) {
			System.out.println("드라이버 로딩 실패");
		}
	}
	
	public void eventProc() {
		ButtonEventHandler hdlr = new ButtonEventHandler();
		bVideoInsert.addActionListener(hdlr);
		bVideoModify.addActionListener(hdlr);
		bVideoDelete.addActionListener(hdlr);
		tfVideoSearch.addActionListener(hdlr);
		
		cbMultiInsert.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				tfInsertCount.setEditable(cbMultiInsert.isSelected());
			}
		});
		
		// JTextArea 비디오 검색에서 클릭 했을 때
		tableVideo.addMouseListener(new MouseAdapter() {
			public void mouseClicked(MouseEvent e) {
				int col = 0;
				int row = tableVideo.getSelectedRow();
				int vNum = (Integer)tableVideo.getValueAt(row, col);
				
				// 1. 선택한 비디오 번호를 모델단의 selectByPK() 호출 시 인자로 보내기
				// 2. 넘겨받은 Video에서 해당 값들 화면 출력하기
				Video vo;
				try {
					vo = db.selectByPK(vNum);
					tfVideoNum.setText(String.valueOf(vo.getVideoNo()));
					tfVideoTitle.setText(vo.getVideoName());
					comVideoJanre.setSelectedItem(String.valueOf(vo.getGenre()));
					tfVideoDirector.setText(vo.getDirector());
					tfVideoActor.setText(vo.getActor());
					taVideoContent.setText(vo.getExp());	
				}catch (Exception ex) {
					System.out.println("에러 : " + ex.getMessage());
				}			
			}
		});
	}		
	
	// 버튼 이벤트 핸들러 만들기
	class ButtonEventHandler implements ActionListener {
		public void actionPerformed(ActionEvent ev) {
			Object o = ev.getSource();
			
			if(o == bVideoInsert) {  
				registVideo();					// 비디오 등록
			}
			else if(o == bVideoModify) {  
				modifyVideo();					// 비디오 정보 수정
			}
			else if(o == bVideoDelete) {  
				deleteVideo();					// 비디오 정보 삭제
			}
			else if(o == tfVideoSearch) {
				try {
					searchVideo();				// 비디오 검색
				}catch(Exception ex) {
					System.out.println("에러 : " + ex.getMessage());
				}
			}
		}
	}
	
	// 입고 클릭시  - 비디오 정보 등록
	public void registVideo(){
		Video vo = new Video();
		vo.setVideoName(tfVideoTitle.getText());
		vo.setGenre(comVideoJanre.getSelectedItem().toString());
		vo.setDirector(tfVideoDirector.getText());
		vo.setActor(tfVideoActor.getText());
		vo.setExp(taVideoContent.getText());
		int count = Integer.valueOf(tfInsertCount.getText());

		try {
			db.insertVideo(vo, count);
		} catch (Exception e) {
			System.out.println("에러 : " + e.getMessage());
		}
		clearTextField();
	}
	void clearTextField() {
		tfVideoNum.setText(null);
		tfVideoTitle.setText(null);
		tfVideoDirector.setText(null);
		tfVideoActor.setText(null);
	}
	
	public void initStyle() {   // 입력하지 못하게 만듬.
		tfVideoNum.setEditable(false);
		tfInsertCount.setEditable(false);		
		tfInsertCount.setHorizontalAlignment(JTextField.RIGHT);
	}
	
	// 수정 클릭시 - 비디오 정보 수정
		public void modifyVideo() {
			Video vo = new Video();
			// 비디오 번호는 기본키라 변경 불가
			vo.setVideoName(tfVideoTitle.getText());
			vo.setGenre(comVideoJanre.getSelectedItem().toString());
			vo.setDirector(tfVideoDirector.getText());
			vo.setActor(tfVideoActor.getText());
			vo.setExp(taVideoContent.getText());

			try {
				db.modifyVideo(vo);
			}catch(Exception ex) {
				System.out.println("에러 : " + ex.getMessage());
			}
			clearTextField();
		}
		
		// 삭제 클릭시 - 비디오 정보 삭제
		public void deleteVideo() {
			Video vo = new Video();
			vo.setVideoNo(Integer.valueOf(tfVideoNum.getText()));
			
			try {
				db.deleteVideo(vo);
			} catch (Exception ex) {
				System.out.println("에러 : " + ex.getMessage());
			}
			clearTextField();
		}
	
	// 비디오현황검색
		public void searchVideo() throws Exception {
			int sel = comVideoSearch.getSelectedIndex(); // 비디오번호를 선택하면 0, 제목을 선택하면 1
			String word = tfVideoSearch.getText();
			try {
				// 검색결과를 화면 JTextArea의 내용을 담당하는 TableModel 안에 data에 지정
				tbModelVideo.data = db.searchVideo(sel, word);
				tbModelVideo.fireTableDataChanged();
			}catch(Exception ex) {
				System.out.println("검색실패 : " + ex.getMessage());
			}
		}
		
	
	//  화면설계 메소드
	public void addLayout() {
		// 멤버변수의 객체 생성
		tfVideoNum = new JTextField();
		tfVideoTitle = new JTextField();
		tfVideoDirector = new JTextField();
		tfVideoActor = new JTextField();
		
		String[] cbJanreStr = {"멜로", "엑션", "스릴", "코미디"};
		comVideoJanre = new JComboBox(cbJanreStr);
		taVideoContent = new JTextArea();
		
		cbMultiInsert = new JCheckBox("다중입고");
		tfInsertCount = new JTextField("1", 5);
	
		bVideoInsert = new JButton("입고");
		bVideoModify = new JButton("수정");
		bVideoDelete = new JButton("삭제");
		
		String[] cbVideoSearch = {"제목", "감독"};
		comVideoSearch = new JComboBox(cbVideoSearch);
		tfVideoSearch = new JTextField(15);
		
		tbModelVideo = new VideoTableModel();
		tableVideo = new JTable(tbModelVideo);

		// 화면 구성
		// 왼쪽 영역 
		JPanel p_west = new JPanel();
		p_west.setLayout(new BorderLayout());
			// 왼쪽 - 메인 영역
			JPanel p_west_c = new JPanel();
			p_west_c.setLayout(new BorderLayout());
				
				// 왼쪽 - 메인 - 중앙
				JPanel p_west_c_c = new JPanel();
				p_west_c_c.setBorder(new TitledBorder("비디오정보입력"));
					
					// 비디오 정보 입력
					JPanel p_west_c_c_1 = new JPanel();
					p_west_c_c_1.setLayout(new GridLayout(5,2));
	                p_west_c_c_1.add(new JLabel(" 비디오 번호 "));
	                p_west_c_c_1.add(tfVideoNum);
	                p_west_c_c_1.add(new JLabel(" 제    목 "));
	                p_west_c_c_1.add(tfVideoTitle);
	                p_west_c_c_1.add(new JLabel(" 장    르  "));
	                p_west_c_c_1.add(comVideoJanre);
	                p_west_c_c_1.add(new JLabel(" 감    독 "));
	                p_west_c_c_1.add(tfVideoDirector);
	                p_west_c_c_1.add(new JLabel(" 배    우 "));
	                p_west_c_c_1.add(tfVideoActor);
					
					// 비디오 설명 입력
					JPanel p_west_c_c_2 = new JPanel();
					p_west_c_c_2.setLayout(new BorderLayout());
					p_west_c_c_2.add(new JLabel("설명"), BorderLayout.WEST);
					p_west_c_c_2.add(taVideoContent, BorderLayout.CENTER);
				
				p_west_c_c.setLayout(new GridLayout(2, 1));
				p_west_c_c.add(p_west_c_c_1);
				p_west_c_c.add(p_west_c_c_2);
			
			p_west_c.add(p_west_c_c, BorderLayout.CENTER);
			
		p_west.add(p_west_c, BorderLayout.CENTER);	
			
				// 왼쪽 - 메인 - 아래
				JPanel p_west_c_s = new JPanel();
				p_west_c_s.setBorder(new TitledBorder("다중입고시 선택하시오"));
				p_west_c_s.add(cbMultiInsert);
				p_west_c_s.add(tfInsertCount);
				p_west_c_s.add(new JLabel("개"));
		
			// 왼쪽 - 버튼 영역
			JPanel p_west_s = new JPanel();
			p_west_s.setLayout(new GridLayout(1, 3));
			p_west_s.add(bVideoInsert);
			p_west_s.add(bVideoModify);
			p_west_s.add(bVideoDelete);
			
			p_west_c.add(p_west_c_s, BorderLayout.SOUTH);
		
		p_west.add(p_west_s, BorderLayout.SOUTH);
		
		// 오른쪽 영역
		JPanel p_east = new JPanel();
		// 오른쪽 패널 위에 이름
		p_east.setBorder(new TitledBorder("비디오검색"));
		p_east.setLayout(new BorderLayout());
			
			JPanel p_east_north = new JPanel();
			p_east_north.add(comVideoSearch);
			p_east_north.add(tfVideoSearch);
			
		p_east.add(p_east_north, BorderLayout.NORTH);
		p_east.add(new JScrollPane(tableVideo), BorderLayout.CENTER);
		
		// 전체 영역 
		setLayout(new GridLayout(1, 2));
		add(p_west);
		add(p_east);		
	}
	
	//화면에 테이블 붙이는 메소드 
	class VideoTableModel extends AbstractTableModel { 
		  
		ArrayList data = new ArrayList();
		String[] columnNames = {"비디오번호", "제목", "장르", "감독", "배우"};

		// 1. 기본적인 TabelModel  만들기
		// 아래 세 함수는 TabelModel 인터페이스의 추상함수인데
		// AbstractTabelModel에서 구현되지 않았기에...
		// 반드시 사용자 구현 필수!!!!

		    public int getColumnCount() { 
		        return columnNames.length; 
		    } 
		     
		    public int getRowCount() { 
		        return data.size(); 
		    } 

		    public Object getValueAt(int row, int col) { 
				ArrayList temp = (ArrayList)data.get(row);
		        return temp.get(col); 
		    }
		    
		    public String getColumnName(int col) {
		    	return columnNames[col];
		    }
	}
}
~~~

## RentView
~~~java
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import javax.swing.*;
import javax.swing.border.TitledBorder;
import javax.swing.table.AbstractTableModel;
import model.RentModel;
import model.vo.Customer;
public class RentView extends JPanel {
	JTextField tfRentTel, tfRentCustName, tfRentVideoNum;
	JButton bRent;
	
	JTextField tfReturnVideoNum;
	JButton bReturn;
	
	JTable tableRecentList;
	
	RentTableModel rentTM;
	
	// 비지니스 로직 역할을 하는 모델 클래스 선언
	RentModel db;

	//	 생성자 함수
	public RentView() {
		addLayout();	// 화면구성
		eventProc();	// DB연결
		connectDB();
		
		selectNonReturn(); // 미납여부
	}
	
	// DB 연결
	void connectDB() {
		try {
			db = new RentModel();
		}catch(Exception ex) {
			System.out.println("에러 : " + ex.getMessage());
		}
	}
	
	// 이벤트 등록
	public void eventProc() {
		ActionHandler ah = new ActionHandler();
		// 이벤트가 발생할 객체들을 핸들러로 연결
		tfRentTel.addActionListener(ah);
		bRent.addActionListener(ah);
		bReturn.addActionListener(ah);
		                         
	}
	class ActionHandler implements ActionListener {
		public void actionPerformed(ActionEvent e) {
			System.out.println("이벤트");
			Object o = e.getSource();
			
			if( o == tfRentTel) {
				selectCustName();
			}else if(o == bRent) {
				rentVideo();
				selectNonReturn();
			}else if(o == bReturn) {
				returnVideo();
				selectNonReturn();
			}
		}
	}
	
	// 전화입력 후 엔터치면 고객명을 출력하는 메소드
	public void selectCustName() {
		// 1. 화면에서 필요한 정보를 얻어오기
		// 2. 모델쪽 메소드를 호출 
		// 3. 결과처리
		try {
			String mNum = tfRentTel.getText();
			Customer vo = db.insertSelectName(mNum);
			tfRentCustName.setText(vo.getCustName());	
		}catch(Exception ex) {
			System.out.println("에러 : " + ex.getMessage());
		}
	}
	
	// 비디오 대여시 처리하는 메소드
	public void rentVideo() {
		// 1. 화면에서 필요한 정보를 얻어오기
		// 2. 모델쪽 메소드를 호출 
		// 3. 대여 후 결과처리
		String tel = tfRentTel.getText();
		String vNum = tfRentVideoNum.getText();
		try {
			db.rentVideo(tel, Integer.parseInt(vNum));
		}catch(Exception ex) {
			System.out.println("에러 : " + ex.getMessage());
		}
		
	}
	
	// 비디오 반납시 처리하는 메소드
	public void returnVideo() {
		// 1. 화면에서 필요한 정보를 얻어오기
		// 2. 모델쪽 메소드를 호출 
		// 3. 대여 후 결과처리
		String vNum = tfReturnVideoNum.getText();
		try {
			db.returnVideo(Integer.parseInt(vNum));
		}catch(Exception ex) {
			System.out.println("에러 : " + ex.getMessage());
		}
	}
	
	// 미납목록 출력하는 메소드
	public void selectNonReturn() {
		try {
			rentTM.data = db.selectList();
			rentTM.fireTableDataChanged();
			
		}catch(Exception ex) {
			System.out.println("에러 : " + ex.getMessage());
		}
	}
	
	
	/*	객체 생성 및 화면 구성   */
	void addLayout() {
		// 멤버 변수 객체 생성
		tfRentTel = new JTextField();
		tfRentCustName = new JTextField();
		tfRentVideoNum = new JTextField();
		
		bRent = new JButton("대여");
		tfReturnVideoNum = new JTextField(15);
		bReturn = new JButton("반납");
		
		rentTM = new RentTableModel();
		tableRecentList = new JTable(rentTM);
		
		// 화면 구성
		// 위쪽 영역
		JPanel p_north = new JPanel();
		p_north.setLayout(new GridLayout(1, 2));
		
			// 위쪽 왼쪽
			JPanel p_north_west = new JPanel();
			p_north_west.setBorder(new TitledBorder("대여"));
			p_north_west.setLayout(new GridLayout(4,2));
			p_north_west.add(new JLabel(" 전 화 번 호 "));
			p_north_west.add(tfRentTel);
			p_north_west.add(new JLabel(" 고 객 명 "));
			p_north_west.add(tfRentCustName);
			p_north_west.add(new JLabel(" 대 여 번 호  "));
			p_north_west.add(tfRentVideoNum);
			p_north_west.add(bRent);

		p_north.add(p_north_west);
		
			// 위쪽 오른쪽
			JPanel p_north_east = new JPanel();
			p_north_east.setBorder(new TitledBorder("반납"));
			p_north_east.setLayout(new FlowLayout());
			p_north_east.add(new JLabel(" 대 여 번 호"));
			p_north_east.add(tfReturnVideoNum);
			p_north_east.add(bReturn);
			
		p_north.add(p_north_east);
			
		// 센터 영역
		JPanel p_center = new JPanel();
		p_center.setLayout(new BorderLayout());
		p_center.add(new JScrollPane(tableRecentList));
		
		// 전체 영역
		setLayout(new BorderLayout());
		add(p_north, BorderLayout.NORTH);
		add(p_center, BorderLayout.CENTER);
		
	}

	class RentTableModel extends AbstractTableModel { 
		  
		ArrayList data = new ArrayList();
		String[] columnNames = {"대여번호", "전화번호", "비디오번호", "대여일", "반납예정일", "반납여부"};

			public int getColumnCount() { 
		        return columnNames.length; 
		    } 
		     
		    public int getRowCount() { 
		        return data.size(); 
		    } 

		    public Object getValueAt(int row, int col) { 
				ArrayList temp = (ArrayList)data.get(row);
		        return temp.get(col); 
		    }
		    
		    public String getColumnName(int col) {
		    	return columnNames[col];
		    }
	}
}
~~~