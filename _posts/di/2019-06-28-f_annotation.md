---
layout: post
title: annotation
category: di
tags: [java, di, annotation]
comments: false
---

# [annotation]()

## MainApp
~~~java
package ex2_annotation;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
public class MainApp {
	public static void main(String[] args) {
		ApplicationContext cxt = new ClassPathXmlApplicationContext("ex2_annotation/apConfig.xml");
		
//		MemberBean mem = cxt.getBean("memberBean", MemberBean.class);
//		mem.output();
		
		MemberDAO dao = cxt.getBean("memberDAO", MemberDAO.class);
		dao.insert();
	}
}
~~~

## MemberBean
~~~java
package ex2_annotation;
import org.springframework.stereotype.Component;
@Component
public class MemberBean {
	private String name;
	private int age;
	private String message;
	
	// contructor
	public MemberBean() {}
	
	public MemberBean(String name, int age, String message) {
		super();
		this.name = name;
		this.age = age;
		this.message = message;
	}
	
	// getter, setter
	public String getName() {
		return name;
	}
	public int getAge() {
		return age;
	}
	public String getMessage() {
		return message;
	}
	public void setName(String name) {
		this.name = name;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public void setMessage(String message) {
		this.message = message;
	}
	
	public void output() {
		System.out.println(name + "(" + age + ") " + message);
	}
}
~~~

## MemberDAO
~~~java
package ex2_annotation;
import javax.annotation.Resource;
import org.springframework.stereotype.Component;
@Component
public class MemberDAO {
	// 내가 불러오고싶은 name을 지정해준다.
/*
	@Autowired
	@Qualifier("memberBean2")
*/
	@Resource(name="memberBean2")
	private MemberBean member;

/*
	// contructor
	public MemberDAO() {}
	
	public MemberDAO(MemberBean member) {
		this.member = member;
	}
	
	// setter
	public void setMember(MemberBean member) {
		this.member = member;
	}
*/	
	public void insert() {
		System.out.println(member.getName() + "님 정보가 입력");
	}
}
~~~

## ApplicationContext_xml
~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:context="http://www.springframework.org/schema/context"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.3.xsd">
<!-- bean에 id는 클래스의 앞글자 소문자로 해준다. -->
<bean id="memberBean" class="ex2_annotation.MemberBean">
	<property name="name" value="홍홍홍"/>
	<property name="age" value="33"/>
	<property name="message" value="지각자안녕"/>
</bean>

<bean id="memberBean2" class="ex2_annotation.MemberBean">
	<property name="name" value="범돌이"/>
	<property name="age" value="27"/>
	<property name="message" value="안녕"/>
</bean>

<!-- @Component 애너테이션이 붙은 클래스들을 Bean 으로 자동 등록해 준다. -->
<context:component-scan base-package="ex2_annotation"/>
</beans>
~~~