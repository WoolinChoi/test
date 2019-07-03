---
layout: post
title: dynamicWeb
category: spring
tags: [java, spring, dynamicWeb]
comments: false
---

# [dynamicWeb]()

## Common-servlet_xml
~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
<!-- ViewResolver : Controller가 리턴한 뷰 이름을 기반으로 Controller 처리 결과를 생성할 뷰를 결정 -->
<bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
	<property name="prefix" value="/WEB-INF/view/"/>
	<property name="suffix" value=".jsp"/>
</bean>
</beans>
~~~

## SpringMVC-servlet_xml
~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:context="http://www.springframework.org/schema/context"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.3.xsd">
<!-- 빈 객체 생성 -->
<bean class="spring.mvc.sample.HelloController"></bean>

<!-- 자동 빈 객체 생성 -->
<context:component-scan base-package="example.member.controller"/>

<bean id="memberVO" class="example.member.model.MemberVO">
	<property name="id" value="001"/>
	<property name="name" value="홍길자"/>
	<property name="age" value="25"/>
</bean>
</beans>
~~~

## web_xml
~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://xmlns.jcp.org/xml/ns/javaee" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd" id="WebApp_ID" version="4.0">
  <display-name>fDynamicWeb</display-name>
  <welcome-file-list>
    <welcome-file>index.jsp</welcome-file>
  </welcome-file-list>
  
  <!-- common servlet 설정 -->
  <listener>
  	<listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
  </listener>
  <context-param>
  	<param-name>contextConfigLocation</param-name>
  	<param-value>/WEB-INF/springConfig/common-servlet.xml</param-value>
  </context-param>  
  
  <!-- spring servlet 설정 -->
  <servlet>
    <servlet-name>springMVC</servlet-name>
	<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
	<init-param>
	  <param-name>contextConfigLocation</param-name>
	  <param-value>/WEB-INF/springConfig/springMVC-servlet.xml</param-value>
	</init-param>
  </servlet>
  <servlet-mapping>
	<servlet-name>springMVC</servlet-name>
	<url-pattern>*.do</url-pattern>
  </servlet-mapping>
  
  <!-- 한글 인코딩 -->
  <filter>
  	<filter-name>characterEncoding</filter-name>
  	<filter-class>org.springframework.web.filter.CharacterEncodingFilter</filter-class>
  	<init-param>
  	  <param-name>encoding</param-name>
  	  <param-value>UTF-8</param-value>
  	</init-param>
  </filter>
  
  <filter-mapping>
  	<filter-name>characterEncoding</filter-name>
  	<url-pattern>/*</url-pattern>
  </filter-mapping>
</web-app>
~~~

## Start
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Start</title>
</head>

<body>
	<a href="start.do">스프링을 시작합니다</a>
</body>
</html>
~~~

## HelloController
~~~java
package spring.mvc.sample;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;
@Controller
// Controller : 클라이언트의 요청을 처리한 뒤, Model를 호출하고 그 결과를 DispatcherServlet에게 알려줌
public class HelloController {
	@RequestMapping("/start.do")
	public ModelAndView start() {
		System.out.println("start.do 요청 받음");
		
		// ModelAndView : Controller가 처리한 데이터 및 화면에 대한 정보를 보유한 객체
		ModelAndView m = new ModelAndView();
		m.addObject("name", "짝꿍님");
		m.addObject("message", "점심은뭐드실래요?");
//		m.setViewName("/WEB-INF/view/hello.jsp");
		// common-servlet.xml에서 앞에는 /WEB-INF/view로 끝에는 .jsp로 했기때문에 클래스명만 설정하면 된다.
		m.setViewName("hello");
		return m;
	}
}
~~~

## Hello
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>WEB-INF/view/hello.jsp</title>
</head>

<body>
	스프링시작<br/>
	${name}께, ${message} 라고전달합니다.
</body>
</html>
~~~

## AutoScan
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>AutoScan</title>
</head>
<body>
	<h2><a href="scan.do">모델 VO 얻어오기</a></h2>
</body>
</html>
~~~

## AutoScanController
~~~java
package example.member.controller;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;
import example.member.model.MemberVO;

@Controller
public class AutoScanController {
	
	@Autowired
	private MemberVO memberVO;
	
	@RequestMapping("/scan.do")
	public ModelAndView test() {
		System.out.println("scan.do 요청");
		
		ModelAndView m = new ModelAndView();
		m.addObject("vo", memberVO);
		m.setViewName("scan");
		System.out.println(m);
		return m;
	}
}
~~~

## MemberVO
~~~java
package example.member.model;
public class MemberVO {
	private String id;
	private String name;
	private int age;
	private boolean state;

	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public boolean isState() {
		return state;
	}
	public void setState(boolean state) {
		this.state = state;
	}
}
~~~

## Scan
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>/WEB-INF/view/scan.jsp</title>
</head>

<body>
	아이디 : ${vo.id} <br/>
	이름 : ${vo.name} <br/>
	나이 : ${vo.age} <br/>
</body>
</html>
~~~

## RequestMapping
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>RequestMapping</title>
</head>

<body>
	<h3>요청 확인</h3>
	<a href="re/a.do">요청1</a><br/>
	<a href="re/b.do">요청2</a><br/>
	<a href="re/c.do?id=hong">요청3</a><br/>
	<a href="re/c.do">요청4</a><br/>
	<hr/>
	
	<h3>폼의 데이타</h3>
	<form action="re/request.do" method="post">
		id : <input type="text" name="id"><br/>
		name : <input type="text" name="name"><br/>
		age : <input type="text" name="age"><br/>
		<input type="submit" value="전송"/>
	</form>
</body>
</html>
~~~

## RequestMappingController
~~~java
package example.member.controller;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import example.member.model.MemberVO;

@Controller
@RequestMapping("/re")
public class RequestMappingController {
/*
	리턴형 void : 요청과 동일한 이름의 뷰페이지로 전달
	리턴형 String : 문자열과 동일한 뷰페이지로 전달 
*/
	@RequestMapping(value={"/a.do", "/b.do"})
	public String test() {
		System.out.println("a.do요청과 b.do요청");
		return "hello"; // 뷰페이지 - /WEB-INF/view/ + 이름 + .jsp
	}
	
	@RequestMapping(value="/c.do", params={"id=hong"})
	public void test2(String id) {
		System.out.println("c.do요청 -> " + id);
	}
	
	@RequestMapping(value="/request.do", method=RequestMethod.POST)
	public void request(@ModelAttribute("vo") MemberVO vo) {
		System.out.println("re/request.do 요청");
		System.out.println(vo.getName() + "입력확인");
	}
}
~~~

