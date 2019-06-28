---
layout: post
title: jqueryBasic
category: ajax
tags: [java, ajax, jqueryBasic]
comments: false
---

# [jqueryBasic]()

## AjaxGetCsv
~~~html
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>AjaxGetCsv</title>
	<script type="text/javascript" src="libs/jquery-1.9.1.min.js"></script>
	<script type="text/javascript">
		$(function(){
			var data = {cate : "book", name : "hong"};
			$.get("01_server.jsp", data, parseData);
		});
		
		function parseData(strText){
			alert(strText);
		};
	</script>
</head>

<body>
	서버로부터 넘겨받은 데이터<br/>
	첫번째 데이터 : <input type="text" name="" id="cate"/><br/>
	두번째 데이터 : <input type="text" name="" id="name"/><br/>
</body>
</html>
~~~

## AjaxGetCsv_server
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	// 1. 이전 화면에서 넘겨받은 데이타
	String cate = request.getParameter("cate");
	String name = request.getParameter("name");
	
	// 2. 다시 화면으로 보낼 데이터 구성
	cate = "서버로부터" + cate;
	name = "from_server_" + name;
	out.write("cate=" + cate + "|name=" + name);
%>    
~~~

## AjaxPostCsv
~~~html
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>AjaxPostCsv</title>
	<script type="text/javascript"  src="libs/jquery-1.9.1.min.js"></script>
	<script type="text/javascript">
		$(function(){
			var data = {cate : "book", name : "hong"};
			$.post("02_server.jsp", data, parseData);
		});
		
		function parseData(strText){
// 			alert(strText);
			var ary = strText.split("|"); 
			// ary[0] : "cate=서버에서 book변경"
			// ary[1] : "name=변경된 hong"
			for(var i = 0; i < ary.length; i++){
				var param = ary[i].split("=");
				// i가 0인 상태 param[0] : "cate"
				//			param[1] : "서버에서 book변경"
				if(param[0].trim() == "cate"){
					$("#cate").val(param[1]);
				}
				if(param[0].trim() == "name"){
					$("#name").val(param[1]);
				}
			}
		};
	</script>	
</head>

<body>
	서버로부터 넘겨받은 데이터<br/>
	첫번째 데이터 : <input type="text" name="" id="cate"/><br/>
	두번째 데이터 : <input type="text" name="" id="name"/><br/>
</body>
</html>
~~~

## AjaxPostCsv_server
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	// 1. 이전 화면에서 넘겨받은 데이타
	String cate = request.getParameter("cate");
	String name = request.getParameter("name");
	
	// 2. 다시 화면으로 보낼 데이터 구성
	cate = "서버로부터" + cate;
	name = "from_server_" + name;
	out.write("cate=" + cate + "|name=" + name);
%>    
~~~

## AjaxPostXml
~~~html
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>AjaxPostXml</title>
	<script type="text/javascript" src="libs/jquery-1.9.1.min.js"></script>
	<script type="text/javascript">
		$(function(){
			var param = {cate : "book", name : "hong"};
			$.ajax({
				type : "POST",
				data : param,			// 보낼데이타 객체
				url : "03_server.jsp",
				dataType : "xml",		// 받는 데이타 형식
				success : parseData
			});
			
			function parseData(xmlInfo){
				// jquery로 찾기
				$("#cate").val($(xmlInfo).find("first").text());
			};
		}); 

// 		$.post("03_server.jsp", param, parseData, "xml"); // 축약형
	</script>
</head>

<body>
	서버로부터 넘겨받은 데이터<br/>
	첫번째 데이터 : <input type="text" name="" id="cate"/><br/>
	두번째 데이터 : <input type="text" name="" id="name"/><br/>
</body>
</html>
~~~

## AjaxPostXml_server
~~~jsp
<%@ page language="java" contentType="text/xml; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!-- contentType="text/xml"이다. -->  
<%	// 1. 이전 화면에서 넘겨받은 데이타
	String cate = request.getParameter("cate");
	String name = request.getParameter("name");
	
	// 2. 다시 화면으로 보낼 데이터 구성
	String result = "";
	
	result += "<data>";
	result += "<first>" + "서버에서" + cate + "변경" + "</first>";
	result += "<second>" + "from_" + name + "_server" + "</second>";
	result += "</data>";
	
	out.write(result);	
%>    
~~~

## AjaxPostJson
~~~html
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>AjaxPostJson</title>
	<script type="text/javascript"  src="libs/jquery-1.9.1.min.js"></script>
	<script type="text/javascript">
		$(function(){
			var param = {cate : "book", name : "hong"};
			$.ajax({
				type : "POST",
				data : param,
				url : "04_server.jsp",
				success : function(resText){
					    	  var obj = {};
					    	  obj = eval("(" + resText + ")");
					    	  $("#cate").val(obj.first);
					      } 
			});
		});
	</script>
</head>

<body>
	서버로부터 넘겨받은 데이터<br/>
	첫번째 데이터 : <input type="text" name="" id="cate"/><br/>
	두번째 데이터 : <input type="text" name="" id="name"/><br/>
</body>
</html>
~~~

## AjaxPostJson_server
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%	// 1. 이전 화면에서 넘겨받은 데이타
	String cate = request.getParameter("cate");
	String name = request.getParameter("name");
	
	// 2. 다시 화면으로 보낼 데이터 구성
	String result = "";
	
	result += "{";
	result += "'first' : " + "'changed_" + cate + "_by_server" + "',";
	result += "'second' : " + "'from_" + name + "_server'";
	result += "}";
	System.out.println(result);
	out.write(result);	
%> 
~~~