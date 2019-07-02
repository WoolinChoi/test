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
	<h2><a href="autoscan.do">모델 VO 얻어오기</a></h2>
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
	@RequestMapping("/autoscan.do")
	public ModelAndView test() {
		System.out.println("autoScan.do 요청");
		ModelAndView m = new ModelAndView();
		m.addObject("vo", memberVO);
		System.out.println(m);
		m.setViewName("autoscan");
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

## Autoscan
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
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import example.member.model.MemberVO;
@Controller
@RequestMapping("/re")
public class RequestMappingController {
	@RequestMapping(value="/request.do", method=RequestMethod.POST)
	public void request(MemberVO vo) {
		System.out.println("re/request.do 요청");
		System.out.println(vo.getName() + "입력확인");
	}
	// **** 리턴형이 void이면 요청이름과 동일한 뷰 페이지 지정
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
	<title>Request</title>
</head>

<body>
	뷰페이지입니다 <br/>
	아이디 : ${param.id} <br/>
	이름 : ${param.name} <br/>
	나이 : ${param.age} <br/>
	<hr/>
</body>
</html>
~~~