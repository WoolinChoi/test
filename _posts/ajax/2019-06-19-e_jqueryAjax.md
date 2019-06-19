---
layout: post
title: jqueryAjax
category: ajax
tags: [java, ajax, jqueryAjax]
comments: false
---

# [jqueryAjax]()

## InputCustomer
~~~html
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>InputCustomer</title>
<script type="text/javascript" src="../02_jquery_ajax_basic/libs/jquery-1.9.1.min.js"></script>
<script type="text/javascript">
	function insertCustomer(){
		$.ajax({
			type : "GET",
			url : "DataInput.jsp",
			data : {
				name : $("#name").val(),
				age : $("#age").val(),
				tel : $("#tel").val(),
				addr : $("#addr").val()
			},	
			dataType : "text",
			success : function(result){
				if(result == 1){
					alert('입력이 완료됬습니다');
				}else{
					alert('다시입력하세요');
				}
			},
			error : function(){
				alert("error");
			}
		});
	};
	
	function getData(){
		var table = $("#listTable");
		var param = {name : "name", age : "age", tel : "tel", addr : "addr"};
		$.ajax({
			type : "GET",
			url : "DataSelect.jsp",
			data : param,	
			dataType : "xml",
			success : function(data){
/*
				var person = $(data).find("person");
				var str = '<tr><td width="80" align="center">Name</td><td width="50" align="center">Age</td><td width="100" align="center">Tel</td><td width="250" align="center">Addr</td></tr>"table.find("tr:first")';
				for(var i = 0; i < person.length; i++){
					str += "<tr>";
					str += "<td>" + person.eq(i).find("name").text() + "</td>";
					str += "<td>" + person.eq(i).find("age").text() + "</td>";
					str += "<td>" + person.eq(i).find("tel").text() + "</td>";
					str += "<td>" + person.eq(i).find("addr").text() + "</td>";
					str += "</tr>"
				}
				table.html(str);
*/
				
				var person = $(data).find("person");
				$("#listTable").find("tr").not(":first").remove();
				for(var i = 0; i < person.length; i++){
					var name = person.eq(i).find("name").text();
					var age = person.eq(i).find("age").text();
					var tel = person.eq(i).find("tel").text();
					var addr = person.eq(i).find("addr").text();
					$("#listTable").append("<tr><td>" + name + "</td><td>" + age + "</td><td>" + tel + "</td><td>" + addr + "</td></tr>");
				}
			},
			error : function(){
				alert("error");
			}
		});
	};
</script>
</head>

<!-- <body> -->
<body>
	<h2>고객정보 입력 </h2>
	<form name="inForm" method="post">
	<table border = 1>
		<tr>
			<td width="80" align="center">Name</td>
			<td width="50" align="center">Age</td>
			<td width="100" align="center">Tel</td>	
			<td width="250" align="center">Addr</td>
		</tr>
		<tr>
			<td align="center"><input type="text" size="8" name="name" id="name"></td>
			<td align="center"><input type="text" size="4" name="age" id="age"></td>
			<td align="center"><input type="text" size="12" name="tel" id="tel"></td>
			<td align="center"><input type="text" size="30" name="addr" id="addr"></td>
		</tr>
		<tr>
			<td colspan="4" align="center"> 
				<input type="button" value="입력" onclick="insertCustomer()">
			</td>
		</tr>
	</table>
	
	<br>
	<hr>
	
	<h2>고객정보 목록보기 </h2>
	<table border='0' width="510"> 
		<tr>
			<td align="right"><input type="button" value="가져오기" onclick="getData()"></td>
		</tr>
	</table>
	<table border = 1 id="listTable">
		<tr>
			<td width="80" align="center">Name</td>
			<td width="50" align="center">Age</td>
			<td width="100" align="center">Tel</td>	
			<td width="250" align="center">Addr</td>
		</tr>
	</table>
	<div id="myDiv"></div>
</form>
</body>
</html>
~~~

## DataInput
~~~jsp
<%@ page language="java" import="java.sql.*"%>
<%
String driver="oracle.jdbc.driver.OracleDriver";
String user = "team5";
String pass = "1004";
String dbURL = "jdbc:oracle:thin:@192.168.0.116:1521:orcl";

String name  = request.getParameter("name");
String age = request.getParameter("age");
String tel = request.getParameter("tel");
String addr= request.getParameter("addr");

	Class.forName(driver);
	Connection connection=DriverManager.getConnection(dbURL,user,pass);		
	
	String sql = "INSERT INTO ajax_temp(name, age, tel, addr) VALUES(";
	sql += "'" + name + "','" + age + "','" + tel + "','" + addr + "')";
	
	Statement stmt = connection.createStatement();
	int result = stmt.executeUpdate(sql);		

	stmt.close();
	connection.close();
	
	out.write(String.valueOf(result));
%>
~~~

## DataSelect
~~~jsp
<%@page contentType="text/xml; charset=utf-8" %>
<%@ page language="java" import="java.sql.*"%>
<%
String driver = "oracle.jdbc.driver.OracleDriver";
String user = "team5";
String pass = "1004";
String dbURL = "jdbc:oracle:thin:@192.168.0.116:1521:orcl";

String rtn_xml="";

	Class.forName(driver);
	Connection connection=DriverManager.getConnection(dbURL,user,pass);
	
	String sql = "SELECT * FROM ajax_temp";
	
	Statement stmt = connection.createStatement();
	ResultSet rs = stmt.executeQuery(sql);	
	
	rtn_xml += "<customer>";

	while (rs.next()){		
		rtn_xml += "<person>";
		rtn_xml += "<name>" + rs.getString("name") + " </name>";
		rtn_xml += "<age>" + rs.getString("age") +  "</age>";
		rtn_xml += "<tel>" + rs.getString("tel") +  "</tel>";
		rtn_xml += "<addr>" + rs.getString("addr") +  "</addr>";
		rtn_xml += "</person>";		
	}
	
	rs.close();
	stmt.close();
	connection.close();

	rtn_xml += "</customer>";

	System.out.println(rtn_xml);
	
	out.write(rtn_xml);
%>
~~~