## Request
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>/WEB-INF/view/re/request.jsp</title>
</head>

<body>
	뷰페이지입니다 <br/>
	아이디 : ${param.id} <br/>
	이름 : ${param.name} <br/>
	나이 : ${param.age} <br/>
	<hr/>
	객체명으로 출력<br/>
	아이디 : ${memberVO.id} <br/>
	이름 : ${memberVO.name} <br/>
	나이 : ${memberVO.age} <br/>
	<hr/>
	지정 변수명으로 출력<br/>
	아이디 : ${vo.id} <br/>
	이름 : ${vo.name} <br/>
	나이 : ${vo.age} <br/>	
</body>
</html>
~~~

## C
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>/WEB-INF/view/re/c.jsp</title>
</head>

<body>
	c.do 요청의 결과<br/>
	넘겨받은 id 값 출력 : ${param.id} <br/>
</body>
</html>
~~~

## ListProperties
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>ListProperties</title>
</head>

<body>
	<form action="multiInsert.do" method="post">
		<table width="600">
			<tr>
				<th width="80">선택</th>
				<th width="210">아이디</th>
				<th width="260">이름</th>
				<th width="50">나이</th>
			</tr>
			<tr>
				<td><input type="checkbox" name="list[0].state"/></td>
				<td><input type="text" name="list[0].id"/></td>
				<td><input type="text" name="list[0].name"/></td>
				<td><input type="text" name="list[0].age"/></td>
			</tr>
			<tr>
				<td><input type="checkbox" name="list[1].state"/></td>
				<td><input type="text" name="list[1].id"/></td>
				<td><input type="text" name="list[1].name"/></td>
				<td><input type="text" name="list[1].age"/></td>
			</tr>
			<tr>
				<td><input type="checkbox" name="list[2].state"/></td>
				<td><input type="text" name="list[2].id"/></td>
				<td><input type="text" name="list[2].name"/></td>
				<td><input type="text" name="list[2].age"/></td>
			</tr>
			<tr>
				<td colspan="4" align="center"><input type="submit" value="입력"/></td>
			</tr>
		</table>
	</form>
