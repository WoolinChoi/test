---
layout: post
title: empMysql
category: jdbc
tags: [java, jdbc, empMysql]
comments: false
---

# [empMysql]()

## InsertTest
~~~java
import java.sql.*;
public class InsertTest {
	public static void main(String[] args) {
		String driver = "com.mysql.cj.jdbc.Driver";
		String url = "jdbc:mysql://localhost:3306/test?serverTimezone=UTC";
		String user = "scott";
		String pass = "tiger";
		Connection con = null;
		try {
			// 1. 드라이버를 메모리 로딩
			Class.forName(driver);
			// 2. 연결객체 얻어오기
			con = DriverManager.getConnection(url, user, pass);
			System.out.println("연결성공");
		}catch(Exception ex) {
			System.out.println("연결실패: " + ex.getMessage());
		}
		/*
			3. SQL 문장만들기(***)
			4. SQL 전송객체 만들기
			5. 전송하기
			6. 닫기
		 */
//		try {
//			// 방금 입력한 사원정보에서 이름은 알아서 연봉은 60000달러 변경
//			String sql = "UPDATE emp SET ename = '갓아무개', sal = 60000 "
//					+ "WHERE empno = 2345";
//			System.out.println(sql);
//			Statement st = con.createStatement();
//			st.executeUpdate(sql);
//			st.close();
//			con.close();
//			System.out.println("SQL 전송 성공");
//		}catch(SQLException ex) {
//			System.out.println("전송실패: " + ex.getMessage());
//		}
	}
}
~~~

## SelectTest
~~~java
import java.sql.*;
public class SelectTest {
	public static void main(String[] args) {
		String driver = "com.mysql.cj.jdbc.Driver";
		String url = "jdbc:mysql://localhost:3306/test?serverTimezone=UTC";
		String user = "scott";
		String pass = "tiger";
		Connection con = null;
		try {
			// 1. 드라이버를 메모리 로딩
			Class.forName(driver);
			// 2. 연결객체 얻어오기
			con = DriverManager.getConnection(url, user, pass);
			System.out.println("연결성공");
		}catch(Exception ex) {
			System.out.println("연결실패: " + ex.getMessage());
		}
		try {
			String sql = "SELECT * FROM temp ORDER BY empno";
			Statement st = con.createStatement();
			ResultSet rs= st.executeQuery(sql);
			while(rs.next()) {
				System.out.println(rs.getInt("EMPNO") + "/" + rs.getString("ENAME") + "/" + rs.getInt("SAL"));
			}
			st.close();
			con.close();
			System.out.println("SQL 전송 성공");
		}catch(SQLException ex) {
			System.out.println("전송실패: " + ex.getMessage());
		}
	}
}
~~~