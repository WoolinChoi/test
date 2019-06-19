---
layout: post
title: jqueryIdcheck
category: ajax
tags: [java, ajax, jqueryIdcheck]
comments: false
---

# [jqueryIdcheck]()

## IdCheck
~~~jsp
<%@ page contentType="text/xml; charset=utf-8" %>
<%@ page language="java" import="java.sql.*"%>

<%
String driver="oracle.jdbc.driver.OracleDriver";
String user="team5";
String pass="1004";
String dbURL="jdbc:oracle:thin:@192.168.0.116:1521:orcl";
	Class.forName(driver);
	Connection conn = DriverManager.getConnection(dbURL,user,pass);
	
	String sql = "SELECT * FROM membertest WHERE id='" + request.getParameter("userId") + "'";
	System.out.println(sql);
	Statement st = conn.createStatement();
	ResultSet rs = st.executeQuery(sql);		

	String result = "NO";
	if(rs.next()){		
		result = "YES";
	}		
	
	st.close();
	rs.close();
	conn.close();
	out.print(result);
%>
~~~

## IdForm
~~~html
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>IdForm</title>
	<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
	<script type="text/javascript">
		$(function(){
// 			$(".userinput").keyup(function(){
			$("#id_check").click(function(){
				$.ajax({
					type : "GET",
					url : "IdCheck.jsp",
					data : {userId : $("input[name='id']").val()},
					dataType : "text",
					success : function(data){
						if(data.trim() == "YES"){
							$("#idmessage").text("이미 사용중인 아이디 입니다");
							$("#idmessage").show();
						}else{
							$("#idmessage").text("사용가능한 아이디입니다");
							$("#idmessage").show();
						}
					},
					error : function(){
						alert("error");
					}
				});
			});
		});
	</script>
</head>

<body>
	<input name="id" type="text" class="userinput" size="15" />
	<button type="button" id="id_check">중복체크</button><br/><br/>
	<!-- display가 none이기때문에 show로 보여줘야한다 -->
	<div id="idmessage" style="display:none;"></div>
</body>
</html>
~~~