</body>
</html>
~~~

## ListPropertiesController
~~~java
package example.member.controller;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import example.member.model.MemberVO;
import example.member.model.MemberVOList;

@Controller
public class ListPropertiesController {
	
	@RequestMapping("/multiInsert.do")
	public void test(MemberVOList memberList) {
		System.out.println("multiInsert.do 요청");
		
		for(MemberVO vo : memberList.getList()) {
			System.out.printf("state=%s, id=%s, name=%10s, age=%d", vo.isState(), vo.getId(), vo.getName(), vo.getAge());
		}
	}
}
~~~

## MultiInsert
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>/WEB-INF/view/multiInsert.jsp</title>
</head>

<body>
	<h3>멤버 리스트</h3>
	<table border="1">
	<tr>
		<td>아이디</td>
		<td>이름</td>
		<td>나이</td>
	</tr>
	
	<!-- ArrayList에서 하나씩 가져오기 -->
	<c:forEach var="a" items="${memberVOList.list}">
		<c:if test="${a.state}">
			<tr>
				<td>${a.id}</td>
				<td>${a.name}</td>
				<td>${a.age}</td>
			</tr>
		</c:if>
	</c:forEach>
	</table>
</body>
</html>
~~~

## Parameter
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
	<title>Parameter</title>
	</head>
<body>
	<h2>파라메터 연습</h2>
	<a href="param.do?id=hong&age=30">파라메터 요청</a>
	
	<!-- MemberVO와 변수명과 name을 같게 해준다. -->
	<h2>폼 파라메터 연습 - 로그인처럼</h2>
	<form action="paramForm.do" method="post">
		id : <input type="text" name="id"/><br/>
		name : <input type="text" name="name"/><br/>
		<input type="submit"/>
	</form>
</body>
</html>
~~~

## ParameterController
~~~java
package example.member.controller;
import javax.servlet.http.HttpSession;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import example.member.model.MemberVO;

@Controller
public class ParameterController {
	// param.do 요청 받아서 뷰 param.jsp에서 파라메터 값 출력 
	@RequestMapping("/param.do")
/*
	public String test(String id, int age) {
		System.out.println("param.do 요청");
		return "param";
	}
*/
	public void test() {
		System.out.println("param.do 요청");
	}
	
	@RequestMapping("/paramForm.do")
	public void test2(MemberVO vo, HttpSession session) {
		System.out.println("paramForm.do 요청");
		
		String dbId = "001";	// DB 검색결과
		String dbName = "홍길동";
		
		// 입력값과 DB값이 모두 동일하면 세션에 저장
		if(vo.getId().equals(dbId) && vo.getName().equals(dbName)) {
			session.setAttribute("login", dbId + "로그인");
		}else {
			System.out.println("로그인실패하셨습니다.");
		}
	}
}
~~~

## Param
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>/WEB-INF/view/param.jsp</title>
</head>

<body>
	아이디 : ${param.id} <br/>
	나이 : ${param.age} <br/>
</body>
</html>
~~~

