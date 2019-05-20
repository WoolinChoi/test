---
layout: post
title: empOracle2
category: jdbc
tags: [java, jdbc, empOracle2]
comments: false
---

# [empOracle2]()

## InsertTest
~~~java
import java.sql.*;
public class InsertTest {
	public static void main(String[] args) {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@192.168.0.114:1521:orcl";
		String user = "scott";
		String pass = "tiger";
		Connection con = null;
		try {
			// 드라이버를 메모리 로딩
			Class.forName(driver);
			
			// 연결객체 얻어오기
			con = DriverManager.getConnection(url, user, pass);
			System.out.println("연결성공");
		}catch(Exception ex) {
			System.out.println("연결실패: " + ex.getMessage());
		}
		try {
			// 화면에서 입력값 얻어오기
			int empno = 6789;
			String ename = "갓DB";
			int sal = 9000;
			int deptno = 30;
			String job = "IT부서";
			
			// SQL 문장만들기(***)
			String sql = "INSERT INTO emp(empno, ename, sal, deptno, job) "
					+ "VALUES(?, ?, ?, ?, ?)";
			System.out.println(sql);
			
			// SQL 전송객체 만들기
			// Statement st = con.createStatement(); // 완성 sql일 때
			PreparedStatement st = con.prepareStatement(sql); // ?(미완성 sql)일 때는 preparedStatement해준다.
			st.setInt(1, empno);
			st.setString(2, ename);
			st.setInt(3, sal);
			st.setInt(4, deptno);
			st.setString(5, job);
			
			// 전송하기
			int result = st.executeUpdate(); // sql 전송하면 안됨
			
			// 닫기
			st.close();
			con.close();
			System.out.println("SQL 전송 성공");
		}catch(SQLException ex) {
			System.out.println("전송실패: " + ex.getMessage());
		}
	}
}
~~~

## SelectTest
~~~java
import java.sql.*;
public class SelectTest {
	public static void main(String[] args) {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@192.168.0.114:1521:orcl";
		String user = "scott";
		String pass = "tiger";
		Connection con = null;
		try {
			// 드라이버를 메모리 로딩
			Class.forName(driver);
			
			// 연결객체 얻어오기
			con = DriverManager.getConnection(url, user, pass);
			System.out.println("연결성공");
		}catch(Exception ex) {
			System.out.println("연결실패: " + ex.getMessage());
		}
		try {
			// SQL 문장만들기
//			int empno = 7788;
//			String sql = "SELECT * FROM emp WHERE empno = ?";
//			
//			// SQL 전송객체 만들기
//			PreparedStatement st = con.prepareStatement(sql);
//			st.setInt(1, empno);
//			
//			// 전송하기
//			ResultSet rs= st.executeQuery(); // sql 지정하면 안됨
//			if(rs.next()) {
//				System.out.println(rs.getInt("EMPNO") + "/" + rs.getString("ENAME") + "/" + rs.getInt("SAL"));
//			} // 가동성을 위해 while문보다 if문을 써주고 하나라도 next를 사용한다.
			
			// 1. 사원 테이블의 총 사원수와 월급의 평균을 출력하시오.
			String sql = "SELECT count(*) count, round(avg(sal)) avg FROM emp";
		
			Statement st = con.createStatement();
			ResultSet rs= st.executeQuery(sql);
			if(rs.next()) {
				System.out.println(rs.getInt("COUNT") + "/" + rs.getInt("AVG"));
			}
			
			// 닫기
			rs.close();
			st.close();
			con.close();
			System.out.println("SQL 전송 성공");
		}catch(SQLException ex) {
			System.out.println("전송실패: " + ex.getMessage());
		}
	}
}
~~~

## UpdateTest
~~~java
import java.sql.*;
public class UpdateTest {
	public static void main(String[] args) {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@192.168.0.114:1521:orcl";
		String user = "scott";
		String pass = "tiger";
		Connection con = null;
		try {
			// 드라이버를 메모리 로딩
			Class.forName(driver);
			
			// 연결객체 얻어오기
			con = DriverManager.getConnection(url, user, pass);
			System.out.println("연결성공");
		}catch(Exception ex) {
			System.out.println("연결실패: " + ex.getMessage());
		}
		try {
			// 화면에서 입력값 얻어오기
			int empno = 6789;
			String ename = "홍숙자";
			int sal = 12000;
			int deptno = 20;
			String job = "개발";
			
			// (*) sql 문장 변경
			String sql = "UPDATE emp SET ename = ?, sal = ?, deptno = ?, job = ? WHERE empno = ?";
			System.out.println(sql);
			
			// SQL 전송객체 만들기
			PreparedStatement st = con.prepareStatement(sql); 
			st.setString(1, ename);
			st.setInt(2, sal);
			st.setInt(3, deptno);
			st.setString(4, job);
			st.setInt(5, empno);
			
			// 전송하기
			int result = st.executeUpdate();
			
			// 닫기
			st.close();
			con.close();
			System.out.println("SQL 전송 성공");
		}catch(SQLException ex) {
			System.out.println("전송실패: " + ex.getMessage());
		}
	}
}
~~~