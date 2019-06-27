---
layout: post
title: mvcSimple
category: framework
tags: [java, framework, mvc, mvcSimple]
comments: false
---

# [mvcSimple]()

## Start
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	// 변수를 프로젝트 명으로 잡음.
	String projectName = "/Jsp";
%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Start</title>
</head>

<body>
	기존 모델 1 방식으로 연결
	<a href="<%=projectName %>/05_mvc_class/1_mvcSimple/simpleView.jsp">기존 방식</a><br/>
	MVC 방식으로 연결
	<a href="<%=projectName%>/xxxx.simple">MVC 요청</a><br/>
	MVC 방식으로 연결 2
	<!-- 쿼리 스트링 추가  -->
	<a href="<%=projectName%>/simple?type=first">MVC 요청2</a><br/> <!-- 모든 요청이 SimpleControl 로 집중 -->
	MVC 방식으로 연결 3
	<a href="<%=projectName%>/SimpleControl">MVC 요청3</a>
</body>
</html>
~~~

## SimpleView
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" %> 
<%
	Object obj = request.getAttribute("param");
	String reqData = request.getParameter("type");
%>    
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>SimpleView</title>
</head>

<body>
	<%= obj %> <br/> <%=reqData %>
	복잡하다고 지나친 좌절과 놀람은 금물입니다. <br/><br/>
	<img src="05_mvc_class/1_mvcSimple/imgs/sponge_1.JPG"/><br/><br/>
</body>
</html>
~~~