## ParamForm
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>/WEB-INF/view/paramForm.jsp</title>
</head>

<body>
	아이디 : ${memberVO.id} <br/>
	이름 : ${memberVO.name} <br/>
	<hr/>
	세션값 : ${sessionScope.login}<br/>
</body>
</html>
~~~

## ReturnType
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>ReturnType</title>
</head>

<body>
	<a href="map.do">Map 리턴</a>
	<a href="model.do">Model 리턴</a>
</body>
</html
~~~

## ReturnTypeController
~~~java
package example.member.controller;
import java.util.HashMap;
import java.util.Map;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class ReturnTypeController {
	
	@RequestMapping("/map.do")
	public Map test() {
		System.out.println("map.do 요청");
		Map<String, String> m = new HashMap<String, String>();
		m.put("age", "22");
		m.put("hobby", "음주가무");
		return m;
	} // 리턴형 Map : 요청과 동일한 이름의 뷰페이지로 전달
	
	@RequestMapping("/model.do")
	public void test2(Model m) {
		System.out.println("model.do 요청");
		// Model 인자에 지정 - 값을 넘겨받는 것이 아니라 뷰쪽으로 전달하는 객체이다.
		m.addAttribute("message", "오늘은뭐드실거");
		m.addAttribute("addr", "동네");
	}
}
~~~

## Map
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>/WEB-INF/view/map.jsp</title>
</head>
<body>
	<!-- Map에서는 키, 값으로 오기때문에 키 값만 적어줘도 된다. -->
	나이 : ${age} <br/>
	취미 : ${hobby} <br/>
</body>
</html>
~~~

## Model
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>/WEB-INF/view/model.jsp</title>
</head>

<body>
	메시지 : ${message} <br/>
	주소 : ${addr} <br/>
</body>
</html>
~~~

## ModelAttribute
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>ModelAttribute</title>
</head>

<body>
	<a href="modelAttr.do">ModelAttribute 요청</a>
</body>
</html>
~~~

## ModelAttributeController
~~~java
package example.member.controller;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import example.member.model.MemberVO;

@Controller
public class ModelAttributeController {
	
	@RequestMapping("/modelAttr.do")
	public void test() {
		System.out.println("modelAttr.do 요청");
/*		
		기본적인 방법 - 뷰로 데이타를 전달하는 방법
		1. Map
		2. ModelAndView
		3. Model
*/		
	}
	
	@ModelAttribute("message")
	public String attr() {
		return "행복한 수요일";
	}
	
	@ModelAttribute("memberVO")
	public MemberVO attr2() {
		MemberVO vo = new MemberVO();
		vo.setId("002");
		vo.setName("홍길동");
		vo.setAge(24);
		return vo;
	}
}
~~~

## ModelAttr
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>/WEB-INF/view/modelAttr.jsp</title>
</head>

<body>
	메시지 : ${message} <br/>
	<hr/>
	아이디 : ${memberVO.id} <br/>
	이름 : ${memberVO.name} <br/>
	나이 : ${memberVO.age} <br/>
</body>
</html>
~~~

## Redirect
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Redirect</title>
</head>

<body>
	<a href="select.do">목록보기</a><br/>
	<a href="insert.do">입력하기</a>
</body>
</html>
~~~

## RedirectController
~~~java
package example.member.controller;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class RedirectController {

	@RequestMapping("/select.do")
	public ModelAndView test() {
		System.out.println("select.do 요청");
		ModelAndView mv = new ModelAndView();
		mv.addObject("info", "목록페이지입니다");
		mv.setViewName("redictResult");
		return mv;
	}
	
	@RequestMapping("/insert.do")
	public String test2() {
		System.out.println("insert.do 요청");
		return "redirect:select.do";
	}
}
~~~

## RedictResult
~~~jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>/WEB-INF/view/redictResult.jsp</title>
</head>

<body>
	<h2>목록페이지</h2>
</body>
</html>
